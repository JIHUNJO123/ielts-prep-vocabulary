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
    ("collaboration","noun","the action of working with someone","Close collaboration."),
    ("collapse","verb","suddenly fall down","The building collapsed."),
    ("collar","noun","the part around the neck of a shirt","A white collar."),
    ("colleague","noun","a person one works with","A trusted colleague."),
    ("collective","adjective","done by people acting as a group","Collective effort."),
    ("collector","noun","a person who collects things","An art collector."),
    ("colonial","adjective","relating to a colony","Colonial history."),
    ("colony","noun","a country under another's control","A former colony."),
    ("colossal","adjective","extremely large","A colossal mistake."),
    ("column","noun","an upright pillar","A newspaper column."),
    ("combat","noun","fighting between armed forces","Armed combat."),
    ("combination","noun","a joining of different things","A winning combination."),
    ("combine","verb","unite or merge","Combine resources."),
    ("comedy","noun","entertainment intended to make people laugh","A romantic comedy."),
    ("comfort","noun","a state of physical ease","Creature comforts."),
    ("comfortable","adjective","providing physical ease","A comfortable chair."),
    ("comic","adjective","causing laughter","A comic strip."),
    ("commander","noun","a person in authority","The commander in chief."),
    ("commemorate","verb","recall and show respect for","Commemorate the event."),
    ("commence","verb","begin or start","Commence operations."),
    ("commend","verb","praise formally","Commend the effort."),
    ("commerce","noun","the activity of buying and selling","E-commerce."),
    ("commercial","adjective","concerned with commerce","A commercial venture."),
    ("commission","noun","an instruction to do something","On commission."),
    ("commissioner","noun","a person appointed to a commission","A police commissioner."),
    ("commitment","noun","the state of being dedicated","A firm commitment."),
    ("committed","adjective","feeling dedication","A committed employee."),
    ("committee","noun","a group of people appointed for a function","A steering committee."),
    ("commodity","noun","a raw material or product","A valuable commodity."),
    ("commonplace","adjective","not unusual; ordinary","A commonplace occurrence."),
    ("commonwealth","noun","an international association of nations","The Commonwealth."),
    ("communal","adjective","shared by all members of a community","Communal areas."),
    ("communicate","verb","share information","Communicate effectively."),
    ("communication","noun","the imparting of information","Clear communication."),
    ("communist","noun","a supporter of communism","A communist party."),
    ("community","noun","a group of people living together","The local community."),
    ("commute","verb","travel some distance to work","Commute daily."),
    ("compact","adjective","closely and neatly packed together","A compact car."),
    ("companion","noun","a person one spends time with","A traveling companion."),
    ("comparable","adjective","able to be compared","Comparable prices."),
    ("comparative","adjective","measured by comparison","Comparative advantage."),
    ("compare","verb","estimate similarities","Compare and contrast."),
    ("comparison","noun","an examination of similarities","By comparison."),
    ("compartment","noun","a separate section","A storage compartment."),
    ("compass","noun","an instrument showing direction","A moral compass."),
    ("compassion","noun","sympathetic concern for others","Show compassion."),
    ("compatible","adjective","able to exist together","Compatible systems."),
    ("compel","verb","force or oblige","Compel action."),
    ("compensate","verb","give something to make up for loss","Compensate for damages."),
    ("compensation","noun","something given to make up for loss","Financial compensation."),
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
