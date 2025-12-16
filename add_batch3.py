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
    ("arithmetic","noun","the branch of mathematics dealing with numbers","Basic arithmetic."),
    ("armour","noun","metal coverings worn for protection","A suit of armour."),
    ("array","noun","an impressive display or range","A vast array."),
    ("artefact","noun","an object made by a human being","Ancient artefacts."),
    ("articulate","verb","express an idea fluently","Articulate thoughts."),
    ("artificial","adjective","made by humans rather than nature","Artificial intelligence."),
    ("ascertain","verb","find something out for certain","Ascertain the facts."),
    ("aspect","noun","a particular part or feature","Every aspect."),
    ("aspire","verb","direct one's hopes toward achieving","Aspire to greatness."),
    ("assemble","verb","gather together in one place","Assemble the team."),
    ("assert","verb","state a fact confidently","Assert authority."),
    ("assess","verb","evaluate or estimate","Assess the damage."),
    ("asset","noun","a useful or valuable thing","A valuable asset."),
    ("assign","verb","allocate a job or duty","Assign tasks."),
    ("assist","verb","help someone","Assist with the project."),
    ("associate","verb","connect in the mind","Associate with success."),
    ("assume","verb","suppose to be the case","Assume responsibility."),
    ("assumption","noun","a thing accepted as true","A basic assumption."),
    ("assure","verb","tell someone positively","Assure quality."),
    ("astonish","verb","surprise greatly","Astonish the audience."),
    ("astronomy","noun","the study of celestial objects","Study astronomy."),
    ("atmosphere","noun","the envelope of gases surrounding earth","The atmosphere."),
    ("atom","noun","the smallest unit of an element","Split the atom."),
    ("attach","verb","fasten or join","Attach the file."),
    ("attain","verb","succeed in achieving","Attain goals."),
    ("attempt","verb","make an effort to achieve","Attempt the task."),
    ("attend","verb","be present at","Attend the meeting."),
    ("attribute","verb","regard as being caused by","Attribute success to."),
    ("auction","noun","a public sale to the highest bidder","Art auction."),
    ("audit","noun","an official inspection of accounts","Financial audit."),
    ("authentic","adjective","of undisputed origin","Authentic cuisine."),
    ("authorize","verb","give official permission","Authorize payment."),
    ("automate","verb","convert to automatic operation","Automate the process."),
    ("autonomous","adjective","having self-government","Autonomous region."),
    ("availability","noun","the quality of being available","Check availability."),
    ("avail","verb","help or benefit","To no avail."),
    ("avert","verb","turn away or prevent","Avert disaster."),
    ("aviation","noun","the flying of aircraft","Civil aviation."),
    ("await","verb","wait for","Await instructions."),
    ("axis","noun","an imaginary line around which a body rotates","The earth's axis."),
    ("bachelor","noun","an unmarried man","A bachelor's degree."),
    ("backdrop","noun","the setting or background","Against the backdrop."),
    ("backbone","noun","the spine","The backbone of society."),
    ("backup","noun","a copy of data stored separately","Create a backup."),
    ("bacteria","noun","microscopic organisms","Harmful bacteria."),
    ("badge","noun","a distinctive emblem","A name badge."),
    ("bail","noun","money paid to secure release","Post bail."),
    ("bait","noun","food used to attract prey","Use as bait."),
    ("ballot","noun","a process of voting","Secret ballot."),
    ("bandwidth","noun","a range of frequencies","Internet bandwidth."),
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

t,a = add_to_file('band80_words.json', NEW_WORDS, 'Band 8.0+')
print(f"Band 8.0+: {t}개 (+{a})")

total = sum(len(json.load(open(f'assets/data/{f}','r',encoding='utf-8'))) 
    for f in ['band45_words.json','band60_words.json','band70_words.json','band80_words.json'])
print(f"총계: {total}개, 남은 수: {5000-total}개")
