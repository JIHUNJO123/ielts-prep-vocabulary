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
    ("effective","adjective","successful in producing a desired result","An effective solution."),
    ("effectiveness","noun","the degree to which something is effective","Measure effectiveness."),
    ("efficiency","noun","the state of achieving maximum productivity","Improve efficiency."),
    ("efficient","adjective","achieving maximum productivity with minimum effort","An efficient process."),
    ("efficiently","adverb","in a way that achieves maximum productivity","Work efficiently."),
    ("effort","noun","a vigorous or determined attempt","Make an effort."),
    ("egg","noun","an oval reproductive body laid by a female bird","A boiled egg."),
    ("elastic","adjective","able to resume normal shape after stretching","An elastic band."),
    ("elbow","noun","the joint between the forearm and upper arm","Elbow room."),
    ("elderly","adjective","old or aging","Elderly people."),
    ("elect","verb","choose by voting","Elect a president."),
    ("election","noun","a formal process of electing a person","A general election."),
    ("electric","adjective","of or worked by electricity","An electric car."),
    ("electrical","adjective","relating to electricity","Electrical equipment."),
    ("electricity","noun","a form of energy resulting from charged particles","Generate electricity."),
    ("electron","noun","a stable subatomic particle","An electron microscope."),
    ("electronic","adjective","having components such as microchips","Electronic devices."),
    ("electronics","noun","the branch of physics dealing with emission of electrons","Consumer electronics."),
    ("elegant","adjective","pleasingly graceful and stylish","An elegant design."),
    ("element","noun","a component or part of something","A key element."),
    ("elementary","adjective","relating to the basic elements","Elementary school."),
    ("elephant","noun","a large mammal with a trunk","An African elephant."),
    ("elevate","verb","raise or lift to a higher position","Elevate the status."),
    ("elevator","noun","a platform or compartment for raising and lowering people","Take the elevator."),
    ("eliminate","verb","completely remove or get rid of","Eliminate errors."),
    ("elimination","noun","the process of eliminating","Process of elimination."),
    ("elite","noun","a select group that is superior","The elite class."),
    ("elsewhere","adverb","in or to another place","Look elsewhere."),
    ("email","noun","messages distributed by electronic means","Send an email."),
    ("embark","verb","go on board a ship or aircraft","Embark on a journey."),
    ("embarrass","verb","cause to feel awkward or ashamed","Embarrass someone."),
    ("embarrassment","noun","a feeling of self-consciousness","Cause embarrassment."),
    ("embassy","noun","the official residence of an ambassador","The US Embassy."),
    ("embrace","verb","hold closely in one's arms","Embrace change."),
    ("emerge","verb","move out of or away from something","Emerge victorious."),
    ("emergence","noun","the process of coming into being","The emergence of new ideas."),
    ("emergency","noun","a serious, unexpected situation","In an emergency."),
    ("emission","noun","the production and discharge of something","Reduce emissions."),
    ("emit","verb","produce and discharge","Emit light."),
    ("emotion","noun","a strong feeling","Mixed emotions."),
    ("emotional","adjective","relating to emotions","Emotional support."),
    ("emotionally","adverb","in an emotional manner","Emotionally drained."),
    ("emperor","noun","a sovereign ruler of great power","The Roman Emperor."),
    ("emphasis","noun","special importance given to something","Place emphasis on."),
    ("emphasize","verb","give special importance to","Emphasize the point."),
    ("empire","noun","an extensive group of states under a single authority","Build an empire."),
    ("employ","verb","give work to someone","Employ workers."),
    ("employee","noun","a person employed for wages","A valued employee."),
    ("employer","noun","a person or organization that employs people","A fair employer."),
    ("employment","noun","the condition of having paid work","Full employment."),
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
