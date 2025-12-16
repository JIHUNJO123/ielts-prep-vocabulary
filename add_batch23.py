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
    ("ubiquitous","adjective","present everywhere","Ubiquitous technology."),
    ("ultimatum","noun","a final demand","Issue an ultimatum."),
    ("umbrella","noun","a device for protection from rain","Umbrella organization."),
    ("unanimous","adjective","fully in agreement","A unanimous decision."),
    ("unaware","adjective","having no knowledge of something","Unaware of the danger."),
    ("uncertainty","noun","the state of being uncertain","Economic uncertainty."),
    ("undergo","verb","experience something unpleasant","Undergo surgery."),
    ("undergraduate","noun","a university student","An undergraduate student."),
    ("underlie","verb","be the cause or basis of","Underlie the problem."),
    ("underlying","adjective","being the real cause","The underlying issue."),
    ("undermine","verb","erode the base of","Undermine confidence."),
    ("underscore","verb","emphasize","Underscore the importance."),
    ("undertake","verb","commit oneself to begin","Undertake a project."),
    ("uneven","adjective","not level or smooth","Uneven distribution."),
    ("unexpected","adjective","not expected","An unexpected result."),
    ("unfold","verb","reveal or be revealed","Events unfold."),
    ("unfortunate","adjective","having bad luck","An unfortunate incident."),
    ("unfortunately","adverb","it is unfortunate that","Unfortunately, it failed."),
    ("unified","adjective","made into a whole","A unified approach."),
    ("uniform","adjective","not varying","Uniform standards."),
    ("unique","adjective","being the only one of its kind","A unique opportunity."),
    ("uniquely","adverb","in a unique manner","Uniquely qualified."),
    ("unity","noun","the state of being united","National unity."),
    ("universal","adjective","relating to all people","Universal access."),
    ("universe","noun","all existing matter and space","The universe."),
    ("university","noun","an institution of higher education","A prestigious university."),
    ("unknown","adjective","not known or familiar","An unknown factor."),
    ("unlike","preposition","different from","Unlike before."),
    ("unlikely","adjective","not likely to happen","An unlikely event."),
    ("unlimited","adjective","not limited or restricted","Unlimited access."),
    ("unprecedented","adjective","never done or known before","Unprecedented growth."),
    ("unpredictable","adjective","not able to be predicted","Unpredictable weather."),
    ("until","preposition","up to the point in time","Until tomorrow."),
    ("unusual","adjective","not habitually or commonly done","An unusual case."),
    ("update","verb","make something more modern","Update the software."),
    ("upgrade","verb","raise to a higher standard","Upgrade the system."),
    ("uphold","verb","confirm or support","Uphold the law."),
    ("upon","preposition","on","Upon arrival."),
    ("upper","adjective","higher in position","Upper level."),
    ("urban","adjective","relating to a city","Urban development."),
    ("urge","verb","try earnestly to persuade","Urge caution."),
    ("urgent","adjective","requiring immediate action","An urgent matter."),
    ("usage","noun","the action of using something","Correct usage."),
    ("useful","adjective","able to be used for a practical purpose","A useful tool."),
    ("useless","adjective","not fulfilling a purpose","A useless effort."),
    ("user","noun","a person who uses something","End user."),
    ("usual","adjective","habitually or typically occurring","The usual time."),
    ("usually","adverb","under normal conditions","Usually arrives on time."),
    ("utility","noun","the state of being useful","Public utility."),
    ("utilize","verb","make practical use of","Utilize resources."),
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

t,a = add_to_file('band70_words.json', NEW_WORDS, 'Band 7.0-7.5')
print(f"Band 7.0-7.5: {t}개 (+{a})")

total = sum(len(json.load(open(f'assets/data/{f}','r',encoding='utf-8'))) 
    for f in ['band45_words.json','band60_words.json','band70_words.json','band80_words.json'])
print(f"총계: {total}개, 남은 수: {5000-total}개")
