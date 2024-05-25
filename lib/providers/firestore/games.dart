import 'package:collection/collection.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import 'tournament.dart';

final roundGameListProvider = StreamProvider<List<RoundGameData>>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('games') //
      .snapshots()
      .map(snapshotData<List<dynamic>>)
      .map((e) => e ?? const [])
      .map(
        (data) => [
          for (final game in data) RoundGameData.fromJson((game as Map).cast()),
        ].sortedBy<num>((e) => e.roundIndex),
      );
});
