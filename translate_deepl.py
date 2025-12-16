import json
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

DEEPL_API_KEY = "c9dd51e5-cf72-4c18-b092-2e70c87674e8:fx"
GOOGLE_API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"

# DeepL supports: KO, JA, ZH, ES, FR, DE
# Google needed for: VI, TH, ZH-TW

DEEPL_LANGS = {
    'ko': 'KO',
    'ja': 'JA', 
    'zh_cn': 'ZH',
    'es': 'ES',
    'fr': 'FR',
    'de': 'DE'
}

GOOGLE_LANGS = {
    'vi': 'vi',
    'th': 'th',
    'zh_tw': 'zh-TW'
}

def translate_deepl_batch(texts, target_lang):
    """Translate batch of texts using DeepL API"""
    url = "https://api-free.deepl.com/v2/translate"
    
    data = {
        'auth_key': DEEPL_API_KEY,
        'text': texts,
        'target_lang': target_lang,
        'source_lang': 'EN'
    }
    
    try:
        response = requests.post(url, data=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            return [t['text'] for t in result['translations']]
        else:
            print(f"DeepL error {response.status_code}: {response.text[:100]}")
            return None
    except Exception as e:
        print(f"DeepL exception: {e}")
        return None

def translate_google_batch(texts, target_lang):
    """Translate batch of texts using Google Cloud Translation API"""
    url = f"https://translation.googleapis.com/language/translate/v2?key={GOOGLE_API_KEY}"
    
    data = {
        'q': texts,
        'target': target_lang,
        'source': 'en',
        'format': 'text'
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            return [t['translatedText'] for t in result['data']['translations']]
        else:
            print(f"Google error {response.status_code}: {response.text[:100]}")
            return None
    except Exception as e:
        print(f"Google exception: {e}")
        return None

def translate_file(input_file, output_file):
    """Translate a single word file to all languages"""
    print(f"\n{'='*60}")
    print(f"Processing: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        words = json.load(f)  # JSON is a list directly
    
    total = len(words)
    print(f"Total words: {total}")
    
    # Collect all texts to translate
    definitions = [w['definition'] for w in words]
    examples = [w['example'] for w in words]
    
    # Batch size for API calls
    BATCH_SIZE = 50
    
    # Process DeepL languages
    for lang_key, lang_code in DEEPL_LANGS.items():
        print(f"\nTranslating to {lang_key} (DeepL)...")
        
        def_translations = []
        ex_translations = []
        
        # Translate definitions in batches
        for i in range(0, total, BATCH_SIZE):
            batch = definitions[i:i+BATCH_SIZE]
            result = translate_deepl_batch(batch, lang_code)
            if result:
                def_translations.extend(result)
            else:
                def_translations.extend(batch)  # Fallback to original
            
            if (i + BATCH_SIZE) % 200 == 0:
                print(f"  Definitions: {min(i+BATCH_SIZE, total)}/{total}")
        
        # Translate examples in batches
        for i in range(0, total, BATCH_SIZE):
            batch = examples[i:i+BATCH_SIZE]
            result = translate_deepl_batch(batch, lang_code)
            if result:
                ex_translations.extend(result)
            else:
                ex_translations.extend(batch)
            
            if (i + BATCH_SIZE) % 200 == 0:
                print(f"  Examples: {min(i+BATCH_SIZE, total)}/{total}")
        
        # Apply translations to words
        for idx, word in enumerate(words):
            if 'translations' not in word:
                word['translations'] = {}
            word['translations'][lang_key] = {
                'definition': def_translations[idx] if idx < len(def_translations) else word['definition'],
                'example': ex_translations[idx] if idx < len(ex_translations) else word['example']
            }
        
        print(f"  ✓ {lang_key} complete")
    
    # Process Google languages
    for lang_key, lang_code in GOOGLE_LANGS.items():
        print(f"\nTranslating to {lang_key} (Google)...")
        
        def_translations = []
        ex_translations = []
        
        # Translate definitions in batches
        for i in range(0, total, BATCH_SIZE):
            batch = definitions[i:i+BATCH_SIZE]
            result = translate_google_batch(batch, lang_code)
            if result:
                def_translations.extend(result)
            else:
                def_translations.extend(batch)
            
            if (i + BATCH_SIZE) % 200 == 0:
                print(f"  Definitions: {min(i+BATCH_SIZE, total)}/{total}")
        
        # Translate examples in batches
        for i in range(0, total, BATCH_SIZE):
            batch = examples[i:i+BATCH_SIZE]
            result = translate_google_batch(batch, lang_code)
            if result:
                ex_translations.extend(result)
            else:
                ex_translations.extend(batch)
            
            if (i + BATCH_SIZE) % 200 == 0:
                print(f"  Examples: {min(i+BATCH_SIZE, total)}/{total}")
        
        # Apply translations
        for idx, word in enumerate(words):
            if 'translations' not in word:
                word['translations'] = {}
            word['translations'][lang_key] = {
                'definition': def_translations[idx] if idx < len(def_translations) else word['definition'],
                'example': ex_translations[idx] if idx < len(ex_translations) else word['example']
            }
        
        print(f"  ✓ {lang_key} complete")
    
    # Save output
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Saved: {output_file}")
    return total

def main():
    base_path = r"c:\Users\hooni\Desktop\IELTS Prep Essential Vocabulary\assets\data"
    
    files = [
        ('band45_words.json', 'band45_words.json'),
        ('band60_words.json', 'band60_words.json'),
        ('band70_words.json', 'band70_words.json'),
        ('band80_words.json', 'band80_words.json'),
    ]
    
    start_time = time.time()
    total_words = 0
    
    for input_name, output_name in files:
        input_path = os.path.join(base_path, input_name)
        output_path = os.path.join(base_path, output_name)
        
        if os.path.exists(input_path):
            count = translate_file(input_path, output_path)
            total_words += count
    
    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"✅ COMPLETE!")
    print(f"Total words translated: {total_words}")
    print(f"Languages: 9 (ko, ja, zh_cn, zh_tw, es, fr, de, vi, th)")
    print(f"Time elapsed: {elapsed/60:.1f} minutes")

if __name__ == "__main__":
    main()
