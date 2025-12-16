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
    ("citizen","noun","a legally recognized subject of a state","A US citizen."),
    ("citizenship","noun","the position or status of being a citizen","Dual citizenship."),
    ("civic","adjective","relating to a city or town","Civic duty."),
    ("civilization","noun","an advanced stage of human society","Ancient civilization."),
    ("civilize","verb","bring to an advanced stage","Civilize society."),
    ("clap","verb","strike the palms together","Clap your hands."),
    ("clarify","verb","make a statement less confused","Clarify the issue."),
    ("clarity","noun","the quality of being clear","Crystal clarity."),
    ("clash","verb","come into conflict","A clash of opinions."),
    ("clasp","verb","grasp tightly with hand","Clasp hands."),
    ("classic","adjective","judged over time to be of highest quality","A classic novel."),
    ("classical","adjective","representing an exemplary standard","Classical music."),
    ("classification","noun","the action of classifying","Data classification."),
    ("classify","verb","arrange in classes","Classify information."),
    ("clause","noun","a unit of grammatical organization","A contract clause."),
    ("clay","noun","a stiff sticky earth","Modeling clay."),
    ("cleanse","verb","make thoroughly clean","Cleanse the skin."),
    ("click","verb","press a button on a mouse","Click the link."),
    ("client","noun","a person using professional services","A valued client."),
    ("cliff","noun","a steep rock face","A cliff edge."),
    ("climate","noun","the weather conditions in an area","Climate change."),
    ("climb","verb","go or come up","Climb the ladder."),
    ("clinic","noun","a place for medical treatment","A dental clinic."),
    ("clinical","adjective","relating to the observation of patients","Clinical trials."),
    ("clip","noun","a device for holding things together","A paper clip."),
    ("cloak","noun","a sleeveless outdoor garment","Under the cloak of darkness."),
    ("clone","noun","an organism genetically identical to another","A human clone."),
    ("closet","noun","a small room or cupboard","Come out of the closet."),
    ("closure","noun","an act of closing something","Road closure."),
    ("cloth","noun","woven fabric","A table cloth."),
    ("clothing","noun","items worn to cover the body","Warm clothing."),
    ("cluster","noun","a group of similar things close together","A cluster of stars."),
    ("clutch","verb","grasp something tightly","Clutch at straws."),
    ("clutter","noun","a collection of things lying about","Clear the clutter."),
    ("coach","noun","a person who trains athletes","A football coach."),
    ("coal","noun","a hard black mineral used as fuel","A coal mine."),
    ("coalition","noun","an alliance for combined action","Form a coalition."),
    ("coarse","adjective","rough in texture","Coarse sand."),
    ("coast","noun","the part of land near the sea","The west coast."),
    ("coastal","adjective","of or near a coast","Coastal areas."),
    ("coating","noun","a thin layer covering something","A protective coating."),
    ("cocktail","noun","an alcoholic mixed drink","A cocktail party."),
    ("code","noun","a system of words or figures","A dress code."),
    ("coerce","verb","persuade using force or threats","Coerce into agreement."),
    ("cognitive","adjective","relating to cognition","Cognitive abilities."),
    ("coherent","adjective","logical and consistent","A coherent argument."),
    ("cohesion","noun","the action of forming a united whole","Social cohesion."),
    ("coincide","verb","occur at the same time","Events coincide."),
    ("coincidence","noun","a remarkable concurrence of events","A strange coincidence."),
    ("collaborate","verb","work jointly on an activity","Collaborate on projects."),
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
