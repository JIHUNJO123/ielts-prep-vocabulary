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
    ("aberration","noun","a departure from what is normal","A statistical aberration."),
    ("abhor","verb","regard with disgust","Abhor violence."),
    ("abhorrent","adjective","inspiring disgust and loathing","An abhorrent act."),
    ("abject","adjective","extremely bad or severe","Abject poverty."),
    ("ablaze","adjective","burning fiercely","The building was ablaze."),
    ("abnormality","noun","something that is not normal","Detect abnormalities."),
    ("abolish","verb","formally put an end to","Abolish the law."),
    ("abolition","noun","the action of abolishing","The abolition of slavery."),
    ("aboriginal","adjective","inhabiting a land from earliest times","Aboriginal culture."),
    ("abound","verb","exist in large numbers","Opportunities abound."),
    ("abrasive","adjective","harsh and causing damage","An abrasive personality."),
    ("abreast","adverb","side by side","Keep abreast of developments."),
    ("abridge","verb","shorten without losing sense","An abridged version."),
    ("abrupt","adjective","sudden and unexpected","An abrupt change."),
    ("abruptly","adverb","suddenly and unexpectedly","Stopped abruptly."),
    ("abstain","verb","restrain oneself from doing something","Abstain from voting."),
    ("abstinence","noun","the practice of restraining oneself","Total abstinence."),
    ("abysmal","adjective","extremely bad","Abysmal performance."),
    ("abyss","noun","a deep chasm","The abyss of despair."),
    ("accede","verb","agree to a demand","Accede to requests."),
    ("acclaim","noun","enthusiastic public praise","Critical acclaim."),
    ("accolade","noun","an award or privilege","Receive an accolade."),
    ("accomplice","noun","a person who helps in a crime","An accomplice to fraud."),
    ("accost","verb","approach and address boldly","Accosted by strangers."),
    ("accrue","verb","accumulate over time","Benefits accrue."),
    ("acerbic","adjective","sharp and forthright","An acerbic comment."),
    ("ache","verb","suffer a continuous dull pain","My head aches."),
    ("acidic","adjective","having the properties of an acid","Acidic soil."),
    ("acknowledge","verb","accept or admit the existence of","Acknowledge the problem."),
    ("acquaint","verb","make someone aware of something","Acquaint yourself with."),
    ("acquaintance","noun","a person one knows slightly","A casual acquaintance."),
    ("acquiesce","verb","accept reluctantly without protest","Acquiesce to demands."),
    ("acquit","verb","declare not guilty of a charge","Acquitted of all charges."),
    ("acronym","noun","an abbreviation from initial letters","NASA is an acronym."),
    ("activate","verb","make something active","Activate the system."),
    ("activism","noun","the policy of taking direct action","Political activism."),
    ("activist","noun","a person who campaigns for change","A human rights activist."),
    ("acute","adjective","very serious or severe","An acute shortage."),
    ("adamant","adjective","refusing to be persuaded","Adamant about the decision."),
    ("adaptable","adjective","able to adjust to new conditions","Highly adaptable."),
    ("adaptation","noun","the action of adapting","Climate adaptation."),
    ("addendum","noun","an item added at the end","An addendum to the report."),
    ("addiction","noun","the fact of being addicted","Drug addiction."),
    ("addictive","adjective","causing addiction","An addictive substance."),
    ("additionally","adverb","as an extra factor","Additionally important."),
    ("adept","adjective","very skilled","Adept at handling problems."),
    ("adequacy","noun","the state of being adequate","Question the adequacy."),
    ("adhere","verb","stick fast to a surface","Adhere to the rules."),
    ("adherent","noun","someone who supports a belief","A strong adherent."),
    ("adjacent","adjective","next to or adjoining","Adjacent buildings."),
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
