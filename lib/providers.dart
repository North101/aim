import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:timezone/timezone.dart';

import 'providers/firestore.dart';
import 'providers/location.dart';

export 'providers/alarm.dart';
export 'providers/fcm.dart';
export 'providers/firestore.dart';
export 'providers/location.dart';
export 'providers/shared_preferences.dart';

final alarmScheduleProvider = StreamProvider((ref) async* {
  final location = await ref.watch(locationProvider.future);
  final roundTableMap = await ref.watch(roundTableMapProvider.future);
  final roundList = await ref.watch(roundScheduleListProvider.future);
  final selectedPlayer = ref.watch(selectedPlayerProvider);

  yield roundList.map((round) {
    final tables = roundTableMap[round.id]!;
    return (
      id: round.id,
      name: round.name,
      alarm: TZDateTime.from(
        round.start,
        location,
      ).subtract(const Duration(minutes: 5)),
      player: selectedPlayer != null
          ? (
              id: selectedPlayer.id,
              name: selectedPlayer.name,
              table: tables.entries
                  .firstWhere((e) => e.value.contains(selectedPlayer.id))
                  .key,
            )
          : null,
    );
  }).toList();
});

extension SelectAsyncValue<State> on StreamProvider<State> {
  ProviderListenable<AsyncValue<Selected>> selectAsyncData<Selected>(
    Selected Function(State value) selector,
  ) {
    return select((e) => e.whenData(selector));
  }
}

void asyncDataListener<T>(
  void Function(T? previous, T next) listener,
  AsyncValue<T>? previous,
  AsyncValue<T> next,
) async {
  if (!next.hasValue) return;

  final previousValue = previous?.valueOrNull;
  final nextValue = next.value;
  if (identical(previousValue, nextValue)) return;

  if (nextValue case T nextValue) {
    return listener(previousValue, nextValue);
  }
}

extension WidgetRefListen on WidgetRef {
  void listenAsyncData<T>(
    ProviderListenable<AsyncValue<T>> provider,
    void Function(T? previous, T next) listener, {
    void Function(Object error, StackTrace stackTrace)? onError,
  }) =>
      listen(
        provider,
        (previous, next) => asyncDataListener(listener, previous, next),
        onError: onError,
      );
}

extension RefListen on Ref {
  ProviderSubscription<AsyncValue<T>> listenAsyncData<T>(
    AlwaysAliveProviderListenable<AsyncValue<T>> provider,
    void Function(T? previous, T next) listener, {
    void Function(Object error, StackTrace stackTrace)? onError,
    bool fireImmediately = false,
  }) =>
      listen(
        provider,
        (previous, next) => asyncDataListener(listener, previous, next),
        onError: onError,
        fireImmediately: fireImmediately,
      );
}

extension AutoDisposeRefListen on AutoDisposeRef {
  ProviderSubscription<AsyncValue<T>> listenAsyncData<T>(
    ProviderListenable<AsyncValue<T>> provider,
    void Function(T? previous, T next) listener, {
    void Function(Object error, StackTrace stackTrace)? onError,
    bool fireImmediately = false,
  }) =>
      listen(
        provider,
        (previous, next) => asyncDataListener(listener, previous, next),
        onError: onError,
        fireImmediately: fireImmediately,
      );
}
