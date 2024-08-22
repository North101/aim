import 'package:collection/collection.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_sticky_header/flutter_sticky_header.dart';
import 'package:intl/intl.dart';
import 'package:timezone/timezone.dart' as tz;

import '/models.dart';
import '/providers.dart';
import '/utils.dart';
import '/views/utils.dart';
import '/views/error_view.dart';
import 'loading_view.dart';

typedef Round = ({
  String id,
  String name,
  tz.TZDateTime start,
  List<RoundTable> tables,
});

typedef RoundTable = ({
  String name,
  Map<Wind, PlayerData> players,
});

final showAllProvider = StateProvider((ref) => false);

final filterByPlayerIdProvider = Provider((ref) {
  return ref.watch(selectedPlayerIdProvider);
});

final filterByPlayerProvider = Provider((ref) {
  final playerId = ref.watch(filterByPlayerIdProvider);
  final playerList = ref.watch(playerListProvider);
  return playerList.value?.firstWhereOrNull((e) => e.id == playerId);
}, dependencies: [
  filterByPlayerIdProvider,
  playerListProvider,
]);

final roundListProvider = StreamProvider((ref) async* {
  final showAll = ref.watch(showAllProvider);
  final filterByPlayer = ref.watch(filterByPlayerProvider);
  final roundMap = await ref.watch(roundMapProvider.future);
  final playerMap = await ref.watch(playerMapProvider.future);

  final roundList = await ref.watch(seatingProvider.future);
  yield roundList
      .map(
        (round) => (
          id: round.id,
          name: roundMap[round.id]!.name,
          start: roundMap[round.id]!.start,
          tables: [
            for (final table in round.tables)
              if (showAll ||
                  filterByPlayer == null ||
                  table.players.contains(filterByPlayer.id))
                (
                  name: table.name,
                  players: {
                    for (final wind in Wind.values)
                      wind: playerMap[table.players[wind.index]]!,
                  },
                )
          ],
        ),
      )
      .sortedBy<DateTime>((round) => round.start.toLocal());
}, dependencies: [
  showAllProvider,
  filterByPlayerProvider,
]);

enum When {
  all,
  upcoming,
  past,
}

final orderedRoundList =
    StreamProvider.family<Iterable<Round>, When>((ref, when) async* {
  final roundList = await ref.watch(roundListProvider.future);
  yield switch (when) {
    When.all => roundList.cast<Round>(),
    When.upcoming => roundList.cast<Round>(),
    When.past => roundList.reversed.cast<Round>(),
  };
}, dependencies: [
  roundListProvider,
]);

bool isRoundOver(round, tz.TZDateTime now, int endRound) {
  return now.isAfter(round.start.add(const Duration(minutes: 45)))
        || (round.id is int ? round.id : int.parse(round.id)) <= endRound;
}

final filteredRoundList = StreamProvider.family<Iterable<Round>, When>(
  (ref, when) async* {

    final rankingList = await ref.watch(allRankingsProvider.future);
    final int endRound = (rankingList.containsKey('roundDone'))
       ? int.parse(rankingList['roundDone'])
       : 0;

    final roundList = await ref.watch(orderedRoundList(when).future);
    tz.TZDateTime? now;
    yield roundList.where((round) {
      now ??= tz.TZDateTime.now(round.start.location);
      return switch (when) {
        When.all => true,
        When.upcoming => !isRoundOver(round, now!, endRound),
        When.past => isRoundOver(round, now!, endRound),
      };
    });
  },
  dependencies: [
    orderedRoundList,
  ],
);

class ScheduleList extends ConsumerWidget {
  const ScheduleList({
    required this.when,
    super.key,
  });

  final When when;

  @override
  Widget build(context, ref) {
    final roundList = ref.watch(filteredRoundList(when));
    final useEventTimezone = ref.watch(timezonePrefProvider);
    final localTimeZoneAsync = ref.watch(localLocationProvider);

    return roundList.when(
      skipLoadingOnReload: true,
      loading: () => const LoadingView(),
      error: (error, stackTrace) => ErrorView(
        error: error,
        stackTrace: stackTrace,
      ),
      data: (roundList) {
        if (roundList.isEmpty) {
          return const Center(child: Text('No seating schedule available'));
        }
        return localTimeZoneAsync.when(
          loading: () => const LoadingView(),
          error: (error, stackTrace) => ErrorView(
            error: error,
            stackTrace: stackTrace,
          ),
          data: (localTimeZone) {
            return CustomScrollView(
              slivers: [
                for (final round in roundList)
                  SliverStickyHeader(
                    header: Material(
                      color: Theme.of(context).colorScheme.primaryContainer,
                      elevation: 1,
                      child: ListTile(
                        leading: const Icon(Icons.watch_later_outlined),
                        title: Text(round.name),
                        subtitle: useEventTimezone
                            ? Text(
                                '${DateFormat('EEEE d MMMM').format(round.start)}\n'
                                '${formatTimeWithDifference(round.start, localTimeZone)}'
                              )
                            : Text(
                                '${DateFormat('HH:mm').format(tz.TZDateTime.from(
                                    round.start, localTimeZone))}'
                                ' (phone time)',
                              ),
                        visualDensity: VisualDensity.compact,
                        onTap: () => Navigator.of(context).pushNamed(
                          ROUTES.round,
                          arguments: round.id,
                        ),
                      ),
                    ),
                    sliver: SliverPadding(
                      padding: const EdgeInsets.only(bottom: 16),
                      sliver: SliverList(
                        delegate: SliverChildListDelegate([
                          for (final table in round.tables)
                            Column(children: [
                              ListTile(
                                leading: const Icon(Icons.table_restaurant),
                                title: Text(table.name),
                              ),
                              Padding(
                                padding: const EdgeInsets.symmetric(horizontal: 8),
                                child: AssignedTable(players: table.players),
                              ),
                            ]),
                        ]),
                      ),
                    ),
                  ),
              ],
            );
          },
        );
      },
    );
  }
}

class AssignedTable extends ConsumerWidget {
  const AssignedTable({
    required this.players,
    super.key,
  });

  final Map<Wind, PlayerData> players;

  void onTap(BuildContext context, PlayerId playerId) =>
      Navigator.of(context).pushNamed(ROUTES.player, arguments: playerId);

  @override
  Widget build(context, ref) {
    final filterByPlayerId = ref.watch(filterByPlayerIdProvider);
    final japaneseWinds = ref.watch(japaneseWindsProvider);
    final playerWinds = Wind.values.map(
      (wind) => (wind: wind, player: players[wind]),
    );
    return Table(
      border: TableBorder.all(
        width: 2,
        color: const Color(0x88888888),
      ),
      columnWidths: const {
        0: IntrinsicColumnWidth(),
        1: FlexColumnWidth(),
      },
      children: [
        for (final (:wind, :player) in playerWinds)
          TableRow(
            decoration: BoxDecoration(
              color: player?.id == filterByPlayerId
                  ? selectedHighlight
                  : Colors.transparent,
            ),
            children: [
              Padding(
                padding: const EdgeInsets.all(8),
                child: Text(
                  switch (japaneseWinds) {
                    true => wind.japanese,
                    false => wind.western,
                  },
                  textAlign: TextAlign.center,
                ),
              ),
              InkWell(
                onTap: player != null ? () => onTap(context, player.id) : null,
                child: Padding(
                  padding: const EdgeInsets.all(8),
                  child: Text(player?.name ?? ''),
                ),
              ),
            ],
          ),
      ],
    );
  }
}