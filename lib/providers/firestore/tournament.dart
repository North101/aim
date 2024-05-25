import 'dart:convert';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/models.dart';
import '/providers/shared_preferences.dart';

T? snapshotData<T>(DocumentSnapshot<Map<String, dynamic>> snapshot) {
  if (snapshot.data() case {'json': String json}) {
    final data = jsonDecode(json) as T;
    return data;
  }
  return null;
}

final firebaseProvider = Provider((ref) => FirebaseFirestore.instance);

final tournamentListProvider = StreamProvider((ref) {
  final db = ref.watch(firebaseProvider);
  final snapshots = switch (kDebugMode) {
    true => db.collection('tournaments').snapshots(),
    false => db
        .collection('tournaments')
        .where('status', isEqualTo: 'live')
        .snapshots(),
  };

  return snapshots.map((query) => [
        for (final doc in query.docs)
          TournamentData.fromJson({
            'id': doc.id,
            'address': '',
            ...(doc.data() as Map).cast(),
          }),
      ]);
});

final tournamentProvider = StreamProvider<TournamentData>((ref) async* {
  final db = ref.watch(firebaseProvider);
  final tournamentId = ref.watch(tournamentIdProvider);
  if (tournamentId == null) return;

  yield* db
      .collection('tournaments')
      .doc(tournamentId)
      .snapshots()
      .map((snapshot) => TournamentData.fromJson({
            'id': snapshot.id,
            'address': '',
            ...(snapshot.data() as Map).cast(),
          }));
});

final tournamentCollectionProvider = Provider((ref) {
  final db = ref.watch(firebaseProvider);
  final tournamentId = ref.watch(tournamentIdProvider);
  if (tournamentId == null) return null;

  return db.collection('tournaments').doc(tournamentId).collection('json');
});
