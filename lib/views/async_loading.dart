import 'package:flutter/material.dart';

class AsyncLoadingWidget extends StatelessWidget {
  const AsyncLoadingWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(child: CircularProgressIndicator());
  }
}
