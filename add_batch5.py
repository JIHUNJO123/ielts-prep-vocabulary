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
    ("borough","noun","a town or district","The borough council."),
    ("botanical","adjective","relating to plants","Botanical garden."),
    ("boundary","noun","a line marking limits","Set boundaries."),
    ("bow","verb","bend the head or body","Take a bow."),
    ("bracket","noun","a category of similar things","Tax bracket."),
    ("brake","noun","a device for slowing a vehicle","Apply the brakes."),
    ("breach","noun","an act of breaking a law","A breach of contract."),
    ("breadth","noun","the distance from side to side","The breadth of knowledge."),
    ("breakdown","noun","a failure of a relationship","A mental breakdown."),
    ("breakthrough","noun","a sudden important discovery","A major breakthrough."),
    ("breed","verb","produce offspring","Breed animals."),
    ("breeze","noun","a gentle wind","A cool breeze."),
    ("bribe","noun","money offered to influence","Accept a bribe."),
    ("brick","noun","a block used for building","A brick wall."),
    ("bride","noun","a woman on her wedding day","The bride arrived."),
    ("brief","adjective","of short duration","A brief meeting."),
    ("brilliant","adjective","exceptionally talented","A brilliant idea."),
    ("brink","noun","the extreme edge","On the brink of."),
    ("brittle","adjective","hard but likely to break","Brittle bones."),
    ("broadcast","verb","transmit by radio or television","Broadcast live."),
    ("brochure","noun","a small book with information","A travel brochure."),
    ("bronze","noun","an alloy of copper and tin","A bronze medal."),
    ("browse","verb","look through casually","Browse the internet."),
    ("bruise","noun","an injury appearing as discoloration","A bad bruise."),
    ("brush","noun","an implement for cleaning","A paint brush."),
    ("brutal","adjective","savagely violent","A brutal attack."),
    ("bubble","noun","a thin sphere of liquid","A soap bubble."),
    ("bucket","noun","a cylindrical container","A bucket of water."),
    ("bud","noun","a growth on a plant","A flower bud."),
    ("buddy","noun","a close friend","My buddy."),
    ("buffer","noun","a person or thing reducing shock","A buffer zone."),
    ("bug","noun","a small insect","A software bug."),
    ("bulk","noun","the mass or size of something large","In bulk."),
    ("bulletin","noun","a short official statement","A news bulletin."),
    ("bully","verb","seek to harm weaker people","Bully others."),
    ("bump","verb","knock against something","Bump into someone."),
    ("bunch","noun","a number of things grouped together","A bunch of flowers."),
    ("bundle","noun","a collection of things tied together","A bundle of joy."),
    ("burden","noun","a heavy load","A financial burden."),
    ("bureaucracy","noun","a system of government by officials","Cut bureaucracy."),
    ("burial","noun","the act of burying a dead body","A burial site."),
    ("burst","verb","break open suddenly","Burst into tears."),
    ("bush","noun","a shrub or clump of shrubs","A rose bush."),
    ("buzz","noun","a low continuous humming sound","Create a buzz."),
    ("bypass","verb","go past or around","Bypass the problem."),
    ("cabin","noun","a small shelter","A log cabin."),
    ("cabinet","noun","a cupboard with shelves","A filing cabinet."),
    ("cable","noun","a thick rope of wire","Cable television."),
    ("cage","noun","a structure of bars for confining animals","A bird cage."),
    ("calendar","noun","a chart showing dates","Check the calendar."),
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
