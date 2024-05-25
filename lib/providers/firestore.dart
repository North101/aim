import 'package:collection/collection.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import 'firestore/games.dart';
import 'firestore/players.dart';
import 'firestore/schedule.dart';
import 'firestore/scores.dart';

export 'firestore/games.dart';
export 'firestore/players.dart';
export 'firestore/schedule.dart';
export 'firestore/scores.dart';
export 'firestore/seating.dart';
export 'firestore/tournament.dart';

final roundListProvider = StreamProvider((ref) async* {
  final roundScheduleList = await ref.watch(roundScheduleListProvider.future);
  final roundGameList = await ref.watch(roundGameListProvider.future);
  yield [
    for (final (index, round) in roundScheduleList.indexed)
      if (roundGameList.elementAtOrNull(index) case RoundGameData gameRound)
        (
          round: round,
          tables: gameRound.tables,
        )
  ];
});

typedef Score = ({
  int roundId,
  int tableId,
  HanchanScore score,
});

typedef PlayerRankedResults = ({
  PlayerData player,
  List<Score> scores,
  int finalScore,
  int gameScore,
  int penalites,
  int rank,
  bool tied,
});

final scoreListProvider = StreamProvider<Iterable<Score>>((ref) async* {
  final roundGameList = await ref.watch(roundGameListProvider.future);
  yield roundGameList
      .map(
        (game) => game.tables.map(
          (table) => table.scores.map(
            (score) => (
              roundId: game.roundIndex,
              tableId: table.tableId,
              score: score,
            ),
          ),
        ),
      )
      .flattened
      .flattened;
});

final scoreMapProvider =
    StreamProvider<Map<PlayerId, List<Score>>>((ref) async* {
  final scoreList = await ref.watch(scoreListProvider.future);
  yield scoreList.groupListsBy((score) => score.score.playerId);
});

final playerScoreListProvider =
    StreamProvider<List<PlayerRankedResults>>((ref) async* {
  final playerList = await ref.watch(playerListProvider.future);
  final scoreMap = await ref.watch(scoreMapProvider.future);
  final playerRankMap = await ref.watch(playerRankMapProvider.future);

  yield playerList.map((player) {
    final playerScores = scoreMap[player.id] ?? [];
    final playerRank = playerRankMap[player.id];
    return (
      player: player,
      scores: playerScores,
      finalScore: playerScores.map((score) => score.score.finalScore).sum,
      gameScore: playerScores.map((score) => score.score.gameScore).sum,
      penalites: playerScores.map((score) => score.score.penalties).sum,
      rank: playerRank?.rank ?? 0,
      tied: playerRank?.tied ?? false,
    );
  }).sortedBy<num>((player) => player.rank);
});
