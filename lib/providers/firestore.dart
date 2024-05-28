import 'dart:convert';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:collection/collection.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:timezone/timezone.dart';

import '/models.dart';
import 'shared_preferences.dart';

T? snapshotData<T>(DocumentSnapshot<Map<String, dynamic>> snapshot) {
  if (snapshot.data() case {'json': String json}) {
    return jsonDecode(json) as T;
  }
  return null;
}

final firebaseProvider = Provider((ref) => FirebaseFirestore.instance);

final tournamentListProvider = StreamProvider((ref) {
  final db = ref.watch(firebaseProvider);
  final snapshots = switch (kDebugMode) {
    true => db.collection('tournaments').snapshots(),
    false => db
        .collection('tournaments')
        .where('status', isEqualTo: 'live')
        .snapshots(),
  };

  return snapshots.map((query) => [
        for (final doc in query.docs)
          TournamentData.fromJson({
            'id': doc.id,
            'address': '',
            ...(doc.data() as Map).cast(),
          }),
      ]);
});

final tournamentProvider = StreamProvider<TournamentData>((ref) async* {
  final db = ref.watch(firebaseProvider);
  final tournamentId = ref.watch(tournamentIdProvider);
  if (tournamentId == null) return;

  yield* db
      .collection('tournaments')
      .doc(tournamentId)
      .snapshots()
      .map((snapshot) => TournamentData.fromJson({
            'id': snapshot.id,
            'address': '',
            ...(snapshot.data() as Map).cast(),
          }));
});

final tournamentCollectionProvider = Provider((ref) {
  final db = ref.watch(firebaseProvider);
  final tournamentId = ref.watch(tournamentIdProvider);
  if (tournamentId == null) return null;

  return db.collection('tournaments').doc(tournamentId).collection('json');
});

final playerListProvider = StreamProvider<List<PlayerData>>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('players')
      .snapshots()
      .map(snapshotData<List<dynamic>>)
      .map((e) => e ?? const [])
      .map((data) => [
        for (final player in data) PlayerData((player as Map).cast()),
      ]);
});

final selectedPlayerProvider = Provider((ref) {
  final selectedPlayerId = ref.watch(selectedPlayerIdProvider);
  if (selectedPlayerId == null) return null;

  final playerList = ref.watch(playerListProvider).valueOrNull;
  return playerList
      ?.firstWhereOrNull((player) => player.id == selectedPlayerId);
});


final scoresBaseProvider = StreamProvider<Map>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('scores') //
      .snapshots()
      .map(snapshotData<Map>)
      .map((e) => e ?? const {});
});


final scoresProvider = StreamProvider<List<ScoreData>>((ref) async* {
  final scoresBase = ref.watch(scoresBaseProvider);

  yield* scoresBase.when(
    data: (data) {
      final int done = data['roundDone'];
      List<ScoreData> out = [
        for (final score in data[done])
          ScoreData.fromJson((score as Map).cast())
      ];
      return Stream.value(out);
    },
    loading: () => const Stream.empty(),
    error: (_, __) => const Stream.empty(),
  );
});


final seatingProvider = StreamProvider<List<RoundData>>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('seating') //
      .snapshots()
      .map(snapshotData<List<dynamic>>)
      .map((e) => e ?? const {})
      .map((data) => [
            for (final round in data) RoundData.fromJson((round as Map).cast()),
          ]);
});

final gamesProvider = StreamProvider<List<GameData>>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('games') //
      .snapshots()
      .map(snapshotData<List<dynamic>>)
      .map((e) => e ?? const {})
      .map((data) => [
            for (final round in data) GameData.fromCloud((round as Map).cast()),
          ]);
});

final scheduleProvider = StreamProvider<ScheduleData>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('schedule') //
      .snapshots()
      .map(snapshotData<Map<String, dynamic>>)
      .map((data) => data != null
          ? ScheduleData.fromJson(data.cast())
          : ScheduleData(timezone: UTC, rounds: const []));
});

final roundsProvider = Provider((ref) {
  final scores = ref.watch(scoresBaseProvider);
  return scores.maybeWhen(
    data: (data) {
      return data['roundDone'] ?? 0;
    },
      orElse: () => 0,
  );
});

typedef RoundScore = ({
  String name,
  DateTime start,
  int score,
});

typedef PlayerScore = ({
  PlayerId id,
  String name,
  String rank,
  int total,
  int penalty,
  List<RoundScore> roundScores,
});

final playerScoreListProvider = StreamProvider((ref) async* {
  final scores = await ref.watch(scoresProvider.future);
  final playerList = await ref.watch(playerListProvider.future);
  final schedule = await ref.watch(scheduleProvider.future);

  final playerNames =
      Map.fromEntries(playerList.map((e) => MapEntry(e.id, e.name)));

  yield [
    for (final score in scores)
      (
        id: score.id,
        name: playerNames[score.id]!,
        rank: score.rank,
        total: score.total,
        penalty: score.penalty,
        roundScores: score.roundScores.indexed
            .map((score) => (
                  name: schedule.rounds[score.$1].name,
                  start: DateTime.now(),
                  score: score.$2,
                ))
            .toList(),
      )
  ];
});
