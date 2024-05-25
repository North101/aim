import 'package:collection/collection.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/providers.dart';
import '/views/rank_text.dart';
import '/views/score_text.dart';

class PlayerStatsTab extends ConsumerWidget {
  const PlayerStatsTab({
    super.key,
    required this.player,
  });

  final PlayerRankedResults player;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final scores = player.scores.map((e) => e.score);
    return ListView(children: [
      ListTile(
        title: const Text('Rank'),
        trailing: RankText(
          rank: player.rank,
          tied: player.tied,
          style: Theme.of(context).textTheme.titleSmall,
        ),
      ),
      ListTile(
        title: const Text('Current Overall Score'),
        trailing: ScoreText(
          player.finalScore,
          style: Theme.of(context).textTheme.titleSmall,
        ),
      ),
      ListTile(
        title: const Text('Penalty'),
        trailing: ScoreText(
          player.penalites,
          style: Theme.of(context).textTheme.titleSmall,
        ),
      ),
      ListTile(
        title: const Text('Average Score'),
        trailing: ScoreText(
          scores.map((e) => e.finalScore).average,
          style: Theme.of(context).textTheme.titleSmall,
        ),
      ),
      ListTile(
        title: const Text('Highest Score'),
        trailing: ScoreText(
          scores.map((e) => e.finalScore).max,
          style: Theme.of(context).textTheme.titleSmall,
        ),
      ),
      ListTile(
        title: const Text('Lowest Score'),
        trailing: ScoreText(
          scores.map((e) => e.finalScore).min,
          style: Theme.of(context).textTheme.titleSmall,
        ),
      ),
    ]);
  }
}
