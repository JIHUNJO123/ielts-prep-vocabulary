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
    ("willingness","noun","the quality of being prepared to do something","Show willingness."),
    ("win","verb","be successful in a contest","Win the game."),
    ("wind","noun","air in motion","Strong wind."),
    ("window","noun","an opening in a wall","Look out the window."),
    ("winner","noun","a person who wins","The winner takes all."),
    ("winter","noun","the coldest season","Cold winter."),
    ("wipe","verb","clean by rubbing","Wipe the surface."),
    ("wire","noun","metal drawn out into thin flexible thread","Electric wire."),
    ("wisdom","noun","the quality of having experience and knowledge","Words of wisdom."),
    ("wise","adjective","having experience and knowledge","A wise decision."),
    ("wish","verb","feel or express a strong desire","Wish for success."),
    ("withdraw","verb","remove or take away","Withdraw money."),
    ("withdrawal","noun","the action of withdrawing","Cash withdrawal."),
    ("within","preposition","inside the limits of","Within reach."),
    ("without","preposition","in the absence of","Without help."),
    ("witness","noun","a person who sees an event","An eyewitness."),
    ("woman","noun","an adult female human","A young woman."),
    ("wonder","verb","desire to know something","Wonder about."),
    ("wonderful","adjective","inspiring delight","A wonderful experience."),
    ("wood","noun","the hard fibrous material of trees","Made of wood."),
    ("wooden","adjective","made of wood","Wooden furniture."),
    ("word","noun","a single unit of language","New words."),
    ("work","noun","activity involving effort","Hard work."),
    ("worker","noun","a person who works","Office worker."),
    ("workforce","noun","the people engaged in work","Skilled workforce."),
    ("working","adjective","having paid employment","Working conditions."),
    ("workplace","noun","a place where people work","Modern workplace."),
    ("workshop","noun","a meeting for discussion","Training workshop."),
    ("world","noun","the earth with all its countries","Around the world."),
    ("worldwide","adjective","throughout the world","Worldwide distribution."),
    ("worried","adjective","anxious or troubled","Worried about."),
    ("worry","verb","feel anxious","Don't worry."),
    ("worse","adjective","of poorer quality","Getting worse."),
    ("worsen","verb","make or become worse","Conditions worsen."),
    ("worst","adjective","most bad or unpleasant","The worst case."),
    ("worth","adjective","equivalent in value to","Worth the effort."),
    ("worthwhile","adjective","worth the time or effort","A worthwhile investment."),
    ("worthy","adjective","deserving effort or attention","A worthy cause."),
    ("wound","noun","an injury to living tissue","Deep wound."),
    ("wrap","verb","cover or enclose","Wrap a gift."),
    ("wreck","verb","destroy or badly damage","Wreck the plan."),
    ("write","verb","mark letters on a surface","Write a letter."),
    ("writer","noun","a person who writes","A famous writer."),
    ("writing","noun","the activity of composing text","Academic writing."),
    ("written","adjective","expressed in writing","Written agreement."),
    ("wrong","adjective","not correct or true","Wrong answer."),
    ("yard","noun","a unit of measurement","A few yards away."),
    ("year","noun","the period of 365 days","Last year."),
    ("yearly","adjective","happening once a year","Yearly report."),
    ("yellow","adjective","of a bright color","Yellow flowers."),
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
