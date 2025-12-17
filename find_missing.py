import json

with open('assets/data/words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

missing = []
for w in words:
    t = w.get('translations', {})
    if not t.get('ko') or not t.get('ja') or not t.get('zh') or not t.get('es') or not t.get('fr') or not t.get('de'):
        missing.append({
            'word': w['word'],
            'definition': w['definition'],
            'translations': t
        })

print(f'누락된 단어 수: {len(missing)}')
for m in missing:
    print(f"\n{m['word']}: {m['definition']}")
    print(f"  현재 번역: {m['translations']}")
