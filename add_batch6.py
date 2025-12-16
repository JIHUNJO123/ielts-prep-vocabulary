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
    ("calibrate","verb","adjust precisely","Calibrate the instrument."),
    ("calm","adjective","not showing nervousness","Stay calm."),
    ("camel","noun","a large desert animal","A camel ride."),
    ("campaign","noun","an organized course of action","Election campaign."),
    ("campus","noun","the grounds of a university","On campus."),
    ("canal","noun","an artificial waterway","The Panama Canal."),
    ("cancel","verb","decide that something will not happen","Cancel the meeting."),
    ("candid","adjective","truthful and straightforward","A candid opinion."),
    ("candidate","noun","a person who applies for a job","A strong candidate."),
    ("candle","noun","a cylinder of wax with a wick","Light a candle."),
    ("canvas","noun","a strong coarse cloth","A canvas bag."),
    ("capable","adjective","having the ability","A capable leader."),
    ("capacity","noun","the maximum amount something can contain","Full capacity."),
    ("cape","noun","a sleeveless cloak","A superhero's cape."),
    ("capital","noun","the city serving as seat of government","The capital city."),
    ("capitalism","noun","an economic system based on private ownership","Free market capitalism."),
    ("captain","noun","the person in command","Team captain."),
    ("caption","noun","a title or brief explanation","Photo caption."),
    ("captive","noun","a person who has been captured","Hold captive."),
    ("capture","verb","take into one's possession by force","Capture the moment."),
    ("carbon","noun","a chemical element","Carbon dioxide."),
    ("cardiac","adjective","relating to the heart","Cardiac arrest."),
    ("cargo","noun","goods carried by vehicle","Cargo ship."),
    ("carnival","noun","a festival with parades","The carnival parade."),
    ("carpet","noun","a floor covering","A red carpet."),
    ("carriage","noun","a four-wheeled vehicle","A horse-drawn carriage."),
    ("carrier","noun","a person or thing that carries","An aircraft carrier."),
    ("carve","verb","cut into a desired shape","Carve wood."),
    ("cascade","noun","a small waterfall","A cascade of events."),
    ("casino","noun","a building for gambling","A casino resort."),
    ("cast","verb","throw forcefully","Cast a shadow."),
    ("castle","noun","a large fortified building","A medieval castle."),
    ("casual","adjective","relaxed and unconcerned","Casual dress."),
    ("casualty","noun","a person killed or injured","War casualties."),
    ("catalog","noun","a complete list of items","A product catalog."),
    ("catastrophe","noun","an event causing great damage","A natural catastrophe."),
    ("category","noun","a class or division","A category of products."),
    ("cater","verb","provide food and drink","Cater for events."),
    ("cathedral","noun","the principal church of a diocese","A Gothic cathedral."),
    ("cattle","noun","large farm animals","Cattle farming."),
    ("caution","noun","care taken to avoid danger","Exercise caution."),
    ("cautious","adjective","careful to avoid problems","A cautious approach."),
    ("cavalry","noun","soldiers who fought on horseback","The cavalry arrived."),
    ("cease","verb","come to an end","Cease fire."),
    ("ceiling","noun","the upper surface of a room","A high ceiling."),
    ("celebrate","verb","acknowledge a happy day","Celebrate success."),
    ("celebrity","noun","a famous person","A celebrity guest."),
    ("cell","noun","the smallest structural unit of an organism","A prison cell."),
    ("cellar","noun","a room below ground level","A wine cellar."),
    ("cement","noun","a powdery substance for building","Cement the relationship."),
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
