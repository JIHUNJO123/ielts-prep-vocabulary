// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for Japanese (`ja`).
class AppLocalizationsJa extends AppLocalizations {
  AppLocalizationsJa([String locale = 'ja']) : super(locale);

  @override
  String get appTitle => 'IELTS Prep: 必須単語';

  @override
  String get todayWord => '今日の単語';

  @override
  String get learning => '学習';

  @override
  String get levelLearning => 'レベル別学習';

  @override
  String get allWords => '全ての単語';

  @override
  String get viewAllWords => '全ての単語を見る';

  @override
  String get favorites => 'お気に入り';

  @override
  String get savedWords => 'Saved words';

  @override
  String get flashcard => 'フラッシュカード';

  @override
  String get cardLearning => 'Card learning';

  @override
  String get quiz => 'クイズ';

  @override
  String get testYourself => 'Test yourself';

  @override
  String get settings => '設定';

  @override
  String get language => '言語';

  @override
  String get displayLanguage => 'Display Language';

  @override
  String get selectLanguage => 'Select Language';

  @override
  String get display => 'Display';

  @override
  String get darkMode => 'ダークモード';

  @override
  String get fontSize => 'Font Size';

  @override
  String get notifications => '通知';

  @override
  String get dailyReminder => '毎日のリマインダー';

  @override
  String get dailyReminderDesc => 'Get reminded to study every day';

  @override
  String get removeAds => '広告を削除';

  @override
  String get adsRemoved => 'Ads Removed';

  @override
  String get thankYou => 'Thank you for your support!';

  @override
  String get buy => 'Buy';

  @override
  String get restorePurchase => '購入を復元';

  @override
  String get restoring => 'Restoring...';

  @override
  String get purchaseSuccess => 'Purchase successful!';

  @override
  String get loading => '読み込み中...';

  @override
  String get notAvailable => 'Not available';

  @override
  String get info => 'Info';

  @override
  String get version => 'バージョン';

  @override
  String get disclaimer => '免責事項';

  @override
  String get disclaimerText =>
      'このアプリはIELTS試験準備のための独立した学習ツールです。Cambridge Assessment EnglishやBritish Council、または他の公式IELTS組織とは一切関係ありません。すべてのコンテンツは教育目的のみに作成されています。';

  @override
  String get privacyPolicy => 'プライバシーポリシー';

  @override
  String get cannotLoadWords => 'Cannot load words';

  @override
  String get noFavoritesYet => 'No favorites yet';

  @override
  String get tapHeartToSave => 'Tap the heart icon to save words';

  @override
  String get addedToFavorites => 'Added to favorites';

  @override
  String get removedFromFavorites => 'Removed from favorites';

  @override
  String get wordDetail => 'Word Detail';

  @override
  String get definition => '定義';

  @override
  String get example => '例文';

  @override
  String levelWords(String level) {
    return '$level Words';
  }

  @override
  String get band45 => '基礎 (Band 4.5-5.5)';

  @override
  String get band45Desc => '基本語彙 1,200語';

  @override
  String get band60 => '中級 (Band 6.0-6.5)';

  @override
  String get band60Desc => 'アカデミック語彙 1,800語';

  @override
  String get band70 => '上級 (Band 7.0-7.5)';

  @override
  String get band70Desc => '高度な表現 1,200語';

  @override
  String get band80 => '専門家 (Band 8.0+)';

  @override
  String get band80Desc => '専門語彙 800語';

  @override
  String get alphabetical => 'Alphabetical';

  @override
  String get random => 'Random';

  @override
  String get tapToFlip => 'タップして裏返す';

  @override
  String get previous => 'Previous';

  @override
  String get next => 'Next';

  @override
  String get question => 'Question';

  @override
  String get score => 'スコア';

  @override
  String get quizComplete => 'クイズ完了！';

  @override
  String get finish => 'Finish';

  @override
  String get tryAgain => 'もう一度';

  @override
  String get showResult => 'Show Result';

  @override
  String get wordToMeaning => 'Word → Meaning';

  @override
  String get meaningToWord => 'Meaning → Word';

  @override
  String get excellent => 'Excellent! Perfect score!';

  @override
  String get great => 'Great job! Keep it up!';

  @override
  String get good => 'Good effort! Keep practicing!';

  @override
  String get keepPracticing => 'Keep practicing! You\'ll improve!';

  @override
  String get levelA1 => 'Beginner';

  @override
  String get levelA2 => 'Elementary';

  @override
  String get levelB1 => 'Intermediate';

  @override
  String get levelB2 => 'Upper Intermediate';

  @override
  String get levelC1 => 'Advanced';

  @override
  String get privacyPolicyContent =>
      'このアプリは個人情報を収集、保存、共有しません。\n\n学習の進捗とお気に入りはデバイスにのみ保存されます。\n\n外部サーバーへのデータ送信はありません。';

  @override
  String get restorePurchaseDesc =>
      '別のデバイスで広告削除を購入した場合、またはアプリを再インストールした場合は、ここをタップして購入を復元してください。';

  @override
  String get restoreComplete => '復元完了';

  @override
  String get noPurchaseFound => '以前の購入が見つかりません';

  @override
  String get cancel => 'キャンセル';

  @override
  String get selectWordRange => '単語範囲を選択';

  @override
  String get allWordsOption => 'すべての単語';

  @override
  String get favoritesOnlyOption => 'お気に入りのみ';

  @override
  String get byLevel => 'レベル別';

  @override
  String get lockedContent => 'Locked Content';

  @override
  String get watchAdToUnlock =>
      'Watch a short video to unlock all words until midnight!';

  @override
  String get watchAd => 'Watch Ad';

  @override
  String get adNotReady => 'Ad is not ready yet. Please try again.';

  @override
  String get unlockedUntilMidnight => 'All words unlocked until midnight!';
}
