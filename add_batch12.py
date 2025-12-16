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
    ("construct","verb","build or erect","Construct a building."),
    ("construction","noun","the action of building","Under construction."),
    ("constructive","adjective","serving a useful purpose","Constructive criticism."),
    ("consult","verb","seek information or advice","Consult a doctor."),
    ("consultant","noun","a person who provides expert advice","A management consultant."),
    ("consultation","noun","the action of consulting","Public consultation."),
    ("consume","verb","eat or drink","Consume energy."),
    ("consumer","noun","a person who purchases goods","Consumer protection."),
    ("consumption","noun","the action of using up a resource","Fuel consumption."),
    ("contact","noun","the state of communication","Make contact."),
    ("contain","verb","have or hold within","Contains vitamins."),
    ("container","noun","an object for holding something","A shipping container."),
    ("contaminate","verb","make impure","Contaminate the water."),
    ("contamination","noun","the action of making impure","Environmental contamination."),
    ("contemplate","verb","look thoughtfully for a long time","Contemplate the future."),
    ("contemporary","adjective","living or occurring at the same time","Contemporary art."),
    ("contempt","noun","the feeling of despising someone","Hold in contempt."),
    ("contend","verb","struggle to surmount","Contend with problems."),
    ("content","noun","things included","The content of the book."),
    ("contented","adjective","happy and at ease","A contented life."),
    ("contest","noun","an event in which people compete","A beauty contest."),
    ("context","noun","the circumstances forming a background","In this context."),
    ("continent","noun","a continuous mass of land","The European continent."),
    ("continental","adjective","forming or belonging to a continent","Continental drift."),
    ("continual","adjective","constantly occurring","Continual improvement."),
    ("continuation","noun","the action of continuing","A continuation of the story."),
    ("continue","verb","persist in an activity","Continue working."),
    ("continuous","adjective","forming an unbroken whole","Continuous improvement."),
    ("contract","noun","a written agreement","Sign a contract."),
    ("contractor","noun","a person who undertakes a contract","A building contractor."),
    ("contradict","verb","deny the truth of a statement","Contradict oneself."),
    ("contradiction","noun","a combination of statements that are opposed","A direct contradiction."),
    ("contrary","adjective","opposite in nature","On the contrary."),
    ("contrast","noun","the state of being strikingly different","In contrast."),
    ("contribute","verb","give something to help achieve","Contribute to society."),
    ("contribution","noun","a gift or payment to a common fund","Make a contribution."),
    ("contributor","noun","a person who contributes something","A major contributor."),
    ("controversial","adjective","giving rise to public disagreement","A controversial issue."),
    ("controversy","noun","prolonged public disagreement","Cause controversy."),
    ("convenience","noun","the state of being able to proceed without difficulty","For convenience."),
    ("convenient","adjective","fitting in well with needs","A convenient location."),
    ("convention","noun","a way in which something is usually done","Social conventions."),
    ("conventional","adjective","based on or in accordance with convention","Conventional methods."),
    ("converge","verb","come together from different directions","Paths converge."),
    ("conversation","noun","a talk between people","A casual conversation."),
    ("conversion","noun","the process of changing","Energy conversion."),
    ("convert","verb","change the form or function of","Convert to digital."),
    ("convey","verb","transport or carry to a place","Convey a message."),
    ("conviction","noun","a formal declaration of guilt","A strong conviction."),
    ("convince","verb","cause to believe firmly","Convince others."),
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
