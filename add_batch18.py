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
    ("dominate","verb","have a commanding influence on","Dominate the market."),
    ("donate","verb","give money for a good cause","Donate to charity."),
    ("donation","noun","something that is given to a charity","A generous donation."),
    ("donor","noun","a person who donates something","A blood donor."),
    ("doom","noun","death, destruction, or any terrible fate","A sense of doom."),
    ("doorway","noun","an entrance to a room through a door","Stand in the doorway."),
    ("dormant","adjective","having normal functions suspended","A dormant volcano."),
    ("dose","noun","a quantity of medicine taken at one time","A daily dose."),
    ("dot","noun","a small round mark","A dot on the map."),
    ("double","adjective","consisting of two equal parts","A double portion."),
    ("doubt","noun","a feeling of uncertainty","No doubt."),
    ("doubtful","adjective","feeling uncertain about something","Highly doubtful."),
    ("dough","noun","a thick mixture of flour and liquid","Pizza dough."),
    ("download","verb","copy data from one computer to another","Download the file."),
    ("downstairs","adverb","down a flight of stairs","Go downstairs."),
    ("downtown","noun","the central area of a city","Downtown area."),
    ("downward","adjective","moving toward a lower place","A downward trend."),
    ("draft","noun","a preliminary version of a piece of writing","A first draft."),
    ("drag","verb","pull along forcefully","Drag and drop."),
    ("dragon","noun","a mythical monster like a giant reptile","A fire-breathing dragon."),
    ("drain","verb","cause liquid to run off","Drain the water."),
    ("drainage","noun","the action of draining","A drainage system."),
    ("drama","noun","a play for theater or television","A TV drama."),
    ("dramatic","adjective","sudden and striking","A dramatic change."),
    ("dramatically","adverb","in a dramatic manner","Dramatically improved."),
    ("drastic","adjective","likely to have a strong effect","Drastic measures."),
    ("draw","verb","produce a picture by making lines","Draw a conclusion."),
    ("drawback","noun","a feature that renders something less acceptable","A major drawback."),
    ("drawer","noun","a storage compartment","A desk drawer."),
    ("drawing","noun","a picture made with a pencil or pen","A detailed drawing."),
    ("dread","verb","anticipate with great fear","Dread the outcome."),
    ("dream","noun","a series of images in the mind while sleeping","A bad dream."),
    ("dress","noun","a one-piece garment for a woman","A wedding dress."),
    ("drift","verb","be carried slowly by a current","Drift apart."),
    ("drill","noun","a tool for boring holes","A power drill."),
    ("drink","verb","take liquid into the mouth","Drink water."),
    ("drip","verb","fall in small drops","Water dripping."),
    ("drive","verb","operate and control a motor vehicle","Drive safely."),
    ("driver","noun","a person who drives a vehicle","A taxi driver."),
    ("drop","verb","let fall","Drop the price."),
    ("drought","noun","a prolonged period of dry weather","A severe drought."),
    ("drown","verb","die through submersion in water","Drown in debt."),
    ("drug","noun","a medicine or other substance","A prescription drug."),
    ("drum","noun","a percussion instrument","Beat the drum."),
    ("drunk","adjective","affected by alcohol","Drunk driving."),
    ("dry","adjective","free from moisture","Dry weather."),
    ("dual","adjective","consisting of two parts","A dual purpose."),
    ("dubious","adjective","hesitating or doubting","A dubious claim."),
    ("duck","noun","a waterbird with a broad bill","A rubber duck."),
    ("due","adjective","expected at a certain time","Due tomorrow."),
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
