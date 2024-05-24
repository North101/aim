# -*- coding: utf-8 -*-
'''
pages and backend for the user running the tournament
'''
import json
import os
import threading

from firebase_admin import messaging
from flask import Blueprint, redirect, url_for, render_template, \
    copy_current_request_context, current_app, request
from flask_login import login_required, current_user

from create.write_sheet import googlesheet
from models import Access
from oauth_setup import db, firestore_client

blueprint = Blueprint('run', __name__)


def prettyScore(score: int):
    if score < 0:
        prefix = '-'
    elif score > 0:
        prefix = '+'
    else:
        prefix = ''
    return f"{prefix} {(abs(round(score/10, 1)))}"


@blueprint.route('/run/select_tournament', methods=['GET', 'POST',])
@login_required
def select_tournament():
    new_id = request.form.get('id')
    if new_id:
        current_user.live_tournament_id = new_id
        db.session.commit()
        return redirect(url_for('run.run_tournament'))
    # Query the Access table for all records where the user_email is the current user's email
    accesses = db.session.query(Access).filter_by(
        user_email=current_user.email).all()
    tournaments = [access.tournament for access in accesses]
    return render_template('select_tournament.html', tournaments=tournaments)


@login_required
def publish_scores_on_web(scores, players):
    env = current_app.jinja_env
    env.filters['prettyScore'] = prettyScore
    title = current_user.live_tournament.title
    html = render_template('scores.html',
                           title=title,
                           scores=scores,
                           players=players,
                           )
    fn = os.path.join(
        current_user.live_tournament.web_directory,
        'scores.html')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)

    return 'scores.html has been updated, notifications sent', 200


@login_required
def _send_topic_fcm(topic: str, title: str, body: str):
    message = messaging.Message(
        notification = messaging.Notification(title=title,body=body,),
        topic=topic,  # The topic name
        )
    messaging.send(message)


@blueprint.route('/run/')
@login_required
def run_tournament():
    if current_user.live_tournament:
        return render_template('run_tournament.html')
    return redirect(url_for('create.index'))


@login_required
def _get_sheet():
    sheet_id = current_user.live_tournament_id
    return googlesheet.get_sheet(sheet_id)


@blueprint.route('/run/update_schedule')
@login_required
def update_schedule():
    sheet = _get_sheet()
    _schedule_to_cloud(sheet)
    _send_messages('schedule updated')
    return "SCHEDULE updated, notifications sent", 200


@blueprint.route('/run/update_seating')
@login_required
def update_seating():
    sheet = _get_sheet()
    schedule = _schedule_to_cloud(sheet)
    _seating_to_cloud(sheet, schedule)
    _send_messages('seating updated')
    return "SEATING PLAN updated, notifications sent", 200


@blueprint.route('/run/update_players')
@login_required
def update_players():
    sheet = _get_sheet()
    _players_to_cloud(sheet)
    _send_messages('player list updated')
    return "PLAYERS updated, notifications sent", 200


@login_required
def _send_messages(msg: str):
    '''
    '''
    firebase_id = current_user.live_tournament.firebase_doc
    _send_topic_fcm(firebase_id, msg, current_user.live_tournament.title)


@login_required
def _message_player_topics(scores, players):
    '''
    send all our player-specific firebase notifications out
    do this in a separate thread so as not to hold up the main response
    '''
    firebase_id = current_user.live_tournament.firebase_doc
    done = scores[0]['roundDone']
    for s in scores:
        name = players[s['id']]
        _send_topic_fcm(
            f"{firebase_id}-{s['id']}",
            f"{name} is now in position {s['r']}",
            f"with {s['t']} points after {done} round(s)",
            )



@blueprint.route('/run/test')
@login_required
def get_game_results():
    sheet = _get_sheet()
    vals = googlesheet.get_table_results(1, sheet)

    row : int = 4
    tables = {}
    while row + 3 < len(vals):
        # Get the table number from column 1
        table = vals[row][0]
        tables[table] = []
        if not table:
            # end of score page
            break
        # For each table, get the player ID & scores
        for i in range(4):
            tables[table].append([
                vals[row + i][1], # player_id
                round(10 * vals[row + i][3] or 0), # chombo
                round(10* vals[row + i][4]), # game score
                vals[row + i][5], # placement
                round(10 * vals[row + i][6]), # final score
                ])

        # Move to the next table
        row += 7

    return f"{vals[0][1]} : {tables}", 200


@blueprint.route('/run/get_results')
@login_required
def sheet_to_cloud():
    sheet = _get_sheet()

    players = _players_to_cloud(sheet)
    scores = _scores_to_cloud(sheet)
    schedule = _schedule_to_cloud(sheet)
    _seating_to_cloud(sheet, schedule)

    @copy_current_request_context
    def _fcm_all_players():
        _message_player_topics(scores, players)

    thread = threading.Thread(target=_fcm_all_players)
    thread.start()
    return publish_scores_on_web(scores, players)


@login_required
def _scores_to_cloud(sheet):
    done, results = googlesheet.get_results(sheet)
    body = results[1:]
    body.sort(key=lambda x: -x[3]) # sort by descending cumulative score
    all_scores = []
    previous_score = -99999
    for i in range(len(body)):
        total = round(10 * body[i][3])
        if previous_score == total:
            prefix = '='
        else:
            previous_score = total
            rank = i + 1
            prefix = ''

        all_scores.append({
            "id": body[i][0],
            "t": total,
            "r": f'{prefix}{rank}',
            "p": round(body[i][4] * 10),
            "s": [round(10 * s) for s in body[i][5 : 5 + done]],
            })


    all_scores[0]['roundDone'] = done
    _save_to_cloud('scores', all_scores)
    return all_scores


@login_required
def _schedule_to_cloud(sheet):
    schedule: list(list) = googlesheet.get_schedule(sheet)
    _save_to_cloud('schedule', schedule)
    return schedule


@login_required
def _players_to_cloud(sheet):
    raw : list(list) = googlesheet.get_players(sheet)
    players = {int(p[0]): p[2] for p in raw}
    _save_to_cloud('players', players)
    return players


@login_required
def _seating_to_cloud(sheet, schedule):
    raw = googlesheet.get_seating(sheet)
    seating = []
    previous_round = ''
    hanchan_number = 0
    for t in raw:
        this_round = str(t[0])
        table = str(t[1])
        players = t[2:]
        if this_round != previous_round:
            previous_round = this_round
            seating.append({
                'id': this_round,
                'tables': {},
                })
            hanchan_number = hanchan_number + 1
        seating[-1]['tables'][table] = players

    _save_to_cloud('seating', seating)
    # return seating


@login_required
def _save_to_cloud(key: str, data):
    firebase_id : str = current_user.live_tournament.firebase_doc
    ref = firestore_client.collection("tournaments")
    out : str = json.dumps(data, ensure_ascii=False, indent=None)
    ref.document(f"{firebase_id}/json/{key}").set(document_data={
        'json': out})
