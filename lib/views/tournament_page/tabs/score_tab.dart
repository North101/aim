import 'package:collection/collection.dart';
import 'package:flutter/material.dart';

import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import '/providers.dart';
import '/utils.dart';
import '/views/data_table_2d.dart';
import '/views/datatable2_fixed_line.dart';
import '/views/error_view.dart';
import '/views/loading_view.dart';
import '/views/rank_text.dart';
import '/views/score_text.dart';
import '/views/utils.dart';

const columnMargin = 18;

final scoreWidthProvider = StreamProvider.autoDispose((ref) async* {
  final negSign = ref.watch(negSignProvider);
  final playerScores = await ref.watch(playerScoreListProvider.future);
  final maxScoreWidth = playerScores
      .map((playerScore) => playerScore.scores)
      .flattened
      .map((score) => scoreSize(score.finalScore, negSign).width);
  final maxTotalWidth = playerScores
      .map((playerScore) => playerScore.total)
      .map((score) => scoreSize(score, negSign).width);
  final maxPenaltyWidth = playerScores
      .map((playerScore) => playerScore.penalty)
      .map((score) => scoreSize(score, negSign).width);

  yield (
    playerScores: playerScores,
    // TOFIX getting a No Element error on tournament-select here at startup sometimes:
    maxRankWidth: playerScores.map((e) => rankSize(e.rank, e.tied).width).max,
    maxNameWidth: playerScores.map((e) => textSize(e.name).width).max,
    maxScoreWidth:
        maxScoreWidth.followedBy(maxTotalWidth).followedBy(maxPenaltyWidth).max,
  );
});

class ScoreTable extends ConsumerWidget {
  const ScoreTable({super.key});

  void onTap(BuildContext context, PlayerId playerId) =>
      Navigator.of(context).pushNamed(ROUTES.player, arguments: playerId);

  @override
  Widget build(context, ref) {
    final selectedPlayerId = ref.watch(selectedPlayerIdProvider);
    final playerScores = ref.watch(scoreWidthProvider);
    return playerScores.when(
      skipLoadingOnReload: true,
      loading: () => const LoadingView(),
      error: (error, stackTrace) => ErrorView(
        error: error,
        stackTrace: stackTrace,
      ),
      data: (playerScores) {
        int? indexSelected;
        if (selectedPlayerId != null) {
          indexSelected = playerScores.playerScores.indexWhere(
                (e) => e.id == selectedPlayerId,
          );
        }
        final int rounds = playerScores.playerScores[0].scores.length;
        return DataTable2FixedLine(
          key: ValueKey(selectedPlayerId),
          minWidth: double.infinity,
          fixedRow: indexSelected,
          columns: [
            DataColumn2(
              label: const Text('#', maxLines: 1),
              numeric: true,
              fixedWidth: playerScores.maxRankWidth + columnMargin,
            ),
            DataColumn2(
              label: const Text('Player', maxLines: 1),
              fixedWidth: playerScores.maxNameWidth + columnMargin,
            ),
            DataColumn2(
              label: const Text('Total', maxLines: 1),
              numeric: true,
              fixedWidth: playerScores.maxScoreWidth + columnMargin,
            ),
            for (int i = rounds - 1; i >= 0; i--)
              DataColumn2(
                label: Text('R${i + 1}', maxLines: 1),
                numeric: true,
                fixedWidth: playerScores.maxScoreWidth + columnMargin,
              ),
            DataColumn2(
              label: const Text('Pen.', maxLines: 1),
              numeric: true,
              fixedWidth: playerScores.maxScoreWidth + columnMargin,
            ),
          ],
          rows: [
            // TODO what if a player doesn't have a score for a particular round?
            for (final score in playerScores.playerScores)
              ScoreRow(
                selected: selectedPlayerId == score.id,
                score: score,
                rounds: rounds,
                onTap: () => onTap(context, score.id),
                decoration: selectedPlayerId == score.id
                    ? BoxDecoration(
                      border: Border.all(
                        color: Colors.green, // Border color
                        width: 2.0,         // Border width
                      ))
                    : null,
              ),
          ],
          columnSpacing: 10,
        );
      },
    );
  }
}

class ScoreRow extends DataRow2 {
  ScoreRow({
    required PlayerScore score,
    required super.onTap,
    required int rounds,
    super.color,
    super.selected,
    super.decoration,
  }) : super(cells: [
          DataCell(RankText(
            rank: score.rank,
            tied: score.tied,
          )),
          DataCell(Text(
            score.name,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          )),
          DataCell(ScoreText(score.total)),
          for (int i = rounds - 1; i >= 0; i--)
            DataCell(
              ScoreText(score.scores[i].finalScore),
              // TODO decide: do we want a user to tap on a single score to go to the whole hanchan score? Maybe in a modal popup?
              // onTap: () => showHanchanModel(score.id, i),
            ),
          DataCell(PenaltyText(score.penalty)),
        ]);
}
