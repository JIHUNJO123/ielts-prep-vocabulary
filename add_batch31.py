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
    ("ailment","noun","an illness","A minor ailment."),
    ("airborne","adjective","transported by air","Airborne particles."),
    ("aisle","noun","a passage between rows","Walk down the aisle."),
    ("akin","adjective","of similar character","Akin to a miracle."),
    ("albeit","conjunction","although","Albeit difficult."),
    ("album","noun","a collection of recordings","Music album."),
    ("alert","adjective","quick to notice","Stay alert."),
    ("alertness","noun","the quality of being alert","Mental alertness."),
    ("alias","noun","a false name","Known by an alias."),
    ("alien","adjective","belonging to a foreign country","Alien concepts."),
    ("alienate","verb","cause to feel isolated","Alienate customers."),
    ("alienation","noun","the state of being alienated","Social alienation."),
    ("align","verb","place in a straight line","Align with goals."),
    ("alignment","noun","arrangement in a straight line","Strategic alignment."),
    ("alike","adjective","similar to each other","Look alike."),
    ("allay","verb","diminish fears or suspicions","Allay concerns."),
    ("allegation","noun","a claim without proof","Serious allegations."),
    ("allege","verb","claim something without proof","Allege misconduct."),
    ("alleged","adjective","said without proof","The alleged crime."),
    ("allegedly","adverb","used to convey that something is claimed","Allegedly involved."),
    ("allegiance","noun","loyalty to a person or group","Pledge allegiance."),
    ("allergic","adjective","caused by an allergy","Allergic reaction."),
    ("allergy","noun","a damaging immune response","Food allergy."),
    ("alleviate","verb","make suffering less severe","Alleviate pain."),
    ("alliance","noun","a union for mutual benefit","Form an alliance."),
    ("allied","adjective","joined by an alliance","Allied forces."),
    ("allocate","verb","distribute for a particular purpose","Allocate resources."),
    ("allocation","noun","the action of allocating","Budget allocation."),
    ("allot","verb","give or apportion","Allot time."),
    ("allotment","noun","an amount allocated","Monthly allotment."),
    ("allowance","noun","a sum of money allowed","Travel allowance."),
    ("allude","verb","suggest or call attention to indirectly","Allude to problems."),
    ("allure","noun","the quality of being attractive","The allure of fame."),
    ("allusion","noun","an indirect reference","A literary allusion."),
    ("ally","noun","a person or organization that cooperates","A political ally."),
    ("almanac","noun","an annual calendar with information","Farmer's almanac."),
    ("almighty","adjective","having complete power","Almighty power."),
    ("alter","verb","change or cause to change","Alter the plan."),
    ("alteration","noun","the action of altering","Make alterations."),
    ("alternate","verb","occur in turn repeatedly","Alternate between."),
    ("alternating","adjective","occurring by turns","Alternating current."),
    ("alternative","noun","one of two or more choices","An alternative option."),
    ("alternatively","adverb","as another option","Alternatively available."),
    ("altitude","noun","the height above sea level","High altitude."),
    ("altogether","adverb","completely","Altogether different."),
    ("aluminium","noun","a silvery-white metal","Aluminium foil."),
    ("amateur","noun","a person who engages in an activity for pleasure","Amateur photographer."),
    ("amaze","verb","surprise greatly","Amaze everyone."),
    ("amazed","adjective","greatly surprised","Completely amazed."),
    ("amazement","noun","a feeling of great surprise","Look on in amazement."),
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
