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
    ("entrance","noun","a way in","The main entrance."),
    ("entrepreneur","noun","a person who sets up a business","A successful entrepreneur."),
    ("entry","noun","an act of entering","Entry to the building."),
    ("envelope","noun","a flat paper container for a letter","Mail envelope."),
    ("environment","noun","the surroundings","Natural environment."),
    ("environmental","adjective","relating to the natural world","Environmental protection."),
    ("environmentalist","noun","a person concerned about the environment","An environmentalist."),
    ("epidemic","noun","a widespread occurrence of a disease","A flu epidemic."),
    ("episode","noun","an event or incident","A dramatic episode."),
    ("equal","adjective","being the same in quantity","Equal rights."),
    ("equality","noun","the state of being equal","Gender equality."),
    ("equally","adverb","in the same manner or to the same extent","Equally important."),
    ("equation","noun","a mathematical statement","A simple equation."),
    ("equip","verb","supply with necessary items","Equip the team."),
    ("equipment","noun","the necessary items for a purpose","Sports equipment."),
    ("equivalent","adjective","equal in value or function","An equivalent amount."),
    ("era","noun","a long period of history","A new era."),
    ("erase","verb","remove all traces of","Erase the data."),
    ("error","noun","a mistake","A spelling error."),
    ("erupt","verb","break out suddenly","Volcano erupt."),
    ("escalate","verb","increase rapidly","Escalate tensions."),
    ("escape","verb","break free from confinement","Escape from prison."),
    ("especially","adverb","particularly","Especially useful."),
    ("essay","noun","a short piece of writing","Write an essay."),
    ("essence","noun","the intrinsic nature of something","The essence of life."),
    ("essential","adjective","absolutely necessary","Essential skills."),
    ("essentially","adverb","used to emphasize the basic nature","Essentially correct."),
    ("establish","verb","set up on a permanent basis","Establish a business."),
    ("established","adjective","having been in existence for a long time","An established company."),
    ("establishment","noun","the action of establishing","The establishment of rules."),
    ("estate","noun","an area of land","A large estate."),
    ("estimate","verb","roughly calculate","Estimate the cost."),
    ("estimation","noun","a rough calculation","In my estimation."),
    ("eternal","adjective","lasting forever","Eternal love."),
    ("ethic","noun","a moral principle","Work ethic."),
    ("ethical","adjective","relating to moral principles","Ethical behavior."),
    ("ethics","noun","moral principles","Business ethics."),
    ("ethnic","adjective","relating to a population subgroup","Ethnic diversity."),
    ("evaluate","verb","form an idea of the value of","Evaluate performance."),
    ("evaluation","noun","the making of a judgment","Performance evaluation."),
    ("even","adverb","used to emphasize something surprising","Even better."),
    ("evening","noun","the period of time at the end of the day","This evening."),
    ("event","noun","a thing that happens","A special event."),
    ("eventually","adverb","in the end","Eventually succeeded."),
    ("ever","adverb","at any time","Have you ever visited."),
    ("every","determiner","used to refer to all the individual members","Every day."),
    ("everybody","pronoun","every person","Everybody knows."),
    ("everyday","adjective","happening or used daily","Everyday life."),
    ("everyone","pronoun","every person","Everyone agrees."),
    ("everything","pronoun","all things","Everything is ready."),
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

t,a = add_to_file('band45_words.json', NEW_WORDS, 'Band 4.5-5.5')
print(f"Band 4.5-5.5: {t}개 (+{a})")

total = sum(len(json.load(open(f'assets/data/{f}','r',encoding='utf-8'))) 
    for f in ['band45_words.json','band60_words.json','band70_words.json','band80_words.json'])
print(f"총계: {total}개, 남은 수: {5000-total}개")
