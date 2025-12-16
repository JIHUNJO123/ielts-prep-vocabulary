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
    ("amazing","adjective","causing great surprise or wonder","An amazing discovery."),
    ("ambassador","noun","an accredited diplomat","The US ambassador."),
    ("ambient","adjective","relating to the immediate surroundings","Ambient temperature."),
    ("ambiguity","noun","the quality of being open to interpretation","Avoid ambiguity."),
    ("ambiguous","adjective","open to more than one interpretation","An ambiguous statement."),
    ("ambition","noun","a strong desire to achieve something","Career ambition."),
    ("ambitious","adjective","having a strong desire to succeed","An ambitious plan."),
    ("ambivalent","adjective","having mixed feelings","Ambivalent about the change."),
    ("ambulance","noun","a vehicle for taking sick people to hospital","Call an ambulance."),
    ("amend","verb","make minor changes to improve","Amend the law."),
    ("amendment","noun","a minor change or addition","Constitutional amendment."),
    ("amenity","noun","a desirable feature","Modern amenities."),
    ("amid","preposition","surrounded by","Amid the chaos."),
    ("amidst","preposition","in the middle of","Amidst the crowd."),
    ("ammunition","noun","a supply of bullets","Run out of ammunition."),
    ("amnesty","noun","an official pardon","Grant amnesty."),
    ("amplify","verb","increase the volume or strength","Amplify the signal."),
    ("amuse","verb","cause to find something funny","Amuse the audience."),
    ("amusement","noun","the state of finding something funny","For amusement."),
    ("amusing","adjective","causing laughter","An amusing story."),
    ("analogy","noun","a comparison between two things","Draw an analogy."),
    ("analyse","verb","examine methodically","Analyse the data."),
    ("analyst","noun","a person who conducts analysis","Financial analyst."),
    ("analytic","adjective","relating to analysis","Analytic skills."),
    ("analytical","adjective","using analysis","Analytical thinking."),
    ("analyze","verb","examine methodically","Analyze the results."),
    ("ancestor","noun","a person from whom one is descended","Early ancestors."),
    ("ancestral","adjective","of or inherited from ancestors","Ancestral home."),
    ("ancestry","noun","one's family or ethnic descent","Trace ancestry."),
    ("anchor","noun","a heavy device to moor a vessel","Drop anchor."),
    ("ancient","adjective","belonging to the very distant past","Ancient history."),
    ("anecdote","noun","a short amusing story","Personal anecdote."),
    ("angel","noun","a spiritual being","Guardian angel."),
    ("anger","noun","a strong feeling of annoyance","Control anger."),
    ("angle","noun","the space between two intersecting lines","Right angle."),
    ("anguish","noun","severe mental or physical pain","In anguish."),
    ("animated","adjective","full of life or excitement","An animated discussion."),
    ("animation","noun","the state of being full of life","Computer animation."),
    ("animosity","noun","strong hostility","Personal animosity."),
    ("ankle","noun","the joint connecting the foot to the leg","Sprain the ankle."),
    ("annex","verb","add as an extra part","Annex territory."),
    ("anniversary","noun","the date on which an event occurred","Wedding anniversary."),
    ("annotate","verb","add notes of explanation","Annotate the text."),
    ("annotation","noun","a note of explanation","Text annotation."),
    ("announce","verb","make a public statement","Announce the results."),
    ("announcement","noun","a public statement","Official announcement."),
    ("annoy","verb","irritate someone","Annoy the neighbors."),
    ("annoyance","noun","the feeling of being annoyed","Express annoyance."),
    ("annoying","adjective","causing irritation","An annoying habit."),
    ("annual","adjective","occurring once every year","Annual report."),
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

t,a = add_to_file('band60_words.json', NEW_WORDS, 'Band 6.0-6.5')
print(f"Band 6.0-6.5: {t}개 (+{a})")

total = sum(len(json.load(open(f'assets/data/{f}','r',encoding='utf-8'))) 
    for f in ['band45_words.json','band60_words.json','band70_words.json','band80_words.json'])
print(f"총계: {total}개, 남은 수: {5000-total}개")
