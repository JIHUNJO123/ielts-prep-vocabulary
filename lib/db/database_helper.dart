import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/word.dart';

class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._init();
  static Database? _database;

  DatabaseHelper._init();

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB('ielts_words.db');
    return _database!;
  }

  Future<Database> _initDB(String filePath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filePath);

    return await openDatabase(
      path,
      version: 1,
      onCreate: _createDB,
      onUpgrade: _upgradeDB,
    );
  }

  Future _createDB(Database db, int version) async {
    // 단어 테이블 (영어 원본만)
    await db.execute('''
      CREATE TABLE words (
        id INTEGER PRIMARY KEY,
        word TEXT NOT NULL,
        level TEXT NOT NULL,
        partOfSpeech TEXT NOT NULL,
        definition TEXT NOT NULL,
        example TEXT NOT NULL,
        category TEXT DEFAULT 'General',
        isFavorite INTEGER DEFAULT 0
      )
    ''');

    // 번역 캐시 테이블
    await db.execute('''
      CREATE TABLE translations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        wordId INTEGER NOT NULL,
        languageCode TEXT NOT NULL,
        fieldType TEXT NOT NULL,
        translatedText TEXT NOT NULL,
        createdAt INTEGER NOT NULL,
        UNIQUE(wordId, languageCode, fieldType)
      )
    ''');

    // 인덱스 생성
    await db.execute('''
      CREATE INDEX idx_translations_lookup 
      ON translations(wordId, languageCode, fieldType)
    ''');

    // Load initial data from JSON
    await _loadInitialData(db);
  }

  Future _upgradeDB(Database db, int oldVersion, int newVersion) async {
    if (oldVersion < newVersion) {
      await db.execute('DROP TABLE IF EXISTS words');
      await db.execute('DROP TABLE IF EXISTS translations');
      await _createDB(db, newVersion);
    }
  }

  Future<void> _loadInitialData(Database db) async {
    try {
      final String response = await rootBundle.loadString(
        'assets/data/words.json',
      );
      final List<dynamic> data = json.decode(response);

      for (var wordJson in data) {
        await db.insert('words', {
          'id': wordJson['id'],
          'word': wordJson['word'],
          'level': wordJson['level'],
          'partOfSpeech': wordJson['partOfSpeech'],
          'definition': wordJson['definition'],
          'example': wordJson['example'],
          'category': wordJson['category'] ?? 'General',
          'isFavorite': 0,
        });
      }
      print('Loaded ${data.length} IELTS words successfully');
    } catch (e) {
      print('Error loading initial data: $e');
    }
  }

  // ============ 번역 캐시 메서드 ============

  /// 번역 캐시에서 가져오기
  Future<String?> getTranslation(
    int wordId,
    String languageCode,
    String fieldType,
  ) async {
    final db = await instance.database;
    final result = await db.query(
      'translations',
      columns: ['translatedText'],
      where: 'wordId = ? AND languageCode = ? AND fieldType = ?',
      whereArgs: [wordId, languageCode, fieldType],
    );
    if (result.isNotEmpty) {
      return result.first['translatedText'] as String;
    }
    return null;
  }

  /// 번역 캐시에 저장
  Future<void> saveTranslation(
    int wordId,
    String languageCode,
    String fieldType,
    String translatedText,
  ) async {
    final db = await instance.database;
    await db.insert('translations', {
      'wordId': wordId,
      'languageCode': languageCode,
      'fieldType': fieldType,
      'translatedText': translatedText,
      'createdAt': DateTime.now().millisecondsSinceEpoch,
    }, conflictAlgorithm: ConflictAlgorithm.replace);
  }

  /// 특정 언어의 모든 번역 삭제
  Future<void> clearTranslations(String languageCode) async {
    final db = await instance.database;
    await db.delete(
      'translations',
      where: 'languageCode = ?',
      whereArgs: [languageCode],
    );
  }

  /// 모든 번역 캐시 삭제
  Future<void> clearAllTranslations() async {
    final db = await instance.database;
    await db.delete('translations');
  }

  // ============ 단어 메서드 ============

  Future<List<Word>> getAllWords() async {
    final db = await instance.database;
    final result = await db.query('words', orderBy: 'word ASC');
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<Word>> getWordsByLevel(String level) async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'level = ?',
      whereArgs: [level],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<Word>> getWordsByCategory(String category) async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'category = ?',
      whereArgs: [category],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<String>> getAllCategories() async {
    final db = await instance.database;
    final result = await db.rawQuery(
      'SELECT DISTINCT category FROM words ORDER BY category ASC',
    );
    return result.map((row) => row['category'] as String).toList();
  }

  Future<List<Word>> getFavorites() async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'isFavorite = ?',
      whereArgs: [1],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<List<Word>> searchWords(String query) async {
    final db = await instance.database;
    final result = await db.query(
      'words',
      where: 'word LIKE ? OR definition LIKE ?',
      whereArgs: ['%$query%', '%$query%'],
      orderBy: 'word ASC',
    );
    return result.map((json) => Word.fromDb(json)).toList();
  }

  Future<void> toggleFavorite(int id, bool isFavorite) async {
    final db = await instance.database;
    await db.update(
      'words',
      {'isFavorite': isFavorite ? 1 : 0},
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  Future<Word?> getWordById(int id) async {
    final db = await instance.database;
    final result = await db.query('words', where: 'id = ?', whereArgs: [id]);
    if (result.isEmpty) return null;
    return Word.fromDb(result.first);
  }

  Future<Word?> getRandomWord() async {
    final db = await instance.database;
    final result = await db.rawQuery(
      'SELECT * FROM words ORDER BY RANDOM() LIMIT 1',
    );
    if (result.isEmpty) return null;
    return Word.fromDb(result.first);
  }

  // JSON 데이터 캐시 (내장 번역 포함)
  List<Word>? _jsonWordsCache;

  /// JSON 캐시 클리어 (핫 리로드 시 사용)
  void clearJsonCache() {
    _jsonWordsCache = null;
  }

  /// JSON 파일에서 모든 단어 로드 (내장 번역 포함)
  /// 번역이 있는 파일(band*.json)을 먼저 로드해서 번역 데이터 우선
  Future<List<Word>> _loadWordsFromJson() async {
    // 캐시 무시하고 항상 새로 로드 (디버깅용)
    // if (_jsonWordsCache != null) return _jsonWordsCache!;

    try {
      final List<Word> allWords = [];
      // 번역이 있는 파일을 먼저 로드! (band*.json에 번역 데이터 있음)
      final jsonFiles = [
        'assets/data/band45_words.json',
        'assets/data/band60_words.json',
        'assets/data/band70_words.json',
        'assets/data/band80_words.json',
        'assets/data/words_batch2.json',
        'assets/data/words.json', // 번역 없는 파일은 마지막에
      ];

      for (final file in jsonFiles) {
        try {
          print('Loading JSON file: $file');
          final String response = await rootBundle.loadString(file);
          final List<dynamic> data = json.decode(response);
          final words = data.map((json) => Word.fromJson(json)).toList();
          print('  Loaded ${words.length} words from $file');
          // 첫 번째 단어의 번역 확인
          if (words.isNotEmpty && words.first.translations != null) {
            print(
              '  First word has translations: ${words.first.translations!.keys}',
            );
          }
          allWords.addAll(words);
        } catch (e) {
          print('Error loading $file: $e');
        }
      }

      print('Total JSON words loaded: ${allWords.length}');
      _jsonWordsCache = allWords;
      return allWords;
    } catch (e) {
      print('Error loading JSON words: $e');
      return [];
    }
  }

  /// 단어 찾기 (번역이 있는 단어 우선)
  Word? _findWordWithTranslation(List<Word> jsonWords, Word dbWord) {
    // 같은 단어명으로 매칭되는 모든 단어 찾기
    final matches =
        jsonWords
            .where((w) => w.word.toLowerCase() == dbWord.word.toLowerCase())
            .toList();

    print('=== _findWordWithTranslation ===');
    print('Looking for: ${dbWord.word}');
    print('Found ${matches.length} matches');

    if (matches.isEmpty) return null;

    // 번역이 있는 단어 우선 반환
    for (final word in matches) {
      if (word.translations != null && word.translations!.isNotEmpty) {
        print('Found word with translations: ${word.translations!.keys}');
        return word;
      }
    }

    print('No word with translations found');
    // 번역 없으면 첫 번째 반환
    return matches.first;
  }

  /// 모든 단어 가져오기 (내장 번역 포함) - 퀴즈용
  Future<List<Word>> getWordsWithTranslations() async {
    final db = await instance.database;
    final dbResult = await db.query('words', orderBy: 'word ASC');
    final dbWords = dbResult.map((json) => Word.fromDb(json)).toList();

    // JSON에서 내장 번역 로드
    final jsonWords = await _loadWordsFromJson();

    // DB 단어에 JSON의 번역 데이터 병합 (번역 있는 단어 우선)
    return dbWords.map((dbWord) {
      final jsonWord = _findWordWithTranslation(jsonWords, dbWord) ?? dbWord;
      return dbWord.copyWith(translations: jsonWord.translations);
    }).toList();
  }

  /// 오늘의 단어 (내장 번역 포함)
  Future<Word?> getTodayWord() async {
    try {
      final db = await instance.database;
      // Use date as seed for consistent daily word
      final today = DateTime.now();
      final seed = today.year * 10000 + today.month * 100 + today.day;
      final count =
          Sqflite.firstIntValue(
            await db.rawQuery('SELECT COUNT(*) FROM words'),
          ) ??
          0;

      if (count == 0) {
        print('No words in database');
        return null;
      }

      final index = seed % count;

      final result = await db.rawQuery('SELECT * FROM words LIMIT 1 OFFSET ?', [
        index,
      ]);
      if (result.isEmpty) return null;

      final dbWord = Word.fromDb(result.first);
      print('=== getTodayWord Debug ===');
      print('DB Word: ${dbWord.word}');

      // JSON에서 내장 번역 찾기 (번역 있는 단어 우선)
      final jsonWords = await _loadWordsFromJson();
      print('JSON words loaded: ${jsonWords.length}');

      final jsonWord = _findWordWithTranslation(jsonWords, dbWord);
      print('Found jsonWord: ${jsonWord != null}');
      print('jsonWord translations: ${jsonWord?.translations}');

      final finalWord = jsonWord ?? dbWord;

      // DB의 isFavorite 상태와 JSON의 번역 데이터 병합
      final result2 = dbWord.copyWith(translations: finalWord.translations);
      print('Final word translations: ${result2.translations}');
      return result2;
    } catch (e) {
      print('Error getting today word: $e');
      return null;
    }
  }

  /// 레벨별 단어 수 가져오기
  Future<Map<String, int>> getWordCountByLevel() async {
    final db = await instance.database;
    final result = await db.rawQuery(
      'SELECT level, COUNT(*) as count FROM words GROUP BY level',
    );
    final Map<String, int> counts = {};
    for (var row in result) {
      counts[row['level'] as String] = row['count'] as int;
    }
    return counts;
  }

  /// 단어에 번역 데이터 적용
  Future<Word> applyTranslations(Word word, String languageCode) async {
    if (languageCode == 'en') return word;

    final translatedDef = await getTranslation(
      word.id,
      languageCode,
      'definition',
    );
    final translatedEx = await getTranslation(word.id, languageCode, 'example');

    return word.copyWith(
      translatedDefinition: translatedDef,
      translatedExample: translatedEx,
    );
  }

  /// 여러 단어에 번역 적용
  Future<List<Word>> applyTranslationsToList(
    List<Word> words,
    String languageCode,
  ) async {
    if (languageCode == 'en') return words;

    final result = <Word>[];
    for (final word in words) {
      result.add(await applyTranslations(word, languageCode));
    }
    return result;
  }

  Future close() async {
    final db = await instance.database;
    db.close();
  }
}
