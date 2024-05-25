import '/views/rank_text.dart';
import 'package:collection/collection.dart';
import 'package:data_table_2/data_table_2.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import '/providers.dart';
import '/utils.dart';
import '/views/async_error.dart';
import '/views/async_loading.dart';
import '/views/score_text.dart';

const columnSpacing = 16.0;

final scoreWidthProvider = StreamProvider.autoDispose((ref) async* {
  final playerScores = await ref.watch(playerScoreListProvider.future);
  if (playerScores.isEmpty) {
    yield null;
    return;
  }

  final negSign = ref.watch(negSignProvider);
  final maxRankWidth = playerScores
      .map((playerScore) => rankSize(playerScore.rank, playerScore.tied))
      .max;
  final maxNameWidth = playerScores
      .map((playerScore) => playerScore.player.name)
      .map((name) => textSize(name))
      .max;

  yield (
    playerScores: playerScores,
    maxRankWidth: maxRankWidth,
    maxNameWidth: maxNameWidth,
    maxScoreWidth: [
      for (final playerScore in playerScores)
        for (final score in playerScore.scores)
          scoreSize(score.score.finalScore, negSign),
      for (final playerScore in playerScores)
        scoreSize(playerScore.finalScore, negSign),
      for (final playerScore in playerScores)
        scoreSize(playerScore.penalites, negSign),
    ].max,
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
      loading: () => const AsyncLoadingWidget(),
      error: (error, stackTrace) => AsyncErrorWidget(error, stackTrace),
      data: (playerScores) {
        if (playerScores == null) {
          return const Center(child: Text(''));
        }

        final rounds =
            playerScores.playerScores.map((e) => e.scores.length).max;
        final selectedScore = playerScores.playerScores.firstWhereOrNull(
          (e) => e.player.id == selectedPlayerId,
        );
        return DataTable2(
          minWidth: double.infinity,
          fixedTopRows: selectedPlayerId != null ? 2 : 1,
          columnSpacing: columnSpacing,
          columns: [
            DataColumn2(
              label: const Text('#', maxLines: 1),
              numeric: true,
              fixedWidth: playerScores.maxRankWidth + columnSpacing,
            ),
            DataColumn2(
              label: const Text('Player', maxLines: 1),
              fixedWidth: playerScores.maxNameWidth + columnSpacing,
            ),
            DataColumn2(
              label: const Text('Total', maxLines: 1),
              numeric: true,
              fixedWidth: playerScores.maxScoreWidth + columnSpacing,
            ),
            for (int i = rounds - 1; i >= 0; i--)
              DataColumn2(
                label: Text('R${i + 1}', maxLines: 1),
                numeric: true,
                fixedWidth: playerScores.maxScoreWidth + columnSpacing,
              ),
            DataColumn2(
              label: const Text('Pen.', maxLines: 1),
              numeric: true,
              fixedWidth: playerScores.maxScoreWidth + columnSpacing,
            ),
          ],
          rows: [
            if (selectedScore case PlayerRankedResults score)
              ScoreRow(
                selected: true,
                score: score,
                rounds: rounds,
                onTap: () => onTap(context, selectedScore.player.id),
                color: WidgetStateProperty.all<Color>(selectedHighlight),
              ),
            for (final score in playerScores.playerScores)
              ScoreRow(
                selected: selectedPlayerId == score.player.id,
                score: score,
                rounds: rounds,
                onTap: () => onTap(context, score.player.id),
                color: selectedPlayerId == score.player.id
                    ? WidgetStateProperty.all<Color>(selectedHighlight)
                    : null,
              ),
          ],
        );
      },
    );
  }
}

class ScoreRow extends DataRow2 {
  ScoreRow({
    required PlayerRankedResults score,
    required int rounds,
    required super.onTap,
    super.color,
    super.selected,
  }) : super(cells: [
          DataCell(RankText(rank: score.rank, tied: score.tied)),
          DataCell(Text(
            score.player.name,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          )),
          DataCell(ScoreText(score.finalScore)),
          for (int i = rounds - 1; i >= 0; i--)
            DataCell(
              ScoreText(score.scores.elementAtOrNull(i)?.score.finalScore ?? 0),
            ),
          DataCell(ScoreText(score.penalites)),
        ]);
}
