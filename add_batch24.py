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
    ("vacillate","verb","waver between different opinions","Vacillate on the decision."),
    ("vacuous","adjective","having or showing a lack of thought","A vacuous expression."),
    ("vagary","noun","an unexpected and inexplicable change","The vagaries of fate."),
    ("vague","adjective","of uncertain meaning","A vague idea."),
    ("vain","adjective","producing no result","A vain attempt."),
    ("valiant","adjective","possessing courage","A valiant effort."),
    ("valid","adjective","having legal force","A valid argument."),
    ("validate","verb","check or prove the validity","Validate the results."),
    ("validity","noun","the quality of being valid","Question the validity."),
    ("valuable","adjective","worth a great deal of money","Valuable information."),
    ("value","noun","the importance or worth of something","Core values."),
    ("vanish","verb","disappear suddenly","Vanish without a trace."),
    ("variable","adjective","not consistent","Variable conditions."),
    ("variance","noun","the fact of being different","At variance with."),
    ("variant","noun","a form differing from others","A new variant."),
    ("variation","noun","a change or difference","Slight variation."),
    ("varied","adjective","incorporating a number of different types","A varied diet."),
    ("variety","noun","the quality of being different","A variety of options."),
    ("various","adjective","different from one another","Various reasons."),
    ("vary","verb","differ in size or amount","Prices vary."),
    ("vast","adjective","of very great extent","A vast area."),
    ("vastly","adverb","to a very great extent","Vastly different."),
    ("vegetable","noun","a plant cultivated for food","Fresh vegetables."),
    ("vegetation","noun","plants considered collectively","Dense vegetation."),
    ("vehicle","noun","a thing used for transport","A motor vehicle."),
    ("veil","noun","a piece of fine material covering something","A veil of secrecy."),
    ("velocity","noun","the speed of something","High velocity."),
    ("vendor","noun","a person who sells something","Street vendor."),
    ("venerable","adjective","accorded a great deal of respect","A venerable institution."),
    ("venerate","verb","regard with great respect","Venerate tradition."),
    ("venture","noun","a risky business enterprise","A new venture."),
    ("venue","noun","the place where something happens","The venue for the event."),
    ("verbal","adjective","relating to words","Verbal agreement."),
    ("verbally","adverb","in spoken words","Verbally agree."),
    ("verdict","noun","a decision on a disputed issue","The jury's verdict."),
    ("verge","noun","an edge or border","On the verge of."),
    ("verify","verb","make sure something is true","Verify the information."),
    ("versatile","adjective","able to adapt to many functions","A versatile tool."),
    ("version","noun","a particular form of something","The latest version."),
    ("versus","preposition","against","Team A versus Team B."),
    ("vertical","adjective","at right angles to a horizontal plane","Vertical line."),
    ("very","adverb","in a high degree","Very important."),
    ("vessel","noun","a ship or large boat","A cargo vessel."),
    ("veteran","noun","a person of long experience","A veteran journalist."),
    ("veto","verb","reject something","Veto the proposal."),
    ("via","preposition","by way of","Travel via train."),
    ("viable","adjective","capable of working successfully","A viable option."),
    ("vibrant","adjective","full of energy and life","A vibrant community."),
    ("vicious","adjective","deliberately cruel","A vicious attack."),
    ("victim","noun","a person harmed by a crime","Crime victim."),
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
