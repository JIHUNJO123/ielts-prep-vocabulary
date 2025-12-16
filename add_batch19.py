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
    ("dull","adjective","lacking brightness","A dull color."),
    ("duly","adverb","in accordance with what is required","Duly noted."),
    ("dumb","adjective","unable to speak","Struck dumb."),
    ("dump","verb","deposit or dispose of carelessly","Dump waste."),
    ("dune","noun","a mound of sand","A sand dune."),
    ("duration","noun","the time during which something continues","The duration of the course."),
    ("during","preposition","throughout the course of","During the meeting."),
    ("dusk","noun","the darker stage of twilight","At dusk."),
    ("dust","noun","fine dry powder","Gather dust."),
    ("dusty","adjective","covered with dust","A dusty road."),
    ("duty","noun","a moral or legal obligation","A sense of duty."),
    ("dwarf","noun","a person of unusually small stature","A garden dwarf."),
    ("dwell","verb","live in a place","Dwell on the past."),
    ("dwelling","noun","a house or place of residence","A permanent dwelling."),
    ("dye","noun","a substance used to add color","Hair dye."),
    ("dynamic","adjective","characterized by constant change","A dynamic environment."),
    ("dynamics","noun","the branch of mechanics concerned with motion","Group dynamics."),
    ("dynasty","noun","a line of hereditary rulers","A royal dynasty."),
    ("eagle","noun","a large bird of prey","A bald eagle."),
    ("ear","noun","the organ of hearing","Lend an ear."),
    ("earn","verb","obtain money in return for labor or services","Earn respect."),
    ("earnest","adjective","resulting from sincere intention","An earnest effort."),
    ("earth","noun","the planet on which we live","Planet Earth."),
    ("earthquake","noun","a sudden violent shaking of the ground","A major earthquake."),
    ("ease","verb","make less serious","Ease the pain."),
    ("easily","adverb","without difficulty","Easily understood."),
    ("east","noun","the direction toward the point of the horizon where the sun rises","The Far East."),
    ("eastern","adjective","situated in or facing the east","Eastern Europe."),
    ("easy","adjective","achieved without great effort","An easy task."),
    ("eat","verb","put food into the mouth and chew","Eat healthily."),
    ("echo","noun","a sound repeated by reflection","An echo of the past."),
    ("eclipse","noun","an obscuring of light from one celestial body","A solar eclipse."),
    ("ecological","adjective","relating to ecology","Ecological balance."),
    ("ecology","noun","the branch of biology dealing with organisms","Marine ecology."),
    ("economic","adjective","relating to economics or the economy","Economic growth."),
    ("economical","adjective","giving good value in relation to money spent","An economical car."),
    ("economics","noun","the branch of knowledge concerned with production","Study economics."),
    ("economist","noun","an expert in economics","A leading economist."),
    ("economy","noun","the state of a country in terms of production","A strong economy."),
    ("ecosystem","noun","a biological community of interacting organisms","A fragile ecosystem."),
    ("edge","noun","the outside limit of an object","On the edge."),
    ("edit","verb","prepare written material for publication","Edit the document."),
    ("edition","noun","a particular form of a book","First edition."),
    ("editor","noun","a person who edits material for publication","The chief editor."),
    ("editorial","noun","a newspaper article giving an opinion","An editorial piece."),
    ("educate","verb","give intellectual or moral instruction","Educate children."),
    ("educated","adjective","having been educated","Highly educated."),
    ("education","noun","the process of receiving instruction","Higher education."),
    ("educational","adjective","relating to education","Educational resources."),
    ("educator","noun","a person who provides instruction","A dedicated educator."),
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
