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
    ("algorithm","noun","a process for solving a problem","A sorting algorithm."),
    ("alien","adjective","belonging to a foreign country","Alien species."),
    ("align","verb","place in a straight line","Align the text."),
    ("alleviate","verb","make suffering less severe","Alleviate pain."),
    ("allocate","verb","distribute for a purpose","Allocate resources."),
    ("allowance","noun","an amount of something permitted","Daily allowance."),
    ("alloy","noun","a metal made by combining metals","Steel alloy."),
    ("ally","noun","a state cooperating with another","A close ally."),
    ("alter","verb","change in character","Alter the plan."),
    ("alternate","adjective","every other","On alternate days."),
    ("altitude","noun","height above sea level","High altitude."),
    ("amateur","noun","a person who does something for pleasure","An amateur photographer."),
    ("ambassador","noun","an accredited diplomat","The US ambassador."),
    ("ambiguous","adjective","open to more than one interpretation","An ambiguous statement."),
    ("ambitious","adjective","having a strong desire for success","An ambitious project."),
    ("amend","verb","make minor changes to improve","Amend the law."),
    ("ample","adjective","enough or more than enough","Ample time."),
    ("analogy","noun","a comparison between two things","Draw an analogy."),
    ("anatomy","noun","the branch of biology dealing with body structure","Human anatomy."),
    ("ancestor","noun","a person from whom one is descended","Our ancestors."),
    ("anchor","noun","a heavy object to moor a vessel","Drop anchor."),
    ("ancient","adjective","belonging to the very distant past","Ancient history."),
    ("anecdote","noun","a short amusing story","A personal anecdote."),
    ("angle","noun","the space between two intersecting lines","A right angle."),
    ("animate","verb","bring to life","Animate the character."),
    ("anniversary","noun","the date on which an event occurred","Wedding anniversary."),
    ("announce","verb","make a public statement","Announce the results."),
    ("annual","adjective","occurring once every year","Annual report."),
    ("anomaly","noun","something that deviates from normal","A statistical anomaly."),
    ("anonymous","adjective","of unknown name","An anonymous donor."),
    ("anticipate","verb","regard as probable","Anticipate problems."),
    ("anxiety","noun","a feeling of worry","Reduce anxiety."),
    ("apparent","adjective","clearly visible or understood","For no apparent reason."),
    ("appeal","verb","make a serious request","Appeal for help."),
    ("appetite","noun","a natural desire to satisfy a need","Loss of appetite."),
    ("appliance","noun","a device designed for a specific task","Kitchen appliances."),
    ("applicable","adjective","relevant or appropriate","Applicable laws."),
    ("applicant","noun","a person who applies for something","Job applicants."),
    ("appoint","verb","assign a job or role to","Appoint a manager."),
    ("appreciate","verb","recognize the full worth of","Appreciate your help."),
    ("apprentice","noun","a person learning a trade","An apprentice chef."),
    ("appropriate","adjective","suitable or proper","Appropriate behavior."),
    ("approve","verb","officially agree to","Approve the budget."),
    ("approximate","adjective","close to the actual","An approximate figure."),
    ("arbitrary","adjective","based on random choice","An arbitrary decision."),
    ("arch","noun","a curved symmetrical structure","A stone arch."),
    ("architect","noun","a person who designs buildings","A famous architect."),
    ("archive","noun","a collection of historical documents","Digital archive."),
    ("arena","noun","a place for sports or entertainment","A sports arena."),
    ("arise","verb","emerge or become apparent","Problems may arise."),
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
