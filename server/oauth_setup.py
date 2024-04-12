# -*- coding: utf-8 -*-

import os

from authlib.integrations.flask_client import OAuth
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, DEFAULT_USERS
from models import User

oauth = OAuth()
login_manager = LoginManager()
db = SQLAlchemy()

def config_db(app):

    # Get the directory of the current file
    current_directory = os.path.dirname(os.path.realpath(__file__))
    db_file = "tournaments.sqlite3"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(current_directory, db_file)

    db.init_app(app)
    with app.app_context():
        for email in DEFAULT_USERS:
            if not db.session.query(User).get(email):
                db.session.add(User(email=email))
        db.session.commit()


def config_login_manager(app):
    login_manager.init_app(app)

def config_oauth(app):
    oauth.init_app(app)
    oauth.register(
        'google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'email',},
    )
