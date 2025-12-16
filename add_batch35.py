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
    ("arrow","noun","a thin pointed weapon shot from a bow","Bow and arrow."),
    ("arson","noun","the crime of deliberately setting fire","Commit arson."),
    ("artery","noun","a blood vessel carrying blood from the heart","Blocked artery."),
    ("arthritis","noun","painful inflammation of the joints","Suffer from arthritis."),
    ("article","noun","a particular item or object","A newspaper article."),
    ("articulate","adjective","having or showing the ability to speak fluently","An articulate speaker."),
    ("artifact","noun","an object made by a human being","Historical artifact."),
    ("artificial","adjective","made by human skill","Artificial intelligence."),
    ("artificially","adverb","in an artificial manner","Artificially created."),
    ("artillery","noun","large-caliber guns","Artillery fire."),
    ("artisan","noun","a skilled worker who makes things by hand","Local artisan."),
    ("artistic","adjective","having or revealing creative skill","Artistic talent."),
    ("ascend","verb","go up or climb","Ascend the stairs."),
    ("ascendancy","noun","occupation of a position of dominance","Rise to ascendancy."),
    ("ascent","noun","a climb or walk to the top","The ascent of the mountain."),
    ("ascertain","verb","find out for certain","Ascertain the facts."),
    ("ascribe","verb","attribute something to a cause","Ascribe blame."),
    ("ashamed","adjective","embarrassed or guilty","Feel ashamed."),
    ("aside","adverb","to one side","Set aside."),
    ("aspiration","noun","a hope or ambition","Career aspirations."),
    ("aspire","verb","direct one's hopes toward achieving something","Aspire to greatness."),
    ("assault","noun","a physical attack","Assault charges."),
    ("assemble","verb","gather together in one place","Assemble the team."),
    ("assembly","noun","a group of people gathered together","General assembly."),
    ("assert","verb","state a fact confidently","Assert your rights."),
    ("assertion","noun","a confident and forceful statement","Make an assertion."),
    ("assertive","adjective","having a confident personality","An assertive manner."),
    ("assess","verb","evaluate the nature of something","Assess the situation."),
    ("assessment","noun","the evaluation of something","Risk assessment."),
    ("asset","noun","a useful or valuable thing","A valuable asset."),
    ("assign","verb","allocate a job or duty","Assign tasks."),
    ("assignment","noun","a task or piece of work allocated","Complete the assignment."),
    ("assimilate","verb","take in and understand fully","Assimilate information."),
    ("assimilation","noun","the process of absorbing information","Cultural assimilation."),
    ("assist","verb","help someone","Assist with the project."),
    ("assistance","noun","the provision of help","Financial assistance."),
    ("assistant","noun","a person who helps","Personal assistant."),
    ("associate","verb","connect in the mind","Associate with success."),
    ("association","noun","a group of people organized for a purpose","Trade association."),
    ("assortment","noun","a miscellaneous collection","An assortment of items."),
    ("assume","verb","suppose to be the case","Assume responsibility."),
    ("assumption","noun","a thing that is accepted as true","Basic assumption."),
    ("assurance","noun","a positive declaration","Give assurance."),
    ("assure","verb","tell someone positively","Assure success."),
    ("assured","adjective","confident","Feel assured."),
    ("asthma","noun","a respiratory condition","Asthma attack."),
    ("astonish","verb","surprise greatly","Astonish everyone."),
    ("astonished","adjective","greatly surprised","Completely astonished."),
    ("astonishing","adjective","extremely surprising","An astonishing result."),
    ("astonishment","noun","great surprise","Look in astonishment."),
    ("astronaut","noun","a person trained to travel in a spacecraft","An astronaut landed."),
    ("astronomy","noun","the study of celestial objects","Study astronomy."),
    ("asylum","noun","protection from danger","Seek asylum."),
    ("athlete","noun","a person who is proficient in sports","Professional athlete."),
    ("athletic","adjective","physically strong and fit","Athletic ability."),
    ("atlas","noun","a book of maps","World atlas."),
    ("atmosphere","noun","the envelope of gases surrounding the earth","Earth's atmosphere."),
    ("atmospheric","adjective","relating to the atmosphere","Atmospheric pressure."),
    ("atom","noun","the smallest unit of a chemical element","Atom structure."),
    ("atomic","adjective","relating to an atom","Atomic energy."),
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
