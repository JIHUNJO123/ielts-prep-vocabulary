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
    ("cemetery","noun","a burial ground","A quiet cemetery."),
    ("census","noun","an official count of a population","National census."),
    ("centennial","adjective","relating to a hundredth anniversary","Centennial celebration."),
    ("ceramic","adjective","made of clay","Ceramic tiles."),
    ("cereal","noun","a grass producing edible grain","Breakfast cereal."),
    ("ceremony","noun","a formal religious or public occasion","Wedding ceremony."),
    ("certainty","noun","firm conviction","With certainty."),
    ("certificate","noun","an official document","A birth certificate."),
    ("certification","noun","the action of certifying","Professional certification."),
    ("chain","noun","a series of linked metal rings","A food chain."),
    ("chair","noun","a seat for one person","The chair of the meeting."),
    ("chalk","noun","a soft white limestone","A chalk board."),
    ("chamber","noun","a large room for formal events","The chamber of commerce."),
    ("champion","noun","a person who has won a competition","World champion."),
    ("championship","noun","a contest for the position of champion","The world championship."),
    ("chaos","noun","complete disorder","Total chaos."),
    ("chapel","noun","a small church","A wedding chapel."),
    ("chapter","noun","a main division of a book","Chapter one."),
    ("characteristic","noun","a feature typical of someone","Key characteristics."),
    ("characterize","verb","describe the distinctive nature","Characterize the problem."),
    ("charity","noun","an organization helping those in need","Give to charity."),
    ("charm","noun","the power of delighting others","Personal charm."),
    ("charter","noun","a written grant of rights","A royal charter."),
    ("chase","verb","pursue in order to catch","Chase dreams."),
    ("chat","verb","talk in a friendly informal way","Chat online."),
    ("cheat","verb","act dishonestly to gain an advantage","Cheat on a test."),
    ("chef","noun","a professional cook","A master chef."),
    ("chemistry","noun","the science of substances","Organic chemistry."),
    ("cherish","verb","protect and care for lovingly","Cherish memories."),
    ("chest","noun","the front surface of the body","Chest pain."),
    ("chew","verb","bite and work food in the mouth","Chew carefully."),
    ("chicken","noun","a domestic fowl","Fried chicken."),
    ("chief","adjective","most important","The chief concern."),
    ("chill","verb","make cold","Chill the wine."),
    ("chimney","noun","a vertical structure for smoke","A brick chimney."),
    ("chin","noun","the protruding part below the mouth","Keep your chin up."),
    ("chip","noun","a small piece broken off","A computer chip."),
    ("choir","noun","an organized group of singers","A church choir."),
    ("choke","verb","have difficulty breathing","Choke on food."),
    ("chord","noun","a group of notes sounded together","Strike a chord."),
    ("chore","noun","a routine task","Daily chores."),
    ("chronic","adjective","persisting for a long time","Chronic pain."),
    ("chronicle","noun","a factual written account","A historical chronicle."),
    ("chunk","noun","a thick solid piece","A chunk of cheese."),
    ("circuit","noun","a roughly circular line","An electrical circuit."),
    ("circular","adjective","having the form of a circle","A circular argument."),
    ("circulate","verb","move or cause to move continuously","Circulate the memo."),
    ("circulation","noun","movement in a circle","Blood circulation."),
    ("circumstance","noun","a fact or condition connected with an event","Under the circumstances."),
    ("cite","verb","quote as evidence","Cite sources."),
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
