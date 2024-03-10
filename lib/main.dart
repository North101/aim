// native imports
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

// third-party imports
import 'package:flutter_redux/flutter_redux.dart';

// app imports
import 'score_table.dart';
import 'store.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle(
    statusBarColor: Colors.black, //top bar color
    statusBarIconBrightness: Brightness.light, //top bar icons
    systemNavigationBarColor: Colors.black, //bottom bar color
    systemNavigationBarIconBrightness: Brightness.light, //bottom bar icons
  ));

  initPrefs().then((_) {
    runApp(MyApp());
  });
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'All-Ireland Mahjong Tournaments',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'All-Ireland Mahjong Tournaments'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return StoreProvider<AllState>(
      // Pass the store to the StoreProvider. Any ancestor `StoreConnector`
      // Widgets will find and use this value as the `Store`.
      store: store,
      child: StoreConnector<AllState, String>(
        converter: (store) => store.state.preferences['backgroundColour'],
        builder: (BuildContext context, String color) {
          return Scaffold( // TODO MaterialApp(
            appBar: AppBar(
              backgroundColor: Theme.of(context).colorScheme.inversePrimary,
              title: Text(widget.title),
            ),
            body: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text(
                    'The next tournament is 10-11 August 2024, in Cork',
                  ),
                  ScoreTable(),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
