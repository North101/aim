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
    this.url_icon,
  });

  factory TournamentData.fromMap(Map<String, dynamic> data) => TournamentData(
        id: data['id'] as TournamentId,
        name: data['name'] as String,
        address: data['address'] as String,
        country: data['country'] as String,
        startDate: data['start_date'] as Timestamp,
        endDate: data['end_date'] as Timestamp,
        status: data['status'] as String,
        rules: data['rules'] as String,
        url_icon: data.containsKey('url_icon') ? data['url_icon'] as String : null,
      );

  final TournamentId id;
  final String name;
  final String address;
  final String country;
  final Timestamp startDate;
  final Timestamp endDate;
  final String status;
  final String rules;
  final String? url_icon; // may not be present, hence can be null

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
        url_icon,
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
typedef TableId = String;

class ScheduleData extends Equatable {
  const ScheduleData({
    required this.timezone,
    required this.rounds,
  });

  factory ScheduleData.fromSeating(Map<String, dynamic> data) {
    final location = getLocation(data['timezone'].toString());

    List<RoundScheduleData> rounds = [];
    for (final Map<String, dynamic> roundSchedule in data['rounds']) {
      RoundScheduleData newRound = RoundScheduleData.fromMap(
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

  factory RoundScheduleData.fromMap(
    Map<String, dynamic> data,
    Location location,
  ) =>
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
  List<Object?> get props => [
        name,
        start,
      ];
}

class RankData extends Equatable {
  // one player's score
  const RankData({
    required this.id,
    required this.rank,
    required this.total,
    required this.penalty,
  });

  factory RankData.fromMap(int id, Map<String, dynamic> data) => RankData(
        id: id,
        rank: "${data['t'] == 1 ? '=' : ''}${data['r']}",
        total: data['total'] as int,
        penalty: data['p'] as int,
      );

  final PlayerId id;
  final String rank;
  final int total;
  final int penalty;

  @override
  List<Object?> get props => [
        id,
        rank,
        total,
        penalty,
      ];
}

extension RoundDataList on List<RoundData> {
  // seating
  Iterable<RoundData> withPlayerId(PlayerId? playerId) => playerId == null
      ? this
      : map((round) => RoundData(
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

  factory RoundData.fromMap(Map<String, dynamic> data) => RoundData(
        id: data['id'] as String,
        tables: data.containsKey('tables') ? (data['tables'] as Map).map(
          (key, value) => MapEntry(
            key as String,
            (value as List).cast(),
          ),
        ) : {},
      );

  final String id;
  final Map<String, List<PlayerId>> tables;

  String tableNameForPlayerId(PlayerId playerId) =>
      tables.entries.firstWhere((e) => e.value.contains(playerId)).key;

  @override
  List<Object?> get props => [
        id,
        tables,
      ];
}

extension HanchanList on List<GameData> {
  // List of detailed results for a given player
  List<Hanchan> withPlayerId(PlayerId playerId) {
    // get one game for each round for the given player
    return [
      for (final hanchan in this)
        for (final table in hanchan.tables.values)
          if (table.hasPlayerId(playerId)) table,
    ];
  }
}

class HanchanScore {
  // detailed score for one player at one table in one round
  final PlayerId playerId;
  final int penalties;
  final int gameScore;
  final int placement;
  final int finalScore;

  const HanchanScore({
    required this.playerId,
    required this.penalties,
    required this.gameScore,
    required this.placement,
    required this.finalScore,
  });

  factory HanchanScore.fromList(List<int> values) {
    return HanchanScore(
      playerId: values[0],
      penalties: values[1],
      gameScore: values[2],
      placement: values[3],
      finalScore: values[4],
    );
  }

  int get uma => finalScore - gameScore - penalties;
}

class Hanchan {
  // the scores for all four players at one table in one round
  final RoundId roundId;
  final TableId tableId;
  final List<HanchanScore> scores; // length 4: one HanchanScore for each player

  const Hanchan({
    required this.roundId,
    required this.tableId,
    required this.scores,
  });

  bool hasPlayerId(PlayerId playerId) =>
      scores.any((e) => e.playerId == playerId);
}

class GameData {
  // detailed scores for all hanchans in a round

  const GameData({
    required this.roundId,
    required this.tables,
  });

  final RoundId roundId;
  final Map<TableId, Hanchan> tables;

  factory GameData.fromMap(MapEntry data) {
    final roundId = data.key as RoundId;
    final tables = (data.value as Map).map((k, v) {
      final tableId = k as TableId;
      return MapEntry(
        tableId,
        Hanchan(
          roundId: roundId,
          tableId: tableId,
          scores: [
            for (final wind in Wind.values)
              HanchanScore.fromList((v['${wind.index}'] as List).cast())
          ],
        ),
      );
    });
    return GameData(roundId: roundId, tables: tables);
  }
}
