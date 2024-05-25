import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import 'tournament.dart';

final roundTableListProvider =
    StreamProvider<List<RoundTableData>>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('seating')
      .snapshots()
      .map(snapshotData<List<dynamic>>)
      .map((e) => e ?? const [])
      .map((data) => [
            for (final round in data)
              RoundTableData.fromJson((round as Map).cast()),
          ]);
});

final roundTableMapProvider = StreamProvider((ref) async* {
  final roundTableList = await ref.watch(roundTableListProvider.future);
  yield {
    for (final round in roundTableList) round.id: round.tables,
  };
});
