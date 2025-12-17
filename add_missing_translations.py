import json

# 20개 누락된 단어의 번역
translations_to_add = {
    "abroad": {
        "ko": "해외에서",
        "ja": "海外で",
        "zh": "在国外",
        "es": "en el extranjero",
        "fr": "à l'étranger",
        "de": "im Ausland"
    },
    "acceptable": {
        "ko": "받아들일 수 있는",
        "ja": "受け入れられる",
        "zh": "可接受的",
        "es": "aceptable",
        "fr": "acceptable",
        "de": "akzeptabel"
    },
    "according": {
        "ko": "~에 따르면",
        "ja": "〜によると",
        "zh": "根据",
        "es": "según",
        "fr": "selon",
        "de": "gemäß"
    },
    "adolescent": {
        "ko": "청소년",
        "ja": "青年",
        "zh": "青少年",
        "es": "adolescente",
        "fr": "adolescent",
        "de": "Jugendlicher"
    },
    "adult": {
        "ko": "성인",
        "ja": "大人",
        "zh": "成年人",
        "es": "adulto",
        "fr": "adulte",
        "de": "Erwachsener"
    },
    "afraid": {
        "ko": "두려운",
        "ja": "怖がって",
        "zh": "害怕的",
        "es": "asustado",
        "fr": "effrayé",
        "de": "ängstlich"
    },
    "agency": {
        "ko": "기관",
        "ja": "機関",
        "zh": "机构",
        "es": "agencia",
        "fr": "agence",
        "de": "Agentur"
    },
    "agent": {
        "ko": "대리인",
        "ja": "代理人",
        "zh": "代理人",
        "es": "agente",
        "fr": "agent",
        "de": "Agent"
    },
    "agriculture": {
        "ko": "농업",
        "ja": "農業",
        "zh": "农业",
        "es": "agricultura",
        "fr": "agriculture",
        "de": "Landwirtschaft"
    },
    "aircraft": {
        "ko": "항공기",
        "ja": "航空機",
        "zh": "飞机",
        "es": "aeronave",
        "fr": "aéronef",
        "de": "Flugzeug"
    },
    "albeit": {
        "ko": "비록 ~이지만",
        "ja": "〜ではあるが",
        "zh": "尽管",
        "es": "aunque",
        "fr": "bien que",
        "de": "obgleich"
    },
    "append": {
        "ko": "추가하다",
        "ja": "追加する",
        "zh": "附加",
        "es": "añadir",
        "fr": "ajouter",
        "de": "anhängen"
    },
    "assemble": {
        "ko": "조립하다",
        "ja": "組み立てる",
        "zh": "组装",
        "es": "ensamblar",
        "fr": "assembler",
        "de": "zusammenbauen"
    },
    "asset": {
        "ko": "자산",
        "ja": "資産",
        "zh": "资产",
        "es": "activo",
        "fr": "actif",
        "de": "Vermögenswert"
    },
    "assure": {
        "ko": "확신시키다",
        "ja": "保証する",
        "zh": "保证",
        "es": "asegurar",
        "fr": "assurer",
        "de": "versichern"
    },
    "chemical": {
        "ko": "화학물질",
        "ja": "化学物質",
        "zh": "化学物质",
        "es": "químico",
        "fr": "produit chimique",
        "de": "Chemikalie"
    },
    "confer": {
        "ko": "협의하다",
        "ja": "協議する",
        "zh": "商议",
        "es": "conferir",
        "fr": "conférer",
        "de": "beraten"
    },
    "consequent": {
        "ko": "결과로 생기는",
        "ja": "結果として生じる",
        "zh": "随之发生的",
        "es": "consecuente",
        "fr": "conséquent",
        "de": "daraus folgend"
    },
    "depress": {
        "ko": "우울하게 하다",
        "ja": "落ち込ませる",
        "zh": "使沮丧",
        "es": "deprimir",
        "fr": "déprimer",
        "de": "deprimieren"
    },
    "device": {
        "ko": "장치",
        "ja": "装置",
        "zh": "设备",
        "es": "dispositivo",
        "fr": "appareil",
        "de": "Gerät"
    }
}

# words.json 로드
with open('assets/data/words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# 번역 추가
updated_count = 0
for word in words:
    if word['word'] in translations_to_add:
        word['translations'] = translations_to_add[word['word']]
        updated_count += 1
        print(f"✓ {word['word']} 번역 추가됨")

# 저장
with open('assets/data/words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"\n총 {updated_count}개 단어 번역 추가 완료!")
