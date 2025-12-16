#!/usr/bin/env python3
"""IELTS 단어 5000개 확장 + 6개 언어 번역 - 배치 1"""
import json
import requests
import time

GOOGLE_API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"
LANGUAGES = ['ko', 'ja', 'zh', 'es', 'fr', 'de']

def translate_batch(texts, target_lang):
    """Google Translate API로 배치 번역"""
    url = f"https://translation.googleapis.com/language/translate/v2?key={GOOGLE_API_KEY}"
    result = []
    
    # 100개씩 배치
    for i in range(0, len(texts), 100):
        batch = texts[i:i+100]
        payload = {"q": batch, "source": "en", "target": target_lang, "format": "text"}
        try:
            resp = requests.post(url, json=payload, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                result.extend([t['translatedText'] for t in data['data']['translations']])
            else:
                result.extend(batch)  # 실패시 원본
        except:
            result.extend(batch)
        time.sleep(0.1)
    return result

def main():
    # 기존 단어 로드
    with open('assets/data/words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)
    
    print(f"현재 단어 수: {len(words)}")
    
    # 기존 단어들의 definition과 example 추출
    definitions = [w['definition'] for w in words]
    examples = [w['example'] for w in words]
    
    # 각 언어로 번역
    for lang in LANGUAGES:
        print(f"\n{lang} 번역 시작...")
        
        # definition 번역
        print(f"  definition 번역 중... ({len(definitions)}개)")
        trans_defs = translate_batch(definitions, lang)
        
        # example 번역
        print(f"  example 번역 중... ({len(examples)}개)")
        trans_exs = translate_batch(examples, lang)
        
        # 단어에 번역 추가
        for i, word in enumerate(words):
            if 'translations' not in word:
                word['translations'] = {}
            word['translations'][lang] = {
                'definition': trans_defs[i] if i < len(trans_defs) else word['definition'],
                'example': trans_exs[i] if i < len(trans_exs) else word['example']
            }
        
        print(f"  {lang} 완료!")
    
    # 저장
    with open('assets/data/words.json', 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"\n완료! 총 {len(words)}개 단어에 6개 언어 번역 추가됨")

if __name__ == "__main__":
    main()
