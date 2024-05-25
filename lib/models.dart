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

  factory TournamentData.fromJson(Map<String, dynamic> data) => TournamentData(
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
  List<Object?> get props => [
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
  const PlayerData(this.id, this.name);

  factory PlayerData.fromJson(Map<String, dynamic> data) => PlayerData(
        data['id'] as PlayerId,
        data['name'] as String,
      );

  final PlayerId id;
  final String name;

  @override
  int compareTo(PlayerData other) => name.compareTo(other.name);

  @override
  List<Object?> get props => [
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
    final rounds = data['rounds'] as List;
    return ScheduleData(
      timezone: location,
      rounds: [
        for (final roundSchedule in rounds)
          RoundScheduleData.fromJson(
            roundSchedule,
            location,
          ),
      ],
    );
  }

  final Location timezone;
  final List<RoundScheduleData> rounds;

  @override
  List<Object?> get props => [
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

  factory RoundScheduleData.fromJson(
    Map<String, dynamic> data,
    Location location,
  ) =>
      RoundScheduleData(
        id: data['id'].toString(),
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
  List<Object?> get props => [
        name,
        start,
      ];
}

class RoundTableData extends Equatable {
  // seating
  const RoundTableData({
    required this.id,
    required this.tables,
  });

  factory RoundTableData.fromJson(Map<String, dynamic> data) => RoundTableData(
        id: data['id'].toString(),
        tables: (data['tables'] as Map).map(
          (key, value) => MapEntry(
            key as String,
            (value as List).cast(),
          ),
        ),
      );

  final RoundId id;
  final Map<String, List<PlayerId>> tables;

  @override
  List<Object?> get props => [
        id,
        tables,
      ];
}

class HanchanScore extends Equatable {
  // detailed score for one player at one table in one round
  const HanchanScore({
    required this.playerId,
    required this.placement,
    required this.finalScore,
    required this.gameScore,
    required this.penalties,
  });

  factory HanchanScore.fromList(List<dynamic> data) => HanchanScore(
        playerId: data[0] as int,
        penalties: data[1] as int,
        gameScore: data[2] as int,
        placement: data[3] as int,
        finalScore: data[4] as int,
      );

  final PlayerId playerId;
  final int placement;
  final int finalScore;
  final int gameScore;
  final int penalties;
  int get uma => finalScore - gameScore - penalties;

  @override
  List<Object?> get props => [
        playerId,
        placement,
        finalScore,
        gameScore,
        penalties,
      ];
}

class Hanchan extends Equatable {
  // the scores for all four players at one table in one round
  const Hanchan({
    required this.tableId,
    required this.scores,
  });

  final int tableId;
  // length 4 - one HanchanScore for each player
  final List<HanchanScore> scores;

  @override
  List<Object?> get props => [
        tableId,
        scores,
      ];
}

class RoundGameData extends Equatable {
  // detailed scores for all hanchans in a round
  const RoundGameData({
    required this.roundIndex,
    required this.tables,
  });

  final int roundIndex;
  final List<Hanchan> tables;

  factory RoundGameData.fromJson(Map<String, dynamic> data) => RoundGameData(
        roundIndex: data['roundIndex'] as int,
        tables: [
          for (final MapEntry(key: tableId, value: scoresList)
              in (data['games'] as Map).entries)
            Hanchan(
              tableId: int.parse(tableId),
              scores: [
                for (final scores in (scoresList as List))
                  HanchanScore.fromList((scores as List).cast())
              ],
            ),
        ],
      );

  @override
  List<Object?> get props => [
        roundIndex,
        tables,
      ];
}

class ScoresData extends Equatable {
  const ScoresData({
    required this.roundDone,
    required this.scores,
  });

  factory ScoresData.fromJson(Map<String, dynamic> data) => ScoresData(
        roundDone: data['roundsDone'] as int,
        scores: {
          for (final MapEntry(:key, :value) in (data as Map).entries)
            key: PlayerScoreData.fromJson(value),
        },
      );

  final int roundDone;
  final Map<RoundId, PlayerScoreData> scores;

  @override
  List<Object?> get props => [
        roundDone,
        scores,
      ];
}

class PlayerScoreData extends Equatable {
  const PlayerScoreData({
    required this.id,
    required this.total,
    required this.penalties,
    required this.scores,
    required this.rank,
    required this.tied,
  });

  factory PlayerScoreData.fromJson(Map<String, dynamic> data) {
    return PlayerScoreData(
      id: data['id'] as PlayerId,
      total: data['total'],
      penalties: data['p'] as int,
      scores: (data['s'] as List).cast(),
      rank: data['r'] as int,
      tied: (data['t'] as int) == 1,
    );
  }

  final PlayerId id;
  final int total;
  final int penalties;
  final List<int> scores;
  final int rank;
  final bool tied;

  @override
  List<Object?> get props => [
        penalties,
        scores,
        rank,
        tied,
      ];
}
