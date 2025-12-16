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
    ("video","noun","the recording of moving visual images","Video recording."),
    ("view","noun","a particular way of considering something","Point of view."),
    ("viewer","noun","a person watching television","Television viewer."),
    ("viewpoint","noun","a particular attitude","Different viewpoint."),
    ("vigorous","adjective","strong and healthy","Vigorous exercise."),
    ("village","noun","a small community","A rural village."),
    ("violate","verb","break or fail to comply with","Violate the rules."),
    ("violation","noun","the action of violating","A violation of rights."),
    ("violence","noun","behavior involving physical force","Acts of violence."),
    ("violent","adjective","using physical force to cause harm","Violent crime."),
    ("virtual","adjective","almost or nearly as described","Virtual reality."),
    ("virtually","adverb","nearly or almost","Virtually impossible."),
    ("virtue","noun","behavior showing high moral standards","The virtue of patience."),
    ("virus","noun","an infective agent","Computer virus."),
    ("visibility","noun","the state of being able to see","Poor visibility."),
    ("visible","adjective","able to be seen","Clearly visible."),
    ("vision","noun","the ability to see","Clear vision."),
    ("visit","verb","go to see and spend time with","Visit friends."),
    ("visitor","noun","a person visiting someone","A regular visitor."),
    ("visual","adjective","relating to seeing","Visual arts."),
    ("vital","adjective","absolutely necessary","Vital information."),
    ("vitality","noun","the state of being strong and active","Full of vitality."),
    ("vivid","adjective","producing strong mental images","A vivid description."),
    ("vocabulary","noun","the body of words used in a language","Expand vocabulary."),
    ("vocal","adjective","relating to the voice","Vocal cords."),
    ("voice","noun","the sound produced in speech","Raise your voice."),
    ("volatile","adjective","liable to change rapidly","Volatile markets."),
    ("volume","noun","the amount of space occupied","Volume of sales."),
    ("voluntary","adjective","done of one's own free will","Voluntary work."),
    ("volunteer","noun","a person who freely offers to do something","A volunteer worker."),
    ("vote","noun","a formal indication of choice","Cast a vote."),
    ("voter","noun","a person who votes","Registered voter."),
    ("vulnerable","adjective","susceptible to harm","Vulnerable population."),
    ("wage","noun","a fixed regular payment for work","Minimum wage."),
    ("wait","verb","stay where one is until something happens","Wait for the bus."),
    ("wake","verb","emerge from a state of sleep","Wake up early."),
    ("walk","verb","move at a regular pace by lifting feet","Walk to school."),
    ("wall","noun","a vertical structure","Brick wall."),
    ("wander","verb","walk or move in a leisurely way","Wander around."),
    ("want","verb","have a desire to possess","Want success."),
    ("war","noun","a state of armed conflict","World war."),
    ("warehouse","noun","a large building for storing goods","Storage warehouse."),
    ("warm","adjective","of moderate high temperature","Warm weather."),
    ("warmth","noun","the quality of being warm","Human warmth."),
    ("warn","verb","inform someone of a danger","Warn of risks."),
    ("warning","noun","a statement that something bad may happen","Early warning."),
    ("warrant","verb","justify or necessitate","Warrant attention."),
    ("warranty","noun","a written guarantee","Product warranty."),
    ("waste","noun","unwanted or unusable material","Waste management."),
    ("watch","verb","look at attentively","Watch television."),
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
