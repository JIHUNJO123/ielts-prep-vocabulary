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
    ("displacement","noun","the moving of something from its place","Population displacement."),
    ("display","verb","make visible","Display artwork."),
    ("disposal","noun","the action of getting rid of something","Waste disposal."),
    ("dispose","verb","get rid of by throwing away","Dispose of waste."),
    ("disposition","noun","a person's inherent qualities","A cheerful disposition."),
    ("dispute","noun","a disagreement or argument","A legal dispute."),
    ("disregard","verb","pay no attention to","Disregard the rules."),
    ("disrupt","verb","interrupt by causing a disturbance","Disrupt services."),
    ("disruption","noun","disturbance that interrupts","Cause disruption."),
    ("dissatisfaction","noun","lack of satisfaction","Express dissatisfaction."),
    ("dissolve","verb","become incorporated into a liquid","Dissolve the company."),
    ("distance","noun","the amount of space between two places","A short distance."),
    ("distant","adjective","far away in space or time","A distant memory."),
    ("distinct","adjective","recognizably different","A distinct flavor."),
    ("distinction","noun","a difference between similar things","Make a distinction."),
    ("distinctive","adjective","characteristic of one person or thing","A distinctive style."),
    ("distinguish","verb","recognize as different","Distinguish between."),
    ("distinguished","adjective","successful and respected","A distinguished career."),
    ("distort","verb","pull out of shape","Distort the facts."),
    ("distortion","noun","the action of distorting","Visual distortion."),
    ("distract","verb","prevent from concentrating","Easily distracted."),
    ("distraction","noun","a thing that prevents concentration","A major distraction."),
    ("distress","noun","extreme anxiety or sorrow","In distress."),
    ("distribute","verb","give shares to a number of recipients","Distribute equally."),
    ("distribution","noun","the action of sharing out","Income distribution."),
    ("distributor","noun","an agent who supplies goods","A local distributor."),
    ("district","noun","an area of a country or city","A business district."),
    ("disturb","verb","interfere with the normal arrangement","Do not disturb."),
    ("disturbance","noun","the interruption of a settled condition","A public disturbance."),
    ("ditch","noun","a narrow channel dug in the ground","Jump the ditch."),
    ("dive","verb","plunge headfirst into water","Dive deep."),
    ("diverse","adjective","showing a great deal of variety","A diverse population."),
    ("diversify","verb","make or become more diverse","Diversify investments."),
    ("diversity","noun","a range of different things","Cultural diversity."),
    ("divert","verb","cause to change course","Divert attention."),
    ("divide","verb","separate into parts","Divide equally."),
    ("dividend","noun","a sum paid to shareholders","Pay dividends."),
    ("divine","adjective","of or from God","Divine intervention."),
    ("division","noun","the action of separating","Cell division."),
    ("divorce","noun","the legal dissolution of a marriage","File for divorce."),
    ("dock","noun","an enclosed area of water for ships","At the dock."),
    ("doctrine","noun","a belief or set of beliefs","Political doctrine."),
    ("document","noun","a piece of written information","A legal document."),
    ("documentary","noun","a film giving factual information","A TV documentary."),
    ("documentation","noun","material providing official information","Proper documentation."),
    ("dolphin","noun","a small whale with a beaklike snout","A friendly dolphin."),
    ("domain","noun","an area of territory","Public domain."),
    ("domestic","adjective","relating to the running of a home","Domestic violence."),
    ("dominance","noun","power and influence over others","Market dominance."),
    ("dominant","adjective","most important or powerful","A dominant force."),
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
