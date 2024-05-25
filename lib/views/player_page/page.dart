import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import '/providers.dart';
import 'tabs/results_tab.dart';
import 'tabs/schedule_tab.dart';
import 'tabs/stats_tab.dart';

final playerScoreProvider = StreamProvider.family
    .autoDispose<PlayerRankedResults, PlayerId>((ref, playerId) async* {
  final playerScoreList = await ref.watch(playerScoreListProvider.future);
  yield playerScoreList.firstWhere((e) => e.player.id == playerId);
});

class PlayerPage extends ConsumerWidget {
  const PlayerPage({
    super.key,
  });

  PlayerId playerId(BuildContext context) {
    return ModalRoute.of(context)?.settings.arguments as PlayerId;
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final player = ref.watch(playerScoreProvider(playerId(context)));
    final isSelected = ref.watch(
      selectedPlayerIdProvider.select((id) => id == playerId(context)),
    );
    return player.when(
      skipLoadingOnReload: true,
      loading: () => Scaffold(
        appBar: AppBar(
          backgroundColor: Theme.of(context).colorScheme.inversePrimary,
          title: const Text('Player'),
        ),
        body: const Center(child: CircularProgressIndicator()),
      ),
      error: (error, stackTrace) => Scaffold(
        appBar: AppBar(
          backgroundColor: Theme.of(context).colorScheme.inversePrimary,
          title: const Text('Player'),
        ),
        body: Center(child: Text('$error')),
      ),
      data: (player) => DefaultTabController(
        length: 3,
        child: Scaffold(
          appBar: AppBar(
            backgroundColor: Theme.of(context).colorScheme.inversePrimary,
            title: Text(player.player.name),
            actions: [
              IconButton(
                onPressed: () {
                  final selectedPlayerIdNotifier =
                      ref.read(selectedPlayerIdProvider.notifier);
                  if (isSelected) {
                    selectedPlayerIdNotifier.set(null);
                  } else {
                    selectedPlayerIdNotifier.set(player.player.id);
                  }
                },
                icon: isSelected
                    ? const Icon(Icons.favorite)
                    : const Icon(Icons.favorite_border),
              ),
            ],
            bottom: const TabBar(tabs: [
              Tab(text: 'Stats'),
              Tab(text: 'Schedule'),
              Tab(text: 'Results'),
            ]),
          ),
          body: TabBarView(children: [
            PlayerStatsTab(player: player),
            PlayerScheduleTab(player: player),
            PlayerResultsTab(player: player),
          ]),
        ),
      ),
    );
  }
}
