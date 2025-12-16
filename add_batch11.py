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
    ("confess","verb","admit that one has committed a crime","Confess guilt."),
    ("confession","noun","a formal statement admitting guilt","Make a confession."),
    ("confidence","noun","the feeling of self-assurance","Build confidence."),
    ("confident","adjective","feeling certain about something","Confident in success."),
    ("confidential","adjective","intended to be kept secret","Confidential information."),
    ("confine","verb","keep within certain limits","Confined to bed."),
    ("confirm","verb","establish the truth of","Confirm the booking."),
    ("confirmation","noun","the action of confirming","Await confirmation."),
    ("conflict","noun","a serious disagreement","Armed conflict."),
    ("conform","verb","comply with rules","Conform to standards."),
    ("confront","verb","meet face to face","Confront the problem."),
    ("confrontation","noun","a hostile meeting","Avoid confrontation."),
    ("confuse","verb","make unclear","Don't confuse the issue."),
    ("confusion","noun","lack of understanding","Cause confusion."),
    ("congratulate","verb","give someone good wishes","Congratulate the winner."),
    ("congregation","noun","a group of people assembled for worship","The congregation gathered."),
    ("congress","noun","a national legislative body","The US Congress."),
    ("conjunction","noun","a word used to connect clauses","A conjunction of events."),
    ("connect","verb","bring together or into contact","Connect the cables."),
    ("connection","noun","a relationship in which things are linked","A strong connection."),
    ("conquer","verb","overcome and take control of","Conquer fears."),
    ("conquest","noun","the act of conquering","Military conquest."),
    ("conscience","noun","a person's moral sense of right and wrong","A guilty conscience."),
    ("conscious","adjective","aware of one's surroundings","Fully conscious."),
    ("consciousness","noun","the state of being awake and aware","Lose consciousness."),
    ("consecutive","adjective","following continuously","Three consecutive wins."),
    ("consensus","noun","a general agreement","Reach consensus."),
    ("consent","noun","permission for something to happen","Give consent."),
    ("consequence","noun","a result or effect of an action","Face the consequences."),
    ("consequent","adjective","following as a result","Consequent effects."),
    ("consequently","adverb","as a result","Consequently failed."),
    ("conservation","noun","prevention of wasteful use","Wildlife conservation."),
    ("conservative","adjective","holding to traditional attitudes","A conservative estimate."),
    ("conserve","verb","protect from harm or destruction","Conserve energy."),
    ("consider","verb","think carefully about","Consider the options."),
    ("considerable","adjective","notably large","A considerable amount."),
    ("considerably","adverb","to a notable degree","Considerably improved."),
    ("considerate","adjective","careful not to cause inconvenience","Be considerate."),
    ("consideration","noun","careful thought","Take into consideration."),
    ("consist","verb","be composed of","Consists of three parts."),
    ("consistency","noun","the quality of being consistent","Maintain consistency."),
    ("consistent","adjective","unchanging in achievement","Consistent performance."),
    ("consolidate","verb","combine into a single unit","Consolidate power."),
    ("conspiracy","noun","a secret plan to do something unlawful","A conspiracy theory."),
    ("constant","adjective","occurring continuously","Constant pressure."),
    ("constantly","adverb","continuously over a period","Constantly improving."),
    ("constitute","verb","be a part of a whole","Constitute a majority."),
    ("constitution","noun","a body of fundamental principles","The Constitution."),
    ("constitutional","adjective","relating to a constitution","Constitutional rights."),
    ("constraint","noun","a limitation or restriction","Budget constraints."),
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
