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

# 완전히 새로운 단어들로 대체
NEW_WORDS = [
    ("deceive","verb","cause someone to believe something false","Deceive the enemy."),
    ("decent","adjective","conforming with accepted standards","A decent salary."),
    ("decisive","adjective","settling an issue","A decisive victory."),
    ("declaration","noun","a formal statement","A declaration of independence."),
    ("declare","verb","announce openly","Declare war."),
    ("decline","verb","politely refuse","Decline an offer."),
    ("decompose","verb","become rotten","Decompose naturally."),
    ("decorate","verb","make more attractive","Decorate the room."),
    ("decoration","noun","the process of decorating","Interior decoration."),
    ("decrease","verb","make or become smaller","Decrease expenses."),
    ("dedicate","verb","devote time to a task","Dedicate resources."),
    ("dedication","noun","the quality of being dedicated","Show dedication."),
    ("deduct","verb","subtract or take away","Deduct taxes."),
    ("deed","noun","an action that is performed","A good deed."),
    ("deem","verb","regard or consider","Deem necessary."),
    ("deepen","verb","make or become deeper","Deepen understanding."),
    ("deer","noun","a hoofed mammal","A wild deer."),
    ("default","noun","failure to fulfill an obligation","By default."),
    ("defeat","verb","win a victory over","Defeat the opponent."),
    ("defect","noun","a shortcoming or imperfection","A manufacturing defect."),
    ("defence","noun","the action of defending","Self defence."),
    ("defend","verb","resist an attack","Defend the title."),
    ("defendant","noun","a person accused in a lawsuit","The defendant pleaded."),
    ("defender","noun","a person who defends","A public defender."),
    ("defensive","adjective","used or intended to defend","A defensive strategy."),
    ("defer","verb","put off to a later time","Defer payment."),
    ("deficiency","noun","a lack or shortage","Vitamin deficiency."),
    ("deficient","adjective","not having enough","Deficient in iron."),
    ("deficit","noun","the amount by which something falls short","Budget deficit."),
    ("define","verb","state the meaning of","Define the term."),
    ("definite","adjective","clearly stated or decided","A definite answer."),
    ("definitely","adverb","without doubt","Definitely agree."),
    ("definition","noun","a statement of the meaning","By definition."),
    ("defy","verb","openly resist or refuse to obey","Defy expectations."),
    ("degrade","verb","treat with disrespect","Degrade the environment."),
    ("degree","noun","the amount or level of something","To some degree."),
    ("delay","verb","make late or slow","Delay departure."),
    ("delegate","verb","entrust to another person","Delegate authority."),
    ("delegation","noun","a body of delegates","The delegation arrived."),
    ("delete","verb","remove or obliterate","Delete the file."),
    ("deliberate","adjective","done consciously and intentionally","A deliberate act."),
    ("deliberately","adverb","consciously and intentionally","Deliberately ignored."),
    ("delicate","adjective","very fine in texture","A delicate matter."),
    ("delight","noun","great pleasure","A source of delight."),
    ("deliver","verb","bring and hand over","Deliver goods."),
    ("delivery","noun","the action of delivering","Free delivery."),
    ("demand","noun","an insistent request","Meet demand."),
    ("demanding","adjective","requiring much skill","A demanding job."),
    ("democracy","noun","a system of government by the people","A stable democracy."),
    ("democrat","noun","a person who believes in democracy","A true democrat."),
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
