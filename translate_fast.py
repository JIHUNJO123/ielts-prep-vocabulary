import json
import os
import time
import concurrent.futures
from deep_translator import GoogleTranslator

LANGUAGES = ['ko', 'ja', 'zh-CN', 'es', 'de', 'fr', 'pt', 'vi', 'ar']
LANG_KEYS = ['ko', 'ja', 'zh', 'es', 'de', 'fr', 'pt', 'vi', 'ar']

def translate_batch(texts, target_lang):
    """Translate a batch of texts"""
    results = []
    translator = GoogleTranslator(source='en', target=target_lang)
    for text in texts:
        try:
            if text:
                result = translator.translate(text)
                results.append(result if result else '')
            else:
                results.append('')
        except:
            results.append('')
    return results

def process_file(filename):
    filepath = f'assets/data/{filename}'
    print(f"\n{'='*50}")
    print(f"Processing: {filename}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        words = json.load(f)
    
    # Filter words needing translation
    to_translate = []
    for i, word in enumerate(words):
        if 'translations' not in word:
            word['translations'] = {k: {"definition": "", "example": ""} for k in LANG_KEYS}
        ko_def = word.get('translations', {}).get('ko', {}).get('definition', '')
        if not ko_def:
            to_translate.append((i, word))
    
    if not to_translate:
        print(f"  All {len(words)} words already translated")
        return 0
    
    print(f"  {len(to_translate)} words need translation")
    
    # Process in batches of 50
    batch_size = 50
    for batch_start in range(0, len(to_translate), batch_size):
        batch = to_translate[batch_start:batch_start + batch_size]
        
        # Collect texts
        definitions = [w['definition'] for _, w in batch]
        examples = [w['example'] for _, w in batch]
        
        print(f"  Batch {batch_start//batch_size + 1}/{(len(to_translate)-1)//batch_size + 1}: ", end='')
        
        # Translate to each language
        for lang_code, lang_key in zip(LANGUAGES, LANG_KEYS):
            def_trans = translate_batch(definitions, lang_code)
            ex_trans = translate_batch(examples, lang_code)
            
            for j, (idx, word) in enumerate(batch):
                if lang_key not in words[idx]['translations']:
                    words[idx]['translations'][lang_key] = {"definition": "", "example": ""}
                words[idx]['translations'][lang_key]['definition'] = def_trans[j]
                words[idx]['translations'][lang_key]['example'] = ex_trans[j]
            
            print(f"{lang_key}✓ ", end='')
            time.sleep(0.1)
        
        print()
        
        # Save after each batch
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ Completed: {len(to_translate)} words")
    return len(to_translate)

def main():
    files = ['band45_words.json', 'band60_words.json', 'band70_words.json', 'band80_words.json']
    
    print("="*50)
    print("IELTS Vocabulary Fast Translation")
    print("="*50)
    
    start = time.time()
    total = sum(process_file(f) for f in files)
    elapsed = time.time() - start
    
    print(f"\n🎉 Done! {total} words in {int(elapsed//60)}m {int(elapsed%60)}s")

if __name__ == '__main__':
    main()
