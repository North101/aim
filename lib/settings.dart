import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'frame.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  SettingsScreenState createState() => SettingsScreenState();
}

class SettingsScreenState extends State<SettingsScreen> {
  bool _alarmValue = true;
  bool _scoreValue = true;
  bool _seatingValue = true;

  @override
  void initState() {
    super.initState();
    _loadSettings();
  }

  _loadSettings() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    setState(() {
      _alarmValue = (prefs.getBool('alarm') ?? true);
      _scoreValue = (prefs.getBool('score') ?? true);
      _seatingValue = (prefs.getBool('seating') ?? true);
    });
  }

  _saveSettings(String key, bool value) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setBool(key, value);
  }

  @override
  Widget build(BuildContext context) {
    return navFrame(
      context,
      ListView(
        children: <Widget>[
          SwitchListTile(
            title: const Text('Alarms for start of hanchan'),
            value: _alarmValue,
            onChanged: (bool value) {
              setState(() {
                _alarmValue = value;
                _saveSettings('alarm', value);
              });
            },
          ),
          SwitchListTile(
            title: const Text('Notifications for updated scores'),
            value: _scoreValue,
            onChanged: (bool value) {
              setState(() {
                _scoreValue = value;
                _saveSettings('score', value);
              });
            },
          ),
          SwitchListTile(
            title: const Text('Notifications for changes to seating'),
            value: _seatingValue,
            onChanged: (bool value) {
              setState(() {
                _seatingValue = value;
                _saveSettings('seating', value);
              });
            },
          ),
        ],
      ),
    );
  }
}