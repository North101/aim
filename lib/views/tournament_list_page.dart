import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '/providers.dart';
import '/utils.dart';
import 'async_error.dart';
import 'async_loading.dart';

class TournamentListPage extends StatelessWidget {
  const TournamentListPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Tournaments'),
      ),
      body: const TournamentList(),
    );
  }
}

class TournamentList extends ConsumerWidget {
  const TournamentList({super.key});
  @override
  Widget build(context, ref) {
    final tournamentId = ref.watch(tournamentIdProvider);
    final tournamentList = ref.watch(tournamentListProvider);
    return tournamentList.when(
      skipLoadingOnReload: true,
      loading: () => const AsyncLoadingWidget(),
      error: (error, stackTrace) => AsyncErrorWidget(error, stackTrace),
      data: (tournamentList) {
        if (tournamentList.isEmpty) {
          return const Center(child: Text('No Tournaments Found'));
        }

        return ListView(
          padding: const EdgeInsets.all(8),
          children: [
            for (final tournament in tournamentList)
              Card(
                child: ListTile(
                  selected: tournamentId == tournament.id,
                  title: Text(tournament.name),
                  subtitle: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(tournament.when),
                      Text(tournament.country),
                    ],
                  ),
                  onTap: () async {
                    await ref
                        .read(tournamentIdProvider.notifier) //
                        .set(tournament.id);

                    if (!context.mounted) return;
                    Navigator.of(context).pushNamed(ROUTES.tournament);
                  },
                ),
              ),
          ],
        );
      },
    );
  }
}
