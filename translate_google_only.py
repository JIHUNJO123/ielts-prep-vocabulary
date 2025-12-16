"""
Google Cloud Translation API만 사용하여 모든 언어 번역
DeepL 할당량 초과로 인해 Google Cloud API로 전환
"""
import json
import requests
import os
from pathlib import Path

# Google Cloud Translation API
GOOGLE_API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"
GOOGLE_URL = "https://translation.googleapis.com/language/translate/v2"

# 배치 크기 (Google은 128개까지 지원)
BATCH_SIZE = 100

# 번역할 언어들 (모두 Google API로)
LANGUAGES = {
    'ko': 'ko',      # 한국어
    'ja': 'ja',      # 일본어
    'zh_cn': 'zh-CN', # 중국어 간체
    'es': 'es',      # 스페인어
    'fr': 'fr',      # 프랑스어
    'de': 'de',      # 독일어
    'vi': 'vi',      # 베트남어
    'th': 'th',      # 태국어
    'zh_tw': 'zh-TW' # 중국어 번체
}

def translate_google_batch(texts: list, target_lang: str) -> list:
    """Google Cloud Translation API로 배치 번역"""
    if not texts:
        return []
    
    try:
        response = requests.post(
            GOOGLE_URL,
            params={'key': GOOGLE_API_KEY},
            json={
                'q': texts,
                'target': target_lang,
                'source': 'en',
                'format': 'text'
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return [t['translatedText'] for t in result['data']['translations']]
        else:
            print(f"Google error {response.status_code}: {response.text[:100]}")
            return texts  # 에러 시 원본 반환
    except Exception as e:
        print(f"Google exception: {e}")
        return texts

def check_if_translated(word: dict, lang_key: str) -> bool:
    """해당 언어의 번역이 이미 있는지 확인"""
    def_key = f'definition_{lang_key}'
    ex_key = f'example_{lang_key}'
    
    has_def = def_key in word and word[def_key] and len(word[def_key]) > 5
    has_ex = ex_key in word and word[ex_key] and len(word[ex_key]) > 5
    
    return has_def and has_ex

def translate_file(filepath: str, languages_to_translate: list = None):
    """파일의 모든 단어를 지정된 언어로 번역"""
    
    print(f"\n{'='*60}")
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        words = json.load(f)
    
    total = len(words)
    print(f"Total words: {total}")
    
    if languages_to_translate is None:
        languages_to_translate = list(LANGUAGES.keys())
    
    for lang_key in languages_to_translate:
        google_lang = LANGUAGES[lang_key]
        
        # 번역이 필요한 단어들만 필터링
        words_to_translate = []
        indices_to_translate = []
        
        for i, word in enumerate(words):
            if not check_if_translated(word, lang_key):
                words_to_translate.append(word)
                indices_to_translate.append(i)
        
        if not words_to_translate:
            print(f"\n✓ {lang_key} already complete (all {total} words translated)")
            continue
        
        print(f"\nTranslating to {lang_key} (Google)... ({len(words_to_translate)} words need translation)")
        
        # Definition 번역
        definitions = [w.get('definition', '') for w in words_to_translate]
        translated_defs = []
        
        for i in range(0, len(definitions), BATCH_SIZE):
            batch = definitions[i:i+BATCH_SIZE]
            result = translate_google_batch(batch, google_lang)
            translated_defs.extend(result)
            print(f"  Definitions: {min(i+BATCH_SIZE, len(definitions))}/{len(definitions)}")
        
        # Example 번역
        examples = [w.get('example', '') for w in words_to_translate]
        translated_examples = []
        
        for i in range(0, len(examples), BATCH_SIZE):
            batch = examples[i:i+BATCH_SIZE]
            result = translate_google_batch(batch, google_lang)
            translated_examples.extend(result)
            print(f"  Examples: {min(i+BATCH_SIZE, len(examples))}/{len(examples)}")
        
        # 결과 저장
        for idx, (def_trans, ex_trans) in enumerate(zip(translated_defs, translated_examples)):
            original_idx = indices_to_translate[idx]
            words[original_idx][f'definition_{lang_key}'] = def_trans
            words[original_idx][f'example_{lang_key}'] = ex_trans
        
        print(f"  ✓ {lang_key} complete")
    
    # 파일 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Saved: {filepath}")

def main():
    # 데이터 폴더 경로
    data_dir = Path(r"c:\Users\hooni\Desktop\IELTS Prep Essential Vocabulary\assets\data")
    
    # 번역할 파일들
    files = [
        data_dir / "band45_words.json",
        data_dir / "band60_words.json", 
        data_dir / "band70_words.json",
        data_dir / "band80_words.json",
    ]
    
    print("="*60)
    print("Google Cloud Translation - Fill Missing Translations")
    print("="*60)
    
    for filepath in files:
        if filepath.exists():
            translate_file(str(filepath))
        else:
            print(f"File not found: {filepath}")
    
    print("\n" + "="*60)
    print("All translations completed!")
    print("="*60)

if __name__ == "__main__":
    main()
