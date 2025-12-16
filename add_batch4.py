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
    ("banner","noun","a long strip of cloth with a message","A welcome banner."),
    ("bargain","noun","an agreement between parties","A good bargain."),
    ("barn","noun","a large farm building","A red barn."),
    ("baron","noun","a member of the lowest order of nobility","Oil baron."),
    ("barrel","noun","a cylindrical container","A barrel of oil."),
    ("barren","adjective","too poor to produce vegetation","Barren land."),
    ("baseline","noun","a starting point for comparisons","Establish a baseline."),
    ("basin","noun","a bowl for washing","River basin."),
    ("beacon","noun","a light serving as a signal","A beacon of hope."),
    ("beam","noun","a ray of light","A beam of light."),
    ("beast","noun","an animal","A wild beast."),
    ("behalf","noun","in the interests of","On behalf of."),
    ("behave","verb","act in a certain way","Behave properly."),
    ("beloved","adjective","dearly loved","A beloved teacher."),
    ("benchmark","noun","a standard for comparison","Set a benchmark."),
    ("beneath","preposition","extending directly under","Beneath the surface."),
    ("beneficiary","noun","a person who benefits","The main beneficiary."),
    ("benign","adjective","gentle and kindly","A benign tumor."),
    ("beverage","noun","a drink","Alcoholic beverages."),
    ("beware","verb","be cautious about","Beware of dogs."),
    ("bias","noun","prejudice for or against","Confirm bias."),
    ("bid","verb","offer a certain price","Bid for the contract."),
    ("bilateral","adjective","having two sides","Bilateral agreement."),
    ("bind","verb","tie or fasten tightly","Legally binding."),
    ("biochemistry","noun","the chemistry of living organisms","Study biochemistry."),
    ("biodiversity","noun","variety of life in an ecosystem","Protect biodiversity."),
    ("biography","noun","an account of someone's life","Read the biography."),
    ("bishop","noun","a senior member of the clergy","The bishop spoke."),
    ("bizarre","adjective","very strange","A bizarre incident."),
    ("blade","noun","the flat cutting edge","A blade of grass."),
    ("blanket","noun","a large piece of woolen material","A warm blanket."),
    ("blast","noun","a destructive wave of air","A bomb blast."),
    ("blaze","noun","a very large fire","A forest blaze."),
    ("bleak","adjective","lacking vegetation and exposed","A bleak future."),
    ("blend","verb","mix together","Blend the ingredients."),
    ("bless","verb","invoke divine favor upon","Bless this house."),
    ("blind","adjective","unable to see","Color blind."),
    ("blink","verb","shut and open the eyes quickly","In the blink of an eye."),
    ("bliss","noun","perfect happiness","Marital bliss."),
    ("bloom","verb","produce flowers","Flowers bloom in spring."),
    ("blossom","noun","a flower on a tree","Cherry blossom."),
    ("blueprint","noun","a design plan","A blueprint for success."),
    ("blunder","noun","a stupid mistake","A serious blunder."),
    ("boast","verb","talk with excessive pride","Boast about achievements."),
    ("bold","adjective","showing courage","A bold move."),
    ("bolt","noun","a metal pin","Lightning bolt."),
    ("bond","noun","a thing used to tie things together","A strong bond."),
    ("bonus","noun","a sum of money added to wages","A year-end bonus."),
    ("boom","noun","a period of rapid economic growth","Economic boom."),
    ("boost","verb","help or encourage to increase","Boost confidence."),
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
