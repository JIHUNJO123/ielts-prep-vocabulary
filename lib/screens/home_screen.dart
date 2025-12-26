import 'package:flutter/material.dart';
import 'package:ielts_vocab_app/l10n/generated/app_localizations.dart';
import '../db/database_helper.dart';
import '../models/word.dart';
import '../services/translation_service.dart';
import '../services/ad_service.dart';
import 'word_list_screen.dart';
import 'word_detail_screen.dart';
import 'favorites_screen.dart';
import 'quiz_screen.dart';
import 'settings_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Word? _todayWord;
  String? _translatedDefinition;
  bool _isLoading = true;
  String? _lastLanguage;

  @override
  void initState() {
    super.initState();
    _loadTodayWord();
    AdService.instance.loadRewardedAd();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final currentLanguage = TranslationService.instance.currentLanguage;
    if (_lastLanguage != null && _lastLanguage != currentLanguage) {
      _loadTodayWord();
    }
    _lastLanguage = currentLanguage;
  }

  Future<void> _loadTodayWord() async {
    try {
      final word = await DatabaseHelper.instance.getTodayWord();
      if (word != null) {
        final translationService = TranslationService.instance;
        await translationService.init();

        if (translationService.needsTranslation) {
          // 내장 번역만 사용 (API 호출 없음)
          final embeddedTranslation = word.getEmbeddedTranslation(
            translationService.currentLanguage,
            'definition',
          );

          if (mounted) {
            setState(() {
              _todayWord = word;
              _translatedDefinition = embeddedTranslation;
              _isLoading = false;
            });
          }
        } else {
          if (mounted) {
            setState(() {
              _todayWord = word;
              _translatedDefinition = null;
              _isLoading = false;
            });
          }
        }
      } else {
        if (mounted) {
          setState(() {
            _todayWord = null;
            _isLoading = false;
          });
        }
      }
    } catch (e) {
      print('Error loading today word: $e');
      if (mounted) {
        setState(() {
          _todayWord = null;
          _isLoading = false;
        });
      }
    }
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;

    return Scaffold(
      appBar: AppBar(
        title: Text(
          l10n.appTitle,
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
        centerTitle: true,
        elevation: 0,
        actions: [
          IconButton(
            icon: const Icon(Icons.settings),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const SettingsScreen()),
              );
            },
          ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Today's Word Card
                  _buildTodayWordCard(),
                  const SizedBox(height: 24),

                  // Quick Actions
                  Text(
                    l10n.learning,
                    style: const TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 12),
                  _buildMenuGrid(),

                  const SizedBox(height: 24),

                  // Band Level Selection
                  Text(
                    l10n.levelLearning,
                    style: const TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 12),
                  _buildBandLevelCards(),
                ],
              ),
            ),
          ),
          // 배너 광고
          _buildBannerAd(),
        ],
      ),
    );
  }

  Widget _buildBannerAd() {
    // 배너 광고 제거됨 - 보상형 광고만 사용
    return const SizedBox.shrink();
  }

  Widget _buildTodayWordCard() {
    final l10n = AppLocalizations.of(context)!;

    if (_isLoading) {
      return const Card(
        child: Padding(
          padding: EdgeInsets.all(24.0),
          child: Center(child: CircularProgressIndicator()),
        ),
      );
    }

    if (_todayWord == null) {
      return Card(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Center(child: Text(l10n.cannotLoadWords)),
        ),
      );
    }

    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: InkWell(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => WordDetailScreen(word: _todayWord!),
            ),
          );
        },
        borderRadius: BorderRadius.circular(16),
        child: Container(
          width: double.infinity,
          padding: const EdgeInsets.all(24.0),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(16),
            gradient: LinearGradient(
              colors: [
                Theme.of(context).primaryColor,
                Theme.of(context).primaryColor.withAlpha((0.7 * 255).toInt()),
              ],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 12,
                      vertical: 6,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.white.withAlpha((0.2 * 255).toInt()),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      "📅 ${l10n.todayWord}",
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 8,
                      vertical: 4,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.white.withAlpha((0.2 * 255).toInt()),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text(
                      _todayWord!.level,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 20),
              Row(
                children: [
                  Expanded(
                    child: Text(
                      _todayWord!.word,
                      style: const TextStyle(
                        fontSize: 28,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              Text(
                _translatedDefinition ?? _todayWord!.definition,
                style: const TextStyle(fontSize: 16, color: Colors.white),
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildMenuGrid() {
    final l10n = AppLocalizations.of(context)!;

    return GridView.count(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      crossAxisCount: 2,
      mainAxisSpacing: 12,
      crossAxisSpacing: 12,
      childAspectRatio: 1.3,
      children: [
        _buildMenuCard(
          icon: Icons.list_alt,
          title: l10n.allWords,
          subtitle: l10n.viewAllWords,
          color: Colors.blue,
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const WordListScreen()),
            );
          },
        ),
        _buildMenuCard(
          icon: Icons.favorite,
          title: l10n.favorites,
          subtitle: l10n.savedWords,
          color: Colors.red,
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const FavoritesScreen()),
            );
          },
        ),
        _buildMenuCard(
          icon: Icons.style,
          title: l10n.flashcard,
          subtitle: l10n.cardLearning,
          color: Colors.orange,
          onTap: () => _showLevelSelectionDialog(isQuiz: false),
        ),
        _buildMenuCard(
          icon: Icons.quiz,
          title: l10n.quiz,
          subtitle: l10n.testYourself,
          color: Colors.green,
          onTap: () => _showLevelSelectionDialog(isQuiz: true),
        ),
      ],
    );
  }

  void _showLevelSelectionDialog({required bool isQuiz}) {
    final l10n = AppLocalizations.of(context)!;

    // IELTS Band levels
    final levels = [
      {'level': 'Band 4.5-5.5', 'name': l10n.band45, 'color': Colors.green},
      {'level': 'Band 6.0-6.5', 'name': l10n.band60, 'color': Colors.blue},
      {'level': 'Band 7.0-7.5', 'name': l10n.band70, 'color': Colors.orange},
      {'level': 'Band 8.0+', 'name': l10n.band80, 'color': Colors.red},
    ];

    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(l10n.selectWordRange),
        content: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // All Words option
              ListTile(
                leading: const Icon(Icons.all_inclusive, color: Colors.purple),
                title: Text(l10n.allWordsOption),
                onTap: () {
                  Navigator.pop(context);
                  if (isQuiz) {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const QuizScreen(),
                      ),
                    );
                  } else {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) =>
                            const WordListScreen(isFlashcardMode: true),
                      ),
                    );
                  }
                },
              ),
              // Favorites Only option
              ListTile(
                leading: const Icon(Icons.favorite, color: Colors.red),
                title: Text(l10n.favoritesOnlyOption),
                onTap: () {
                  Navigator.pop(context);
                  if (isQuiz) {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) =>
                            const QuizScreen(favoritesOnly: true),
                      ),
                    );
                  } else {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const WordListScreen(
                          isFlashcardMode: true,
                          favoritesOnly: true,
                        ),
                      ),
                    );
                  }
                },
              ),
              const Divider(),
              // By Level header
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 8.0),
                child: Text(
                  l10n.byLevel,
                  style: const TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Colors.grey,
                  ),
                ),
              ),
              // Level options
              ...levels.map((levelData) => ListTile(
                    leading:
                        Icon(Icons.school, color: levelData['color'] as Color),
                    title: Text(levelData['name'] as String),
                    onTap: () {
                      Navigator.pop(context);
                      if (isQuiz) {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) =>
                                QuizScreen(level: levelData['level'] as String),
                          ),
                        );
                      } else {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => WordListScreen(
                              isFlashcardMode: true,
                              level: levelData['level'] as String,
                            ),
                          ),
                        );
                      }
                    },
                  )),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text(l10n.cancel),
          ),
        ],
      ),
    );
  }

  Widget _buildMenuCard({
    required IconData icon,
    required String title,
    required String subtitle,
    required Color color,
    required VoidCallback onTap,
  }) {
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12.0, vertical: 10.0),
          child: Row(
            children: [
              Icon(icon, size: 36, color: color),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      title,
                      style: const TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 14,
                      ),
                      overflow: TextOverflow.ellipsis,
                    ),
                    const SizedBox(height: 2),
                    Text(
                      subtitle,
                      style: TextStyle(color: Colors.grey[600], fontSize: 11),
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildBandLevelCards() {
    final l10n = AppLocalizations.of(context)!;

    // IELTS Band 기준 레벨 (새 체계)
    final levels = [
      {
        'level': 'Band 4.5-5.5',
        'name': l10n.band45,
        'desc': l10n.band45Desc,
        'color': Colors.green,
      },
      {
        'level': 'Band 6.0-6.5',
        'name': l10n.band60,
        'desc': l10n.band60Desc,
        'color': Colors.blue,
      },
      {
        'level': 'Band 7.0-7.5',
        'name': l10n.band70,
        'desc': l10n.band70Desc,
        'color': Colors.orange,
      },
      {
        'level': 'Band 8.0+',
        'name': l10n.band80,
        'desc': l10n.band80Desc,
        'color': Colors.red,
      },
    ];

    return SizedBox(
      height: 120,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: levels.length,
        itemBuilder: (context, index) {
          final level = levels[index];
          return Container(
            width: 140,
            margin: const EdgeInsets.only(right: 10),
            child: Card(
              elevation: 2,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
              ),
              child: InkWell(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) =>
                          WordListScreen(level: level['level'] as String),
                    ),
                  );
                },
                borderRadius: BorderRadius.circular(12),
                child: Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(12),
                    gradient: LinearGradient(
                      colors: [
                        (level['color'] as Color).withAlpha(
                          (0.8 * 255).toInt(),
                        ),
                        (level['color'] as Color),
                      ],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 8.0,
                      vertical: 10.0,
                    ),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          level['level'] as String,
                          style: const TextStyle(
                            fontSize: 14,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          level['desc'] as String,
                          style: const TextStyle(
                            fontSize: 9,
                            color: Colors.white70,
                          ),
                          textAlign: TextAlign.center,
                          maxLines: 2,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}
