import 'package:collection/collection.dart';
import 'package:data_table_2/data_table_2.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import '/providers.dart';
import '/views/async_error.dart';
import '/views/async_loading.dart';
import '/views/score_text.dart';

const columnSpacing = 16.0;

typedef PlayerRoundScore = ({
  RoundScheduleData round,
  HanchanScore score,
});

typedef PlayerHanchanData = ({
  double nameWidth,
  double placementWidth,
  double scoreWidth,
  List<PlayerRoundScore> hanchanList,
});

final playerGameRoundListProvider = StreamProvider.family
    .autoDispose<List<PlayerRoundScore>, PlayerId>((ref, playerId) async* {
  final gameRoundList = await ref.watch(roundListProvider.future);
  yield [
    for (final gameRound in gameRoundList)
      for (final hanchan in gameRound.tables)
        for (final hanchanScore in hanchan.scores)
          if (hanchanScore.playerId == playerId)
            (
              round: gameRound.round,
              score: hanchanScore,
            ),
  ];
});

final playerHanchanWidthProvider = StreamProvider.family
    .autoDispose<PlayerHanchanData?, PlayerId>((ref, playerId) async* {
  final playerHanchanList =
      await ref.watch(playerGameRoundListProvider(playerId).future);

  if (playerHanchanList.isEmpty) {
    yield null;
    return;
  }

  final negSign = ref.watch(negSignProvider);
  yield (
    nameWidth: playerHanchanList.map((e) => textSize(e.round.name)).max,
    placementWidth:
        playerHanchanList.map((e) => textSize('${e.score.placement}')).max,
    scoreWidth: [
      for (final e in playerHanchanList) scoreSize(e.score.finalScore, negSign),
      for (final e in playerHanchanList) scoreSize(e.score.gameScore, negSign),
      for (final e in playerHanchanList) scoreSize(e.score.uma, negSign),
      for (final e in playerHanchanList) scoreSize(e.score.penalties, negSign),
    ].max,
    hanchanList: playerHanchanList,
  );
});

class PlayerResultsTab extends ConsumerWidget {
  const PlayerResultsTab({
    super.key,
    required this.player,
  });

  final PlayerRankedResults player;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final playerHanchanList =
        ref.watch(playerHanchanWidthProvider(player.player.id));
    return playerHanchanList.when(
      loading: () => const AsyncLoadingWidget(),
      error: (error, stackTrace) => AsyncErrorWidget(error, stackTrace),
      data: (playerHanchanData) {
        if (playerHanchanData == null) {
          return const Center(child: Text('No Hanchans Played'));
        }

        return DataTable2(
          minWidth: double.infinity,
          columnSpacing: columnSpacing,
          columns: [
            DataColumn2(
              label: const Text('Round'),
              fixedWidth: playerHanchanData.nameWidth + columnSpacing,
            ),
            DataColumn2(
              label: const Text('#'),
              numeric: true,
              fixedWidth: playerHanchanData.placementWidth + columnSpacing,
            ),
            DataColumn2(
              label: const Text('Final'),
              numeric: true,
              fixedWidth: playerHanchanData.scoreWidth + columnSpacing,
            ),
            DataColumn2(
              label: const Text('Game'),
              numeric: true,
              fixedWidth: playerHanchanData.scoreWidth + columnSpacing,
            ),
            DataColumn2(
              label: const Text('Uma'),
              numeric: true,
              fixedWidth: playerHanchanData.scoreWidth + columnSpacing,
            ),
            DataColumn2(
              label: const Text('Pen.'),
              numeric: true,
              fixedWidth: playerHanchanData.scoreWidth + columnSpacing,
            ),
          ],
          rows: [
            for (final hanchan in playerHanchanData.hanchanList)
              DataRow2(cells: [
                DataCell(Text(
                  hanchan.round.name,
                  maxLines: 1,
                )),
                DataCell(Text(
                  '${hanchan.score.placement}',
                  maxLines: 1,
                )),
                DataCell(ScoreText(hanchan.score.finalScore)),
                DataCell(ScoreText(hanchan.score.gameScore)),
                DataCell(ScoreText(hanchan.score.uma)),
                DataCell(ScoreText(hanchan.score.penalties)),
              ]),
          ],
        );
      },
    );
  }
}
