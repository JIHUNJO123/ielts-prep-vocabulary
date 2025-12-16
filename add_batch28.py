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
    ("yesterday","adverb","on the day before today","I saw him yesterday."),
    ("yet","adverb","up until now","Not finished yet."),
    ("yield","verb","produce or provide","Yield results."),
    ("young","adjective","having lived for only a short time","Young people."),
    ("youngster","noun","a child or young person","Local youngsters."),
    ("youth","noun","the period between childhood and adulthood","In his youth."),
    ("youthful","adjective","young or seeming young","Youthful energy."),
    ("zeal","noun","great energy in pursuit of an objective","Work with zeal."),
    ("zealous","adjective","having great energy or enthusiasm","A zealous supporter."),
    ("zenith","noun","the highest point","Reach the zenith."),
    ("zero","noun","the figure 0","Zero tolerance."),
    ("zone","noun","an area with particular characteristics","Time zone."),
    ("zoology","noun","the scientific study of animals","Study zoology."),
    ("absorption","noun","the process of absorbing","Nutrient absorption."),
    ("abstract","adjective","existing in thought only","Abstract concept."),
    ("abstraction","noun","the quality of dealing with ideas","Mathematical abstraction."),
    ("absurd","adjective","wildly unreasonable","An absurd idea."),
    ("abundance","noun","a very large quantity","An abundance of resources."),
    ("abundant","adjective","existing in large quantities","Abundant supply."),
    ("abuse","noun","cruel treatment","Child abuse prevention."),
    ("academic","adjective","relating to education","Academic performance."),
    ("academy","noun","a place of study or training","Military academy."),
    ("accelerate","verb","increase in speed","Accelerate growth."),
    ("acceleration","noun","increase in rate of speed","Rapid acceleration."),
    ("accent","noun","a distinctive way of pronunciation","Foreign accent."),
    ("accept","verb","agree to receive","Accept the offer."),
    ("acceptable","adjective","able to be agreed on","An acceptable solution."),
    ("acceptance","noun","the action of consenting","Gain acceptance."),
    ("accessibility","noun","the quality of being easy to reach","Improved accessibility."),
    ("accessible","adjective","able to be reached or entered","Easily accessible."),
    ("accessory","noun","a thing added to something else","Fashion accessory."),
    ("accident","noun","an unfortunate incident","Car accident."),
    ("accidental","adjective","happening by chance","Accidental discovery."),
    ("accidentally","adverb","in an unintentional way","Accidentally deleted."),
    ("accommodate","verb","provide lodging or room for","Accommodate guests."),
    ("accommodation","noun","a room or building to live in","Book accommodation."),
    ("accompany","verb","go somewhere with someone","Accompany the team."),
    ("accomplish","verb","achieve or complete successfully","Accomplish the goal."),
    ("accomplishment","noun","something achieved successfully","A major accomplishment."),
    ("accord","noun","an official agreement","Peace accord."),
    ("accordance","noun","conformity or agreement","In accordance with."),
    ("according","preposition","as stated by","According to reports."),
    ("accordingly","adverb","in a way that is appropriate","Act accordingly."),
    ("accountability","noun","the fact of being responsible","Corporate accountability."),
    ("accountable","adjective","required to explain decisions","Hold accountable."),
    ("accountant","noun","a person who keeps financial accounts","A certified accountant."),
    ("accounting","noun","the action of keeping financial records","Accounting standards."),
    ("accumulate","verb","gather together","Accumulate wealth."),
    ("accumulation","noun","the gathering of a large amount","Accumulation of data."),
    ("accuracy","noun","the quality of being correct","Data accuracy."),
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
