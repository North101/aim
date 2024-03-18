import 'package:firebase_messaging/firebase_messaging.dart';

import 'notifications.dart';
import 'utils.dart';

Future<void> setupFCM() async {

  await getFCMToken();

  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
  //subscribeUserToTopic();

  FirebaseMessaging.onMessage.listen((RemoteMessage message) {
  // handle message received when app is in foreground
    notifyWhenFocused(message);
    _handleMessage(message);
  });
}

@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  // TESTED AND WORKS
  Log.debug("Handling a background message: ${message.messageId}");
  Log.debug("Message body: ${message.notification?.body}");
  _handleMessage(message);
}

void subscribeUserToTopic() async {
  // subscribe to topic on each app start-up
  // await messaging.subscribeToTopic('cork2024');
}

void unsubscribeUserToTopic() async {
  // currently not called from anywhere
  await messaging.unsubscribeFromTopic('cork2024');
}

Future<void> getFCMToken() async {
  final String fcmToken = await messaging.getToken() ?? '';

  Log.debug('FCM token: $fcmToken');

  messaging.onTokenRefresh.listen((fcmToken) {
    Log.debug('FCM token refreshed: $fcmToken');
    // Note: This callback is fired at each app startup and whenever a new
    // token is generated.
  }).onError((err) {
    // Error getting token.
  });
}

Future<void> setupInteractedMessage() async {
  // Get any messages which caused the application to open from
  // a terminated state.
  RemoteMessage? initialMessage = await messaging.getInitialMessage();

  if (initialMessage != null) {
    _handleMessage(initialMessage);
  }

  // Also handle any interaction when the app is in the background via a
  // Stream listener
  FirebaseMessaging.onMessageOpenedApp.listen(_handleMessage);
}

void _handleMessage(RemoteMessage message) {
  Log.debug('_handleMessage received a notification');
  Log.debug("Title: ${message.notification?.title}");
  Log.debug("body: ${message.notification?.body}");
  Log.debug("data: ${message.data}");
  // contentAvailable collapseKey category senderId
  // message.data['type'] message.data
}
