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
    ("democratic","adjective","relating to democracy","Democratic elections."),
    ("demographic","adjective","relating to population statistics","Demographic data."),
    ("demolish","verb","pull or knock down a building","Demolish the structure."),
    ("demon","noun","an evil spirit","Inner demons."),
    ("demonstrate","verb","clearly show the existence of","Demonstrate skills."),
    ("demonstration","noun","a public meeting or march","A peaceful demonstration."),
    ("denial","noun","the action of declaring untrue","A flat denial."),
    ("denounce","verb","publicly declare to be wrong","Denounce violence."),
    ("dense","adjective","closely compacted in substance","Dense fog."),
    ("density","noun","the degree of compactness","Population density."),
    ("dental","adjective","relating to the teeth","Dental care."),
    ("deny","verb","state that something is not true","Deny accusations."),
    ("depart","verb","leave, especially to start a journey","Depart from the airport."),
    ("department","noun","a division of a larger organization","The sales department."),
    ("departure","noun","the action of leaving","A sudden departure."),
    ("depend","verb","be controlled by","Depend on circumstances."),
    ("dependence","noun","the state of relying on someone","Drug dependence."),
    ("dependent","adjective","contingent on or determined by","Dependent on results."),
    ("depict","verb","represent by a drawing or painting","Depict scenes."),
    ("deploy","verb","move troops into position","Deploy resources."),
    ("deposit","noun","a sum of money placed in an account","Make a deposit."),
    ("depress","verb","make someone feel sad","Depress the market."),
    ("depression","noun","severe despondency and dejection","Clinical depression."),
    ("deprive","verb","deny a person the possession of","Deprive of rights."),
    ("depth","noun","the distance from the top to the bottom","Depth of knowledge."),
    ("deputy","noun","a person appointed to act for another","A deputy manager."),
    ("derive","verb","obtain something from a source","Derive pleasure from."),
    ("descend","verb","move downward","Descend the stairs."),
    ("descendant","noun","a person descended from another","A direct descendant."),
    ("descent","noun","an act of moving downward","A steep descent."),
    ("describe","verb","give an account in words","Describe the scene."),
    ("description","noun","a spoken or written account","A detailed description."),
    ("desert","noun","a waterless area of land","The Sahara desert."),
    ("deserve","verb","do something worthy of reward","Deserve recognition."),
    ("designate","verb","appoint to a specified position","Designate a leader."),
    ("designer","noun","a person who plans the form","A fashion designer."),
    ("desirable","adjective","worth having","A desirable outcome."),
    ("desire","noun","a strong feeling of wanting","A desire for change."),
    ("desk","noun","a piece of furniture for writing","A computer desk."),
    ("desperate","adjective","feeling hopelessness","Desperate measures."),
    ("despise","verb","feel contempt for","Despise dishonesty."),
    ("despite","preposition","without being affected by","Despite the rain."),
    ("destination","noun","the place to which someone is going","The final destination."),
    ("destiny","noun","the events that will happen to a person","Control your destiny."),
    ("destroy","verb","put an end to the existence of","Destroy evidence."),
    ("destruction","noun","the action of destroying","Environmental destruction."),
    ("destructive","adjective","causing great damage","Destructive behavior."),
    ("detach","verb","disengage something","Detach the cable."),
    ("detail","noun","an individual feature","Pay attention to detail."),
    ("detailed","adjective","having many details","A detailed report."),
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
