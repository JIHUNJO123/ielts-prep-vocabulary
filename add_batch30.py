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
    ("adjoin","verb","be next to and joined with","The buildings adjoin."),
    ("adjourn","verb","break off a meeting","Adjourn the session."),
    ("adjunct","noun","a thing added to something else","An adjunct to the team."),
    ("administrate","verb","manage and organize","Administrate the program."),
    ("administrator","noun","a person responsible for managing","System administrator."),
    ("admirable","adjective","arousing or deserving respect","An admirable effort."),
    ("admiral","noun","a high-ranking naval officer","Fleet admiral."),
    ("admiration","noun","respect and warm approval","Express admiration."),
    ("admire","verb","regard with respect","Admire her courage."),
    ("admissible","adjective","acceptable or valid","Admissible evidence."),
    ("admission","noun","a statement acknowledging the truth","Admission of guilt."),
    ("adolescence","noun","the period of being an adolescent","During adolescence."),
    ("adolescent","noun","a young person developing into an adult","Adolescent behavior."),
    ("adoption","noun","the action of adopting","Child adoption."),
    ("adorn","verb","make more attractive","Adorn with flowers."),
    ("adrenaline","noun","a hormone secreted in stress","Adrenaline rush."),
    ("adversary","noun","one's opponent in a conflict","A formidable adversary."),
    ("adversely","adverb","in a way that prevents success","Adversely affected."),
    ("adversity","noun","difficulties or misfortune","Overcome adversity."),
    ("advocacy","noun","public support for a cause","Environmental advocacy."),
    ("advocate","verb","publicly recommend or support","Advocate for change."),
    ("aerial","adjective","existing in the air","Aerial view."),
    ("aerobic","adjective","relating to aerobic exercise","Aerobic fitness."),
    ("aerospace","noun","the industry dealing with aircraft","Aerospace engineering."),
    ("aesthetic","adjective","concerned with beauty","Aesthetic appeal."),
    ("aesthetically","adverb","in an aesthetic manner","Aesthetically pleasing."),
    ("affable","adjective","friendly and good-natured","An affable personality."),
    ("affection","noun","a gentle feeling of fondness","Show affection."),
    ("affectionate","adjective","readily feeling or showing fondness","An affectionate gesture."),
    ("affiliate","verb","officially attach to an organization","Affiliate with a group."),
    ("affiliation","noun","the state of being affiliated","Political affiliation."),
    ("affinity","noun","a natural liking for something","An affinity for music."),
    ("affirm","verb","state as a fact","Affirm the decision."),
    ("affirmation","noun","the action of affirming something","Positive affirmation."),
    ("afflict","verb","cause pain or suffering to","Afflicted by disease."),
    ("affluence","noun","the state of having a great deal of money","Growing affluence."),
    ("affluent","adjective","having a great deal of money","An affluent neighborhood."),
    ("affront","noun","an action causing offense","A personal affront."),
    ("aftermath","noun","the consequences of an event","In the aftermath of."),
    ("aggravate","verb","make worse or more serious","Aggravate the situation."),
    ("aggregate","noun","a whole formed by combining elements","In aggregate."),
    ("aggression","noun","hostile or violent behavior","Military aggression."),
    ("aggressive","adjective","ready to attack or confront","Aggressive marketing."),
    ("agile","adjective","able to move quickly and easily","An agile mind."),
    ("agility","noun","ability to move quickly","Physical agility."),
    ("agitate","verb","make someone troubled","Agitate for reform."),
    ("agitation","noun","a state of anxiety","Political agitation."),
    ("agonize","verb","undergo great mental anguish","Agonize over decisions."),
    ("agony","noun","extreme physical or mental suffering","In agony."),
    ("agrarian","adjective","relating to cultivated land","Agrarian reform."),
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
