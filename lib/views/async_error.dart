import 'package:flutter/material.dart';

class AsyncErrorWidget extends StatelessWidget {
  const AsyncErrorWidget(this.error, this.stackTrace, {super.key});

  final Object error;
  final StackTrace stackTrace;

  @override
  Widget build(BuildContext context) {
    debugPrintStack(stackTrace: stackTrace, label: '$error');
    return Center(
      child: Text(
        '$error',
        style: TextStyle(color: Theme.of(context).colorScheme.error),
      ),
    );
  }
}
