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
    ("annually","adverb","once a year","Meet annually."),
    ("anomaly","noun","something that deviates from normal","A statistical anomaly."),
    ("anonymous","adjective","not identified by name","Anonymous donor."),
    ("anonymously","adverb","in an anonymous manner","Submit anonymously."),
    ("antagonism","noun","active hostility","Growing antagonism."),
    ("antagonist","noun","a person who opposes","The main antagonist."),
    ("antagonize","verb","cause someone to become hostile","Antagonize opponents."),
    ("antenna","noun","a rod for receiving signals","Television antenna."),
    ("anthem","noun","a rousing or uplifting song","National anthem."),
    ("anthropology","noun","the study of human societies","Cultural anthropology."),
    ("antibiotic","noun","a medicine that inhibits bacteria","Prescribe antibiotics."),
    ("anticipate","verb","regard as probable","Anticipate problems."),
    ("anticipation","noun","the action of anticipating","In anticipation."),
    ("antidote","noun","a medicine to counteract a poison","Find an antidote."),
    ("antiquated","adjective","old-fashioned or outdated","Antiquated methods."),
    ("antique","noun","an old collectible item","Antique furniture."),
    ("antiquity","noun","the ancient past","In antiquity."),
    ("antisocial","adjective","contrary to social norms","Antisocial behavior."),
    ("anxiety","noun","a feeling of worry","Reduce anxiety."),
    ("anxious","adjective","experiencing worry","Feel anxious."),
    ("anxiously","adverb","in a manner showing worry","Wait anxiously."),
    ("apartheid","noun","a policy of racial segregation","End apartheid."),
    ("apathy","noun","lack of interest","Political apathy."),
    ("apex","noun","the top or highest part","Reach the apex."),
    ("apology","noun","an expression of regret","Offer an apology."),
    ("appalling","adjective","causing shock or dismay","Appalling conditions."),
    ("apparatus","noun","the technical equipment for an activity","Laboratory apparatus."),
    ("apparent","adjective","clearly visible or understood","Apparent contradiction."),
    ("apparently","adverb","as far as one knows","Apparently successful."),
    ("appeal","noun","a serious request for help","Make an appeal."),
    ("appealing","adjective","attractive or interesting","An appealing offer."),
    ("appearance","noun","the way someone or something looks","Physical appearance."),
    ("appendix","noun","additional matter at the end of a book","See appendix."),
    ("appetite","noun","a natural desire for food","Healthy appetite."),
    ("applaud","verb","show approval by clapping","Applaud the performance."),
    ("applause","noun","approval shown by clapping","Loud applause."),
    ("apple","noun","a round fruit","Apple tree."),
    ("appliance","noun","a device for a specific task","Kitchen appliance."),
    ("applicable","adjective","relevant or appropriate","Applicable laws."),
    ("applicant","noun","a person who applies for something","Job applicant."),
    ("application","noun","a formal request","Job application."),
    ("applied","adjective","put to practical use","Applied science."),
    ("appoint","verb","assign a job or role to","Appoint a manager."),
    ("appointed","adjective","having been assigned to a position","Newly appointed."),
    ("appointment","noun","an arrangement to meet someone","Schedule an appointment."),
    ("appraisal","noun","an assessment of something's value","Performance appraisal."),
    ("appreciate","verb","recognize the full worth of","Appreciate the effort."),
    ("appreciation","noun","recognition of the worth of something","Show appreciation."),
    ("apprehend","verb","arrest someone","Apprehend the suspect."),
    ("apprehension","noun","anxiety about the future","A sense of apprehension."),
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
