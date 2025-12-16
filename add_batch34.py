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
    ("apprentice","noun","a person learning a trade","An apprentice electrician."),
    ("apprenticeship","noun","training under a skilled employer","Complete an apprenticeship."),
    ("appropriate","adjective","suitable for a particular purpose","An appropriate response."),
    ("appropriately","adverb","in a manner that is suitable","Dress appropriately."),
    ("appropriation","noun","the action of taking something","Budget appropriation."),
    ("approval","noun","the belief that something is good","Seek approval."),
    ("approve","verb","officially agree to","Approve the plan."),
    ("approximately","adverb","close to an exact amount","Approximately correct."),
    ("approximation","noun","a close estimate","A rough approximation."),
    ("apt","adjective","appropriate in the circumstances","An apt description."),
    ("aptitude","noun","a natural ability to do something","Show aptitude."),
    ("aquarium","noun","a tank for keeping fish","Fish aquarium."),
    ("aquatic","adjective","relating to water","Aquatic animals."),
    ("arbitrary","adjective","based on random choice","An arbitrary decision."),
    ("arbitration","noun","the use of an arbitrator","Go to arbitration."),
    ("arc","noun","a part of a curve","A rainbow arc."),
    ("arch","noun","a curved structure","Stone arch."),
    ("archaic","adjective","very old or old-fashioned","Archaic language."),
    ("archaeology","noun","the study of ancient cultures","Archaeological site."),
    ("architect","noun","a person who designs buildings","Famous architect."),
    ("architectural","adjective","relating to architecture","Architectural design."),
    ("architecture","noun","the art of designing buildings","Modern architecture."),
    ("archive","noun","a collection of historical documents","National archives."),
    ("arctic","adjective","relating to the region around the North Pole","Arctic climate."),
    ("ardent","adjective","enthusiastic or passionate","An ardent supporter."),
    ("arduous","adjective","involving or requiring strenuous effort","An arduous journey."),
    ("arena","noun","a level area for sports","Sports arena."),
    ("arguably","adverb","it may be argued","Arguably the best."),
    ("argument","noun","an exchange of opposing views","A heated argument."),
    ("arid","adjective","having little or no rain","Arid climate."),
    ("arise","verb","emerge or become apparent","Problems arise."),
    ("aristocracy","noun","the highest class in society","The British aristocracy."),
    ("aristocrat","noun","a member of the aristocracy","A wealthy aristocrat."),
    ("arithmetic","noun","the branch of mathematics with numbers","Basic arithmetic."),
    ("arm","noun","each of the upper limbs","Broken arm."),
    ("armament","noun","military weapons","Nuclear armaments."),
    ("armed","adjective","equipped with weapons","Armed forces."),
    ("armor","noun","metal covering for protection","Suit of armor."),
    ("army","noun","an organized military force","Join the army."),
    ("aroma","noun","a distinctive pleasant smell","Coffee aroma."),
    ("aromatic","adjective","having a pleasant smell","Aromatic herbs."),
    ("arouse","verb","evoke a feeling or response","Arouse suspicion."),
    ("arrange","verb","put in a neat order","Arrange the furniture."),
    ("arrangement","noun","a thing that has been arranged","Make arrangements."),
    ("array","noun","an impressive display","A vast array."),
    ("arrest","verb","seize someone by legal authority","Arrest the suspect."),
    ("arrival","noun","the action of arriving","On arrival."),
    ("arrive","verb","reach a place at the end of a journey","Arrive on time."),
    ("arrogance","noun","an attitude of superiority","Display arrogance."),
    ("arrogant","adjective","having an exaggerated sense of importance","An arrogant attitude."),
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
