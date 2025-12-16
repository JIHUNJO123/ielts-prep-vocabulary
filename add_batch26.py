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
    ("water","noun","a transparent liquid","Drinking water."),
    ("wave","noun","a long body of water curling","Ocean waves."),
    ("way","noun","a method or manner","The best way."),
    ("weak","adjective","lacking physical strength","A weak signal."),
    ("weakness","noun","the state of being weak","A major weakness."),
    ("wealth","noun","an abundance of valuable possessions","Personal wealth."),
    ("wealthy","adjective","having a great deal of money","A wealthy family."),
    ("weapon","noun","a thing designed to cause harm","Nuclear weapons."),
    ("wear","verb","have on one's body","Wear a suit."),
    ("weather","noun","the state of the atmosphere","Cold weather."),
    ("web","noun","a network of fine threads","Spider web."),
    ("website","noun","a location on the internet","Company website."),
    ("wedding","noun","a marriage ceremony","Wedding ceremony."),
    ("week","noun","a period of seven days","Next week."),
    ("weekend","noun","Saturday and Sunday","This weekend."),
    ("weekly","adjective","done once a week","Weekly meeting."),
    ("weigh","verb","find out how heavy something is","Weigh yourself."),
    ("weight","noun","a body's mass","Lose weight."),
    ("weird","adjective","very strange","A weird situation."),
    ("welcome","verb","greet someone arriving","Welcome visitors."),
    ("welfare","noun","the health and happiness of a person","Child welfare."),
    ("well","adverb","in a good or satisfactory way","Done well."),
    ("well-being","noun","the state of being comfortable","Mental well-being."),
    ("well-known","adjective","known widely","A well-known brand."),
    ("west","noun","the direction of the sunset","Go west."),
    ("western","adjective","situated in the west","Western culture."),
    ("wet","adjective","covered with water","Wet clothes."),
    ("whatsoever","adverb","at all","No doubt whatsoever."),
    ("wheat","noun","a cereal plant","Wheat field."),
    ("wheel","noun","a circular object that revolves","Car wheel."),
    ("whenever","conjunction","at whatever time","Whenever possible."),
    ("whereas","conjunction","in contrast to the fact that","Whereas before."),
    ("whereby","adverb","by which","A method whereby."),
    ("wherever","conjunction","in or to whatever place","Wherever you go."),
    ("whether","conjunction","expressing doubt between alternatives","Whether or not."),
    ("whilst","conjunction","during the time that","Whilst working."),
    ("whisper","verb","speak very softly","Whisper a secret."),
    ("white","adjective","of the color of milk","White paper."),
    ("whoever","pronoun","the person who","Whoever wants."),
    ("whole","adjective","entire or complete","The whole story."),
    ("wholly","adverb","entirely","Wholly committed."),
    ("whose","determiner","belonging to which person","Whose book is this."),
    ("wide","adjective","of great extent","A wide range."),
    ("widely","adverb","over a large area","Widely used."),
    ("widen","verb","make or become wider","Widen the road."),
    ("widespread","adjective","found over a large area","Widespread damage."),
    ("width","noun","the measurement from side to side","The width of the room."),
    ("wild","adjective","living in a natural state","Wild animals."),
    ("wildlife","noun","wild animals collectively","Wildlife conservation."),
    ("will","noun","the faculty of conscious choice","Free will."),
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
