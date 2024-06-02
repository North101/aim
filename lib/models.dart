import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:equatable/equatable.dart';
import 'package:timezone/timezone.dart';

import 'utils.dart';

enum Wind {
  east('E', '東'),
  south('S', '西'),
  west('W', '南'),
  north('N', '北');

  const Wind(this.western, this.japanese);

  final String japanese;
  final String western;
}

typedef TournamentId = String;

class TournamentData extends Equatable {
  const TournamentData({
    required this.id,
    required this.name,
    required this.address,
    required this.country,
    required this.startDate,
    required this.endDate,
    required this.status,
    required this.rules,
  });

  factory TournamentData.fromJson(Map<String, dynamic> data) =>
      TournamentData(
        id: data['id'] as TournamentId,
        name: data['name'] as String,
        address: data['address'] as String,
        country: data['country'] as String,
        startDate: data['start_date'] as Timestamp,
        endDate: data['end_date'] as Timestamp,
        status: data['status'] as String,
        rules: data['rules'] as String,
      );

  final TournamentId id;
  final String name;
  final String address;
  final String country;
  final Timestamp startDate;
  final Timestamp endDate;
  final String status;
  final String rules;

  String get when => dateRange(startDate, endDate);

  @override
  List<Object?> get props =>
      [
        id,
        name,
        address,
        country,
        startDate,
        endDate,
        status,
        rules,
      ];
}

typedef PlayerId = int;

class PlayerData extends Equatable implements Comparable<PlayerData> {
  final PlayerId id;
  final String name;

  PlayerData(Map<String, dynamic> playerMap)
      : id = playerMap['id'],
        name = playerMap['name'];

  @override
  int compareTo(PlayerData other) => name.compareTo(other.name);

  @override
  List<Object?> get props =>
      [
        id,
        name,
      ];
}

extension PlayerList on List<PlayerData> {
  PlayerData? byId(PlayerId id) {
    try {
      return firstWhere((player) => player.id == id);
    } on StateError {
      return null;
    }
  }
}

typedef RoundId = String;

class ScheduleData extends Equatable {
  const ScheduleData({
    required this.timezone,
    required this.rounds,
  });

  factory ScheduleData.fromJson(Map<String, dynamic> data) {
    final location = getLocation(data['timezone'] as String);
    final roundScheduleList = data['rounds'];

    List<RoundScheduleData> rounds = [];
    for (final Map<String, dynamic> roundSchedule in roundScheduleList) {
      RoundScheduleData newRound = RoundScheduleData.fromJson(
        roundSchedule,
        location,
      );
      rounds.add(newRound);
    }

    return ScheduleData(timezone: location, rounds: rounds);
  }

  final Location timezone;
  final List<RoundScheduleData> rounds;

  @override
  List<Object?> get props =>
      [
        timezone,
        rounds,
      ];
}

class RoundScheduleData extends Equatable {
  const RoundScheduleData({
    required this.id,
    required this.name,
    required this.start,
  });

  factory RoundScheduleData.fromJson(Map<String, dynamic> data,
      Location location,) =>
      RoundScheduleData(
        id: data['id'] as RoundId,
        name: data['name'] as String,
        start: TZDateTime.from(
          DateTime.parse(data['start'] as String),
          location,
        ),
      );

  final RoundId id;
  final String name;
  final DateTime start;

  @override
  List<Object?> get props =>
      [
        name,
        start,
      ];
}

class ScoreData extends Equatable {
  // one player's score
  const ScoreData({
    required this.id,
    required this.rank,
    required this.total,
    required this.penalty,
    required this.roundScores,
  });

  factory ScoreData.fromJson(int id, Map<String, dynamic> data) =>
      ScoreData(
        id: id,
        rank: "${['', '='][data['t']]}${data['r']}",
        total: data['total'] as int,
        penalty: data['p'] as int,
        roundScores: (data['s'] as List).cast(),
      );

  final PlayerId id;
  final String rank;
  final int total;
  final int penalty;
  final List<int> roundScores;

  @override
  List<Object?> get props =>
      [
        id,
        rank,
        total,
        penalty,
        roundScores,
      ];
}

extension RoundDataList on List<RoundData> {
  // seating
  Iterable<RoundData> withPlayerId(PlayerId? playerId) =>
      playerId == null
          ? this
          : map((round) =>
          RoundData(
            id: round.id,
            tables: {
              for (final MapEntry(:key, :value) in round.tables.entries)
                if (value.contains(playerId)) key: value,
            },
          ));
}

class RoundData extends Equatable {
  // seating
  const RoundData({
    required this.id,
    required this.tables,
  });

  factory RoundData.fromJson(Map<String, dynamic> data) =>
      RoundData(
        id: data['id'] as String,
        tables: (data['tables'] as Map).map(
              (key, value) =>
              MapEntry(
                key as String,
                (value as List).cast(),
              ),
        ),
      );

  final String id;
  final Map<String, List<PlayerId>> tables;

  String tableNameForPlayerId(PlayerId playerId) =>
      tables.entries
          .firstWhere((e) => e.value.contains(playerId))
          .key;

  @override
  List<Object?> get props =>
      [
        id,
        tables,
      ];
}

extension HanchanList on List<GameData> {
  // List of detailed results for a given player
  List<Hanchan> withPlayerId(PlayerId playerId) {
    List<Hanchan> out = [];
    for (final GameData round in this) {
      // get one game for each round for the given player
      out.add(round.tables.values.firstWhere(
              (Hanchan h) => h.playerIndex(playerId) > -1));
    }
    return out;
  }
}

class HanchanScore {
  // detailed score for one player at one table in one round
  late PlayerId playerId;
  late int penalties;
  late int gameScore;
  late int placement;
  late int finalScore;
  late int rank;
  late bool tied;
  late int uma;

  HanchanScore(List<int> initScores) {
    playerId = initScores[0];
    penalties = initScores[1];
    gameScore = initScores[2];
    placement = initScores[3];
    finalScore = initScores[4];
    uma = finalScore - gameScore - penalties;
  }
}

class Hanchan {
  // the scores for all four players at one table in one round
  final RoundId roundId;
  final int tableId;
  late Map<PlayerId, int> _players;
  late List<HanchanScore> scores; // length 4: one HanchanScore for each player

  Hanchan({
    required this.roundId,
    required this.tableId,
    required initScores,
  }) {
    _players = {};
    scores = [];
    int i = 0;
    for (List score in initScores) {
      HanchanScore player = HanchanScore(score.cast<int>());
      scores.add(player);
      _players[player.playerId] = i;
      i++;
    }
  }

  int playerIndex(PlayerId pid) {
    // the ?? -1 is unnecessary, but the linter doesn't realise that
    return _players.containsKey(pid) ? (_players[pid] ?? -1) : -1;
  }
}

class GameData { // detailed scores for all hanchans in a round

  GameData({
    required this.roundId,
    required this.tables,
  });

  final RoundId roundId;
  final Map<String, Hanchan> tables;

  factory GameData.fromJson(Map<String, dynamic> data) => GameData(
        roundId: data['roundIndex'].toString(),
        tables: (data['games'] as Map).map(
          (tableId, scoresList) => MapEntry(
              tableId.toString(),
              Hanchan(
                roundId: data['roundIndex'].toString(),
                tableId: int.parse(tableId),
                initScores: scoresList.cast(),
              )),
        ),
      );
}
