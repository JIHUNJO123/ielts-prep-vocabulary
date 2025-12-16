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
    ("competence","noun","the ability to do something successfully","Professional competence."),
    ("competent","adjective","having the necessary ability","A competent worker."),
    ("competition","noun","the activity of competing","Fierce competition."),
    ("competitive","adjective","having a strong desire to win","A competitive market."),
    ("competitor","noun","a person who takes part in competition","A major competitor."),
    ("compile","verb","produce by assembling information","Compile a report."),
    ("complacent","adjective","smugly satisfied","Don't be complacent."),
    ("complain","verb","express dissatisfaction","Complain about service."),
    ("complaint","noun","an expression of dissatisfaction","File a complaint."),
    ("complement","verb","add to so as to improve","Complement each other."),
    ("complementary","adjective","combining to enhance qualities","Complementary skills."),
    ("complete","adjective","having all necessary parts","A complete set."),
    ("completion","noun","the action of completing","Project completion."),
    ("complexity","noun","the state of being complex","The complexity of the issue."),
    ("compliance","noun","the action of complying","Regulatory compliance."),
    ("compliant","adjective","meeting rules or standards","Fully compliant."),
    ("complicate","verb","make more difficult","Don't complicate things."),
    ("complicated","adjective","consisting of many parts","A complicated process."),
    ("complication","noun","a circumstance that complicates","Medical complications."),
    ("compliment","noun","a polite expression of praise","Pay a compliment."),
    ("comply","verb","act in accordance with a wish","Comply with regulations."),
    ("component","noun","a part of a larger whole","Key components."),
    ("compose","verb","write or create","Compose music."),
    ("composer","noun","a person who writes music","A famous composer."),
    ("composite","adjective","made up of various parts","A composite material."),
    ("composition","noun","the nature of something's ingredients","Chemical composition."),
    ("compound","noun","a thing composed of two or more elements","A chemical compound."),
    ("comprehensive","adjective","complete and including everything","A comprehensive guide."),
    ("compress","verb","flatten by pressure","Compress data."),
    ("comprise","verb","consist of or be made up of","The team comprises experts."),
    ("compromise","noun","an agreement reached by concession","Reach a compromise."),
    ("compulsory","adjective","required by law","Compulsory education."),
    ("compute","verb","calculate or reckon","Compute the total."),
    ("conceal","verb","keep from sight","Conceal evidence."),
    ("concede","verb","admit that something is true","Concede defeat."),
    ("conceive","verb","form a concept in the mind","Conceive an idea."),
    ("concentrate","verb","focus attention","Concentrate on work."),
    ("concentration","noun","the action of concentrating","Lack of concentration."),
    ("conception","noun","the forming of a concept","From conception to completion."),
    ("concern","noun","anxiety or worry","A cause for concern."),
    ("concerned","adjective","worried or anxious","Deeply concerned."),
    ("concerning","preposition","about or regarding","Concerning this matter."),
    ("concert","noun","a musical performance","A rock concert."),
    ("concession","noun","a thing that is granted","Make concessions."),
    ("conclude","verb","bring to an end","Conclude the meeting."),
    ("conclusion","noun","the end or finish of something","In conclusion."),
    ("concrete","adjective","existing in material form","Concrete evidence."),
    ("condemn","verb","express complete disapproval","Condemn violence."),
    ("condense","verb","make denser or more concentrated","Condense the report."),
    ("condition","noun","the state of something","In good condition."),
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
