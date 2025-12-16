import json
import os
import time
from deep_translator import GoogleTranslator

LANGUAGES = {
    'ko': 'ko',
    'ja': 'ja',
    'zh': 'zh-CN',
    'es': 'es',
    'de': 'de',
    'fr': 'fr',
    'pt': 'pt',
    'vi': 'vi',
    'ar': 'ar',
}

def translate_text(text, target_lang):
    if not text or text.strip() == '':
        return ''
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        result = translator.translate(text)
        return result if result else ''
    except Exception as e:
        return ''

def translate_file(filename):
    filepath = f'assets/data/{filename}'
    print(f"\n{'='*60}")
    print(f"Processing: {filename}")
    print(f"{'='*60}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        words = json.load(f)
    
    total = len(words)
    translated_count = 0
    
    for i, word in enumerate(words):
        # Ensure translations field exists
        if 'translations' not in word:
            word['translations'] = {}
            for lang in LANGUAGES:
                word['translations'][lang] = {"definition": "", "example": ""}
        
        # Check if already translated
        ko_def = word.get('translations', {}).get('ko', {}).get('definition', '')
        if ko_def:
            continue
        
        translated_count += 1
        print(f"[{i+1}/{total}] {word['word']}: ", end='')
        
        definition = word.get('definition', '')
        example = word.get('example', '')
        
        for lang_key, lang_code in LANGUAGES.items():
            try:
                def_trans = translate_text(definition, lang_code)
                ex_trans = translate_text(example, lang_code)
                
                if lang_key not in word['translations']:
                    word['translations'][lang_key] = {"definition": "", "example": ""}
                
                word['translations'][lang_key]['definition'] = def_trans
                word['translations'][lang_key]['example'] = ex_trans
                print(f"{lang_key}✓ ", end='')
                time.sleep(0.05)
            except Exception as e:
                print(f"{lang_key}✗ ", end='')
        
        print()
        
        # Save every 100 words
        if translated_count % 100 == 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(words, f, ensure_ascii=False, indent=2)
            print(f">>> Saved: {translated_count} words")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ {filename}: {translated_count} translations")
    return translated_count

def main():
    files = ['band45_words.json', 'band60_words.json', 'band70_words.json', 'band80_words.json']
    
    print("="*60)
    print("IELTS Vocabulary Translation (9 Languages)")
    print("="*60)
    
    start_time = time.time()
    total = 0
    
    for f in files:
        total += translate_file(f)
    
    elapsed = time.time() - start_time
    print(f"\n🎉 Complete! {total} words in {int(elapsed//60)}m {int(elapsed%60)}s")

if __name__ == '__main__':
    main()
