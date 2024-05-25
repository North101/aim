import 'dart:convert';

import 'package:aim_tournaments/providers/firestore.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import 'tournament.dart';

final roundScoreListProvider =
    StreamProvider<List<PlayerScoreData>>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('scores') //
      .snapshots()
      .map((e) => e.data() ?? {})
      .map(
    (data) {
      final roundDone = data.remove('roundDone');
      return [
        for (final MapEntry(:key, :value)
            in jsonDecode(data[roundDone]).entries)
          PlayerScoreData.fromJson({
            'id': int.parse(key),
            ...value,
          })
      ];
    },
  );
});

final playerRankMapProvider = StreamProvider((ref) async* {
  final playerScoreList = await ref.watch(roundScoreListProvider.future);
  yield {
    for (final playerScore in playerScoreList)
      playerScore.id: (
        rank: playerScore.rank,
        tied: playerScore.tied,
      ),
  };
});
