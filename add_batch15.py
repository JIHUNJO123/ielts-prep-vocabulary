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
    ("detect","verb","discover the presence of","Detect problems."),
    ("detection","noun","the action of detecting","Early detection."),
    ("detective","noun","a person who investigates crimes","A private detective."),
    ("detector","noun","a device for detecting something","A smoke detector."),
    ("detention","noun","the state of being detained","Detention center."),
    ("deter","verb","discourage from doing something","Deter crime."),
    ("deteriorate","verb","become progressively worse","Health deteriorated."),
    ("determination","noun","firmness of purpose","Strong determination."),
    ("determine","verb","cause something to occur","Determine the outcome."),
    ("determined","adjective","having made a firm decision","A determined effort."),
    ("detrimental","adjective","tending to cause harm","Detrimental effects."),
    ("devastate","verb","destroy or ruin","Devastate the economy."),
    ("devastating","adjective","highly destructive","A devastating blow."),
    ("developer","noun","a person who develops something","A software developer."),
    ("developmental","adjective","concerned with development","Developmental stages."),
    ("deviation","noun","the action of departing from a norm","A deviation from plan."),
    ("device","noun","a thing made for a particular purpose","A mobile device."),
    ("devise","verb","plan or invent by careful thought","Devise a strategy."),
    ("devote","verb","give all or most of time to","Devote time to study."),
    ("devoted","adjective","very loving or loyal","A devoted fan."),
    ("devotion","noun","love, loyalty, or enthusiasm","Devotion to duty."),
    ("diagnose","verb","identify the nature of an illness","Diagnose the problem."),
    ("diagnosis","noun","the identification of an illness","A medical diagnosis."),
    ("diagram","noun","a simplified drawing","A flow diagram."),
    ("dialect","noun","a form of a language","A regional dialect."),
    ("dialogue","noun","conversation between two or more people","Open dialogue."),
    ("diameter","noun","a straight line through the center","The diameter of the circle."),
    ("diamond","noun","a precious stone","A diamond ring."),
    ("diary","noun","a book for daily records","Keep a diary."),
    ("dictate","verb","state or order authoritatively","Dictate terms."),
    ("dictator","noun","a ruler with total power","A military dictator."),
    ("dictionary","noun","a book listing words with meanings","Use a dictionary."),
    ("diet","noun","the kinds of food a person eats","A healthy diet."),
    ("dietary","adjective","relating to diet","Dietary requirements."),
    ("differ","verb","be unlike or dissimilar","Opinions differ."),
    ("differential","adjective","relating to a difference","A differential diagnosis."),
    ("differentiate","verb","recognize as different","Differentiate between options."),
    ("differently","adverb","in a different way","Think differently."),
    ("digest","verb","break down food in the body","Digest information."),
    ("digital","adjective","relating to computer technology","Digital media."),
    ("dignity","noun","the state of being worthy of honor","Human dignity."),
    ("dilemma","noun","a situation requiring a difficult choice","A moral dilemma."),
    ("dilute","verb","make thinner or weaker","Dilute the solution."),
    ("dimension","noun","a measurable extent","Three dimensions."),
    ("diminish","verb","make or become less","Diminish over time."),
    ("dine","verb","eat dinner","Dine out."),
    ("dining","noun","the activity of eating a meal","A dining room."),
    ("dinner","noun","the main meal of the day","Dinner time."),
    ("dinosaur","noun","a reptile of the Mesozoic era","A dinosaur fossil."),
    ("dioxide","noun","an oxide containing two atoms of oxygen","Carbon dioxide."),
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
