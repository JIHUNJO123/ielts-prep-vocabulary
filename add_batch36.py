import json, os

def load_existing():
    words = set()
    for f in ['band45_words.json','band60_words.json','band70_words.json','band80_words.json']:
        path = f'assets/data/{f}'
        if os.path.exists(path):
            with open(path,'r',encoding='utf-8') as file:
                for w in json.load(file): words.add(w['word'].lower())
    return words

existing = load_existing()

NEW_WORDS = [
    ("atrocity","noun","an extremely wicked act","Commit an atrocity."),
    ("attain","verb","succeed in achieving","Attain the goal."),
    ("attainment","noun","the action of achieving something","Educational attainment."),
    ("attempted","adjective","tried but not successfully completed","An attempted robbery."),
    ("attendant","noun","a person employed to provide a service","Flight attendant."),
    ("attest","verb","provide or serve as evidence","Attest to the fact."),
    ("attic","noun","a space just below the roof","Store in the attic."),
    ("attorney","noun","a person appointed to act for another in legal matters","Hire an attorney."),
    ("attributable","adjective","able to be attributed to","Attributable to success."),
    ("attribute","verb","regard something as being caused by","Attribute the success to."),
    ("attribution","noun","the action of regarding something as being caused by","Proper attribution."),
    ("auction","noun","a public sale","Auction house."),
    ("audible","adjective","able to be heard","Barely audible."),
    ("audition","noun","an interview for a performer","Acting audition."),
    ("auditor","noun","a person who conducts an audit","Financial auditor."),
    ("auditorium","noun","a large room for audiences","School auditorium."),
    ("augment","verb","make something greater by adding to it","Augment income."),
    ("aura","noun","the distinctive atmosphere","An aura of mystery."),
    ("authentic","adjective","of undisputed origin","An authentic artifact."),
    ("authenticity","noun","the quality of being authentic","Verify authenticity."),
    ("authoritative","adjective","commanding and self-confident","An authoritative source."),
    ("authorization","noun","official permission","Get authorization."),
    ("authorize","verb","give official permission","Authorize the transaction."),
    ("autobiography","noun","an account of a person's life written by themselves","Write an autobiography."),
    ("autocracy","noun","a system of government by one person","An autocracy regime."),
]

def add_to_file(filename, words, level):
    path = f'assets/data/{filename}'
    data = json.load(open(path,'r',encoding='utf-8')) if os.path.exists(path) else []
    exist = set(w['word'].lower() for w in data)
    max_id = max([w['id'] for w in data], default=0)
    added = 0
    for word,pos,defn,ex in words:
        if word.lower() not in exist and word.lower() not in existing:
            max_id += 1
            data.append({"id":max_id,"word":word,"level":level,"partOfSpeech":pos,
                "definition":defn,"example":ex,"translations":{"ko":{"definition":"","example":""},
                "ja":{"definition":"","example":""},"zh":{"definition":"","example":""},
                "es":{"definition":"","example":""},"de":{"definition":"","example":""},
                "fr":{"definition":"","example":""},"pt":{"definition":"","example":""},
                "vi":{"definition":"","example":""},"ar":{"definition":"","example":""}}})
            added += 1
    json.dump(data,open(path,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    return len(data), added

t,a = add_to_file('band80_words.json', NEW_WORDS, 'Band 8.0+')
print(f"Band 8.0+: {t}개 (+{a})")

total = sum(len(json.load(open(f'assets/data/{f}','r',encoding='utf-8'))) 
    for f in ['band45_words.json','band60_words.json','band70_words.json','band80_words.json'])
print(f"총계: {total}개, 남은 수: {5000-total}개")
