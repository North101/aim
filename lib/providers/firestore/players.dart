import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import '/providers/shared_preferences.dart';
import 'tournament.dart';

final playerListProvider = StreamProvider<List<PlayerData>>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('players')
      .snapshots()
      .map(snapshotData<List<dynamic>>)
      .map((e) => e ?? const {})
      .map((data) => [
            for (final player in data) PlayerData.fromJson(player),
          ]);
});

final playerMapProvider = StreamProvider((ref) async* {
  final playerList = await ref.watch(playerListProvider.future);
  yield {
    for (final player in playerList) player.id: player,
  };
});

final selectedPlayerProvider = Provider((ref) {
  final selectedPlayerId = ref.watch(selectedPlayerIdProvider);
  if (selectedPlayerId == null) return null;

  final playerMap = ref.watch(playerMapProvider).valueOrNull;
  return playerMap?[selectedPlayerId];
});
