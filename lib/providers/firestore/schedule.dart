import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:timezone/timezone.dart';

import '/models.dart';
import 'tournament.dart';

final scheduleProvider = StreamProvider<ScheduleData>((ref) async* {
  final collection = ref.watch(tournamentCollectionProvider);
  if (collection == null) return;

  yield* collection
      .doc('schedule')
      .snapshots()
      .map(snapshotData<Map<String, dynamic>>)
      .map((data) => data != null
          ? ScheduleData.fromJson(data.cast())
          : ScheduleData(timezone: UTC, rounds: const []));
});

final roundScheduleListProvider = StreamProvider((ref) async* {
  final schedule = await ref.watch(scheduleProvider.future);
  yield schedule.rounds;
});
