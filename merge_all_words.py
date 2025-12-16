#!/usr/bin/env python3
"""모든 Band 단어 파일을 합쳐서 words.json 생성"""
import json
import os

def main():
    all_words = []
    band_files = [
        'assets/data/band45_words.json',
        'assets/data/band60_words.json',
        'assets/data/band70_words.json',
        'assets/data/band80_words.json'
    ]
    
    word_id = 1
    seen_words = set()
    
    for band_file in band_files:
        if os.path.exists(band_file):
            with open(band_file, 'r', encoding='utf-8') as f:
                words = json.load(f)
                for word in words:
                    if word['word'] not in seen_words:
                        word['id'] = word_id
                        all_words.append(word)
                        seen_words.add(word['word'])
                        word_id += 1
    
    with open('assets/data/words.json', 'w', encoding='utf-8') as f:
        json.dump(all_words, f, indent=2, ensure_ascii=False)
    
    # 통계 출력
    band_counts = {}
    for word in all_words:
        level = word['level']
        band_counts[level] = band_counts.get(level, 0) + 1
    
    print("=" * 50)
    print("📊 단어 통계:")
    print("=" * 50)
    for level, count in sorted(band_counts.items()):
        print(f"  {level}: {count}개")
    print("=" * 50)
    print(f"✅ 총 단어 수: {len(all_words)}개")
    print("=" * 50)

if __name__ == '__main__':
    main()
