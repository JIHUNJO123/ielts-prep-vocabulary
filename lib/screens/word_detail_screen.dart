import 'package:flutter/material.dart';
import 'package:ielts_vocab_app/l10n/generated/app_localizations.dart';
import '../db/database_helper.dart';
import '../models/word.dart';
import '../services/translation_service.dart';

class WordDetailScreen extends StatefulWidget {
  final Word word;

  const WordDetailScreen({super.key, required this.word});

  @override
  State<WordDetailScreen> createState() => _WordDetailScreenState();
}

class _WordDetailScreenState extends State<WordDetailScreen> {
  late Word _word;
  String? _translatedDefinition;
  String? _translatedExample;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _word = widget.word;
    _loadTranslations();
  }

  Future<void> _loadTranslations() async {
    final translationService = TranslationService.instance;
    await translationService.init();
    final langCode = translationService.currentLanguage;

    if (translationService.needsTranslation) {
      // 내장 번역 먼저 확인 (빠른 로딩)
      final embeddedDef = _word.getEmbeddedTranslation(langCode, 'definition');
      final embeddedEx = _word.getEmbeddedTranslation(langCode, 'example');

      String translatedDef;
      String translatedEx;

      if (embeddedDef != null && embeddedDef.isNotEmpty) {
        translatedDef = embeddedDef;
      } else {
        translatedDef = await translationService.translate(
          _word.definition,
          _word.id,
          'definition',
        );
      }

      if (embeddedEx != null && embeddedEx.isNotEmpty) {
        translatedEx = embeddedEx;
      } else {
        translatedEx = await translationService.translate(
          _word.example,
          _word.id,
          'example',
        );
      }

      if (mounted) {
        setState(() {
          _translatedDefinition = translatedDef;
          _translatedExample = translatedEx;
          _isLoading = false;
        });
      }
    } else {
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  Future<void> _toggleFavorite() async {
    await DatabaseHelper.instance.toggleFavorite(_word.id, !_word.isFavorite);
    setState(() {
      _word = _word.copyWith(isFavorite: !_word.isFavorite);
    });

    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            _word.isFavorite
                ? AppLocalizations.of(context)!.addedToFavorites
                : AppLocalizations.of(context)!.removedFromFavorites,
          ),
          duration: const Duration(seconds: 1),
        ),
      );
    }
  }

  Color _getLevelColor(String level) {
    switch (level) {
      case 'Band 5':
        return Colors.green;
      case 'Band 6':
        return Colors.lightGreen;
      case 'Band 7':
        return Colors.orange;
      case 'Band 8+':
        return Colors.red;
      default:
        return Colors.blue;
    }
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    final levelColor = _getLevelColor(_word.level);

    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.wordDetail),
        actions: [
          IconButton(
            icon: Icon(
              _word.isFavorite ? Icons.favorite : Icons.favorite_border,
              color: _word.isFavorite ? Colors.red : null,
            ),
            onPressed: _toggleFavorite,
          ),
        ],
      ),
      body:
          _isLoading
              ? const Center(child: CircularProgressIndicator())
              : SingleChildScrollView(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Header Card
                    Card(
                      elevation: 4,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                      child: Container(
                        width: double.infinity,
                        padding: const EdgeInsets.all(24.0),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(16),
                          gradient: LinearGradient(
                            colors: [
                              levelColor,
                              levelColor.withAlpha((0.7 * 255).toInt()),
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
                                    color: Colors.white.withAlpha(
                                      (0.2 * 255).toInt(),
                                    ),
                                    borderRadius: BorderRadius.circular(20),
                                  ),
                                  child: Text(
                                    _word.partOfSpeech,
                                    style: const TextStyle(
                                      color: Colors.white,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                ),
                                Row(
                                  children: [
                                    Container(
                                      padding: const EdgeInsets.symmetric(
                                        horizontal: 8,
                                        vertical: 4,
                                      ),
                                      decoration: BoxDecoration(
                                        color: Colors.white.withAlpha(
                                          (0.2 * 255).toInt(),
                                        ),
                                        borderRadius: BorderRadius.circular(12),
                                      ),
                                      child: Text(
                                        _word.level,
                                        style: const TextStyle(
                                          color: Colors.white,
                                          fontSize: 12,
                                          fontWeight: FontWeight.bold,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                            const SizedBox(height: 20),
                            Text(
                              _word.word,
                              style: const TextStyle(
                                fontSize: 28,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(height: 24),

                    // Definition Section - 영어 정의(검은색) 위, 번역(회색) 아래
                    _buildSection(
                      title: l10n.definition,
                      icon: Icons.book,
                      content: _word.definition,
                      original: _translatedDefinition,
                    ),
                    const SizedBox(height: 16),

                    // Example Section - 영어 예문(검은색) 위, 번역(회색) 아래
                    _buildSection(
                      title: l10n.example,
                      icon: Icons.format_quote,
                      content: _word.example,
                      original: _translatedExample,
                    ),
                  ],
                ),
              ),
    );
  }

  Widget _buildSection({
    required String title,
    required IconData icon,
    required String content,
    String? original,
  }) {
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon, size: 20, color: Theme.of(context).primaryColor),
                const SizedBox(width: 8),
                Text(
                  title,
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                    color: Theme.of(context).primaryColor,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Text(content, style: const TextStyle(fontSize: 16, height: 1.5)),
            if (original != null) ...[
              const SizedBox(height: 8),
              Text(
                original,
                style: TextStyle(
                  fontSize: 14,
                  color: Colors.grey[600],
                  fontStyle: FontStyle.italic,
                  height: 1.5,
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }
}
