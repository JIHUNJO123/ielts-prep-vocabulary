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
    ("empower","verb","give power or authority to","Empower employees."),
    ("empty","adjective","containing nothing","An empty room."),
    ("enable","verb","give someone the ability to do something","Enable progress."),
    ("enact","verb","make into law","Enact legislation."),
    ("encounter","verb","unexpectedly experience","Encounter problems."),
    ("encourage","verb","give support or hope to","Encourage participation."),
    ("encouragement","noun","the action of encouraging","Words of encouragement."),
    ("encyclopedia","noun","a book giving information on many subjects","An online encyclopedia."),
    ("ending","noun","an end or final part","A happy ending."),
    ("endless","adjective","having no end","Endless possibilities."),
    ("endorse","verb","declare public approval of","Endorse a product."),
    ("endorsement","noun","public approval or support","Celebrity endorsement."),
    ("endure","verb","suffer something painful","Endure hardship."),
    ("enemy","noun","a person who is hostile to another","A common enemy."),
    ("energetic","adjective","showing great activity","An energetic person."),
    ("enforce","verb","compel observance of a law","Enforce the rules."),
    ("enforcement","noun","the act of compelling observance","Law enforcement."),
    ("engage","verb","participate or become involved in","Engage in discussion."),
    ("engaged","adjective","busy or occupied","Fully engaged."),
    ("engagement","noun","a formal agreement to get married","Wedding engagement."),
    ("engine","noun","a machine with moving parts","A car engine."),
    ("engineer","noun","a person who designs or builds machines","A civil engineer."),
    ("engineering","noun","the branch of science concerned with design","Software engineering."),
    ("enhance","verb","intensify or improve","Enhance performance."),
    ("enhancement","noun","an increase or improvement","Quality enhancement."),
    ("enjoy","verb","take pleasure in","Enjoy the music."),
    ("enjoyable","adjective","giving delight or pleasure","An enjoyable experience."),
    ("enjoyment","noun","the state of taking pleasure","For your enjoyment."),
    ("enlarge","verb","make or become larger","Enlarge the photo."),
    ("enormous","adjective","very large in size","An enormous building."),
    ("enormously","adverb","to a very great degree","Enormously popular."),
    ("enough","determiner","as much as required","Enough time."),
    ("enquiry","noun","an act of asking for information","Make an enquiry."),
    ("enrich","verb","improve the quality of","Enrich the experience."),
    ("enroll","verb","officially register","Enroll in a course."),
    ("enrollment","noun","the action of enrolling","School enrollment."),
    ("ensure","verb","make certain that something happens","Ensure safety."),
    ("enter","verb","come or go into","Enter the building."),
    ("enterprise","noun","a project or undertaking","A business enterprise."),
    ("entertain","verb","provide with amusement","Entertain guests."),
    ("entertainer","noun","a person who entertains others","A famous entertainer."),
    ("entertaining","adjective","providing amusement","An entertaining show."),
    ("entertainment","noun","the action of entertaining","Live entertainment."),
    ("enthusiasm","noun","intense enjoyment and interest","Show enthusiasm."),
    ("enthusiast","noun","a person who is very interested in something","A car enthusiast."),
    ("enthusiastic","adjective","having intense enjoyment","An enthusiastic response."),
    ("entire","adjective","with no part left out","The entire population."),
    ("entirely","adverb","completely","Entirely different."),
    ("entitle","verb","give a right to","Entitled to benefits."),
    ("entity","noun","a thing with distinct existence","A separate entity."),
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
