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
    ("abandon","verb","give up completely","Abandon the plan."),
    ("abbreviate","verb","shorten a word or phrase","Abbreviate the title."),
    ("abolish","verb","formally put an end to","Abolish slavery."),
    ("aboriginal","adjective","inhabiting a land from earliest times","Aboriginal culture."),
    ("abrupt","adjective","sudden and unexpected","An abrupt change."),
    ("absorb","verb","take in or soak up","Absorb information."),
    ("abstract","adjective","existing in thought only","Abstract art."),
    ("absurd","adjective","wildly unreasonable","An absurd idea."),
    ("abundant","adjective","existing in large quantities","Abundant resources."),
    ("accelerate","verb","increase in speed","Accelerate growth."),
    ("accent","noun","a distinctive way of pronunciation","A foreign accent."),
    ("acceptable","adjective","able to be agreed on","An acceptable solution."),
    ("accessible","adjective","able to be reached","Accessible to all."),
    ("accommodate","verb","provide lodging or room for","Accommodate guests."),
    ("accompany","verb","go somewhere with someone","Accompany the delegation."),
    ("accomplish","verb","achieve or complete successfully","Accomplish goals."),
    ("accountable","adjective","required to explain actions","Held accountable."),
    ("accumulate","verb","gather together over time","Accumulate wealth."),
    ("accurate","adjective","correct in all details","Accurate data."),
    ("accuse","verb","charge someone with an offense","Accuse of theft."),
    ("achieve","verb","successfully reach a goal","Achieve success."),
    ("acid","noun","a chemical substance","Acid rain."),
    ("acknowledge","verb","accept or admit the truth","Acknowledge the problem."),
    ("acquire","verb","buy or obtain","Acquire skills."),
    ("activate","verb","make something active","Activate the system."),
    ("acute","adjective","present or severe","An acute shortage."),
    ("adapt","verb","adjust to new conditions","Adapt to change."),
    ("adequate","adjective","sufficient for a requirement","Adequate funding."),
    ("adjacent","adjective","next to or adjoining","Adjacent buildings."),
    ("adjust","verb","alter slightly to achieve a result","Adjust the settings."),
    ("administer","verb","manage or be responsible for","Administer the program."),
    ("admire","verb","regard with respect","Admire the view."),
    ("admission","noun","the process of entering","Admission fee."),
    ("adolescent","noun","a young person developing into an adult","Adolescent behavior."),
    ("adopt","verb","legally take another's child","Adopt a policy."),
    ("advent","noun","the arrival of something notable","The advent of technology."),
    ("adverse","adjective","preventing success","Adverse effects."),
    ("advocate","verb","publicly recommend","Advocate for change."),
    ("aesthetic","adjective","concerned with beauty","Aesthetic appeal."),
    ("affair","noun","an event or sequence of events","Current affairs."),
    ("affect","verb","have an effect on","Affect the outcome."),
    ("affiliate","verb","officially attach to an organization","Affiliate with partners."),
    ("affirm","verb","state as a fact","Affirm the decision."),
    ("agenda","noun","a list of items to be discussed","Meeting agenda."),
    ("aggression","noun","hostile or violent behavior","Show aggression."),
    ("agile","adjective","able to move quickly","Agile development."),
    ("agriculture","noun","the science of farming","Sustainable agriculture."),
    ("aid","noun","help or support","Financial aid."),
    ("alarm","noun","a warning of danger","Sound the alarm."),
    ("albeit","conjunction","although","Albeit slowly."),
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

# 총계
total = sum(len(json.load(open(f'assets/data/{f}','r',encoding='utf-8'))) 
    for f in ['band45_words.json','band60_words.json','band70_words.json','band80_words.json'])
print(f"총계: {total}개, 남은 수: {5000-total}개")
