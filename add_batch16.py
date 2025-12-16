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
    ("diploma","noun","a certificate awarded by an educational institution","A university diploma."),
    ("diplomacy","noun","the profession of managing international relations","Skilled diplomacy."),
    ("diplomat","noun","a person appointed to conduct diplomacy","A senior diplomat."),
    ("diplomatic","adjective","relating to diplomacy","Diplomatic relations."),
    ("dire","adjective","extremely serious or urgent","Dire consequences."),
    ("direct","adjective","going straight to a place","A direct route."),
    ("direction","noun","the course along which something moves","A new direction."),
    ("directive","noun","an official instruction","An EU directive."),
    ("directly","adverb","without changing direction","Directly related."),
    ("director","noun","a person who is in charge","The managing director."),
    ("directory","noun","a book listing individuals","A phone directory."),
    ("dirt","noun","a substance such as mud","Covered in dirt."),
    ("dirty","adjective","covered or marked with dirt","Dirty water."),
    ("disability","noun","a physical or mental condition that limits movements","Learning disability."),
    ("disabled","adjective","having a physical or mental disability","Disabled access."),
    ("disadvantage","noun","an unfavorable circumstance","A major disadvantage."),
    ("disagree","verb","have a different opinion","Strongly disagree."),
    ("disagreement","noun","lack of consensus","A minor disagreement."),
    ("disappear","verb","cease to be visible","Disappear from view."),
    ("disappoint","verb","fail to fulfill expectations","Disappoint fans."),
    ("disappointment","noun","sadness from unfulfilled hopes","Hide disappointment."),
    ("disaster","noun","a sudden event causing great damage","A natural disaster."),
    ("disastrous","adjective","causing great damage","A disastrous decision."),
    ("discard","verb","get rid of as no longer useful","Discard waste."),
    ("discharge","verb","allow to leave","Discharge from hospital."),
    ("discipline","noun","the practice of training people to obey rules","Military discipline."),
    ("disclose","verb","make known","Disclose information."),
    ("disclosure","noun","the action of making new information known","Full disclosure."),
    ("discount","noun","a deduction from the usual cost","A big discount."),
    ("discourage","verb","cause to lose confidence","Discourage investment."),
    ("discourse","noun","written or spoken communication","Public discourse."),
    ("discover","verb","find unexpectedly","Discover new species."),
    ("discovery","noun","the action of finding something","A scientific discovery."),
    ("discretion","noun","the quality of behaving carefully","Use discretion."),
    ("discriminate","verb","recognize a distinction","Discriminate unfairly."),
    ("discrimination","noun","unjust treatment of different categories","Racial discrimination."),
    ("discuss","verb","talk about in order to reach a decision","Discuss the issue."),
    ("discussion","noun","the action of discussing","A group discussion."),
    ("disease","noun","a disorder of structure or function","Heart disease."),
    ("disgrace","noun","loss of reputation","A public disgrace."),
    ("disguise","noun","a means of altering one's appearance","In disguise."),
    ("dish","noun","a shallow container for food","A main dish."),
    ("dislike","verb","feel distaste for","Strongly dislike."),
    ("dismiss","verb","order or allow to leave","Dismiss the claim."),
    ("dismissal","noun","the act of dismissing","Wrongful dismissal."),
    ("disorder","noun","a state of confusion","A mental disorder."),
    ("dispatch","verb","send off to a destination","Dispatch goods."),
    ("dispense","verb","distribute or provide","Dispense advice."),
    ("disperse","verb","distribute over a wide area","Disperse the crowd."),
    ("displace","verb","take over the place of","Displace workers."),
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
