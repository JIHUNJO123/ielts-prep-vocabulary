#!/usr/bin/env python3
import json, requests, time
API = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"
LANGS = ['ko', 'ja', 'zh', 'es', 'fr', 'de']
WORDS = [
    ("barricade", "noun", "barrier", "Police barricade.", "Band 8.0+"),
    ("basalt", "noun", "volcanic rock", "Basalt columns.", "Band 8.0+"),
    ("baseline", "noun", "starting point", "Establish baseline.", "Band 7.0-7.5"),
    ("basement", "noun", "lower floor", "Dark basement.", "Band 6.0-6.5"),
    ("basin", "noun", "bowl", "River basin.", "Band 7.0-7.5"),
    ("battalion", "noun", "military unit", "Army battalion.", "Band 8.0+"),
    ("battlefield", "noun", "war area", "Ancient battlefield.", "Band 7.0-7.5"),
    ("battleground", "noun", "fighting area", "Political battleground.", "Band 8.0+"),
    ("beacon", "noun", "signal light", "Lighthouse beacon.", "Band 8.0+"),
    ("beaker", "noun", "container", "Lab beaker.", "Band 7.0-7.5"),
    ("beam", "noun", "light ray", "Laser beam.", "Band 6.0-6.5"),
    ("beast", "noun", "animal", "Wild beast.", "Band 6.0-6.5"),
    ("beautician", "noun", "beauty expert", "Professional beautician.", "Band 7.0-7.5"),
    ("bedding", "noun", "bed covers", "Fresh bedding.", "Band 6.0-6.5"),
    ("beehive", "noun", "bee home", "Natural beehive.", "Band 7.0-7.5"),
    ("beggar", "noun", "homeless person", "Street beggar.", "Band 7.0-7.5"),
    ("beginner", "noun", "novice", "Complete beginner.", "Band 6.0-6.5"),
    ("behalf", "noun", "interest", "On behalf of.", "Band 7.0-7.5"),
    ("behavioral", "adjective", "related to behavior", "Behavioral science.", "Band 7.0-7.5"),
    ("believer", "noun", "faithful person", "True believer.", "Band 6.0-6.5"),
    ("bellboy", "noun", "hotel worker", "Call the bellboy.", "Band 7.0-7.5"),
    ("belongings", "noun", "possessions", "Personal belongings.", "Band 6.0-6.5"),
    ("benefactor", "noun", "supporter", "Generous benefactor.", "Band 8.0+"),
    ("beneficiary", "noun", "receiver", "Insurance beneficiary.", "Band 8.0+"),
    ("benevolence", "noun", "kindness", "Acts of benevolence.", "Band 8.0+"),
    ("beverage", "noun", "drink", "Hot beverage.", "Band 6.0-6.5"),
    ("bibliography", "noun", "book list", "Complete bibliography.", "Band 8.0+"),
    ("biceps", "noun", "arm muscle", "Strong biceps.", "Band 7.0-7.5"),
    ("bicyclist", "noun", "bike rider", "Professional bicyclist.", "Band 7.0-7.5"),
    ("bidder", "noun", "auction participant", "Highest bidder.", "Band 7.0-7.5"),
    ("bigotry", "noun", "intolerance", "Fight bigotry.", "Band 8.0+"),
    ("bilingual", "adjective", "two languages", "Bilingual education.", "Band 7.0-7.5"),
    ("billboard", "noun", "large sign", "Highway billboard.", "Band 6.0-6.5"),
    ("billing", "noun", "invoicing", "Monthly billing.", "Band 7.0-7.5"),
    ("biodegradable", "adjective", "eco-friendly", "Biodegradable packaging.", "Band 7.0-7.5"),
    ("biodiversity", "noun", "biological variety", "Protect biodiversity.", "Band 7.0-7.5"),
    ("biofuel", "noun", "organic fuel", "Sustainable biofuel.", "Band 8.0+"),
    ("biography", "noun", "life story", "Read biography.", "Band 6.0-6.5"),
    ("biologist", "noun", "scientist", "Marine biologist.", "Band 6.0-6.5"),
    ("biology", "noun", "life science", "Study biology.", "Band 6.0-6.5"),
    ("biotech", "noun", "biotechnology", "Biotech company.", "Band 7.0-7.5"),
    ("birthplace", "noun", "origin place", "Historical birthplace.", "Band 6.0-6.5"),
    ("bishop", "noun", "religious leader", "Catholic bishop.", "Band 7.0-7.5"),
    ("blackout", "noun", "power failure", "City blackout.", "Band 7.0-7.5"),
    ("blaze", "noun", "fire", "Forest blaze.", "Band 7.0-7.5"),
    ("blessing", "noun", "good wish", "Count your blessings.", "Band 6.0-6.5"),
    ("blindness", "noun", "inability to see", "Color blindness.", "Band 7.0-7.5"),
    ("bliss", "noun", "joy", "Domestic bliss.", "Band 8.0+"),
    ("blizzard", "noun", "snowstorm", "Severe blizzard.", "Band 7.0-7.5"),
    ("blockade", "noun", "barrier", "Naval blockade.", "Band 8.0+"),
    ("blogger", "noun", "online writer", "Popular blogger.", "Band 6.0-6.5"),
    ("bloodstream", "noun", "blood flow", "Enter the bloodstream.", "Band 7.0-7.5"),
    ("blueprint", "noun", "plan", "Building blueprint.", "Band 7.0-7.5"),
    ("blues", "noun", "music genre", "Chicago blues.", "Band 7.0-7.5"),
    ("boardroom", "noun", "meeting room", "Corporate boardroom.", "Band 7.0-7.5"),
    ("bodyguard", "noun", "protector", "Personal bodyguard.", "Band 6.0-6.5"),
    ("bombardment", "noun", "attack", "Heavy bombardment.", "Band 8.0+"),
    ("bonfire", "noun", "outdoor fire", "Beach bonfire.", "Band 6.0-6.5"),
    ("bookcase", "noun", "shelf", "Wooden bookcase.", "Band 6.0-6.5"),
    ("booklet", "noun", "small book", "Information booklet.", "Band 6.0-6.5"),
    ("bookmark", "noun", "page marker", "Digital bookmark.", "Band 6.0-6.5"),
    ("bookshelf", "noun", "shelf", "Full bookshelf.", "Band 6.0-6.5"),
    ("booster", "noun", "enhancer", "Booster shot.", "Band 7.0-7.5"),
    ("borderline", "noun", "boundary", "On the borderline.", "Band 7.0-7.5"),
    ("botanist", "noun", "plant scientist", "Famous botanist.", "Band 8.0+"),
    ("botany", "noun", "plant study", "Study botany.", "Band 7.0-7.5"),
    ("boulder", "noun", "large rock", "Giant boulder.", "Band 7.0-7.5"),
    ("boulevard", "noun", "wide street", "Sunset Boulevard.", "Band 7.0-7.5"),
    ("bounty", "noun", "reward", "Generous bounty.", "Band 8.0+"),
    ("bouquet", "noun", "flowers", "Wedding bouquet.", "Band 6.0-6.5"),
    ("boutique", "noun", "small shop", "Fashion boutique.", "Band 6.0-6.5"),
    ("bowling", "noun", "sport", "Ten-pin bowling.", "Band 6.0-6.5"),
    ("boxer", "noun", "fighter", "Professional boxer.", "Band 6.0-6.5"),
    ("boxing", "noun", "sport", "Olympic boxing.", "Band 6.0-6.5"),
    ("boycott", "noun", "protest", "Consumer boycott.", "Band 7.0-7.5"),
    ("brainstorm", "noun", "idea session", "Creative brainstorm.", "Band 7.0-7.5"),
    ("brainwashing", "noun", "mind control", "Political brainwashing.", "Band 8.0+"),
    ("branding", "noun", "marketing", "Corporate branding.", "Band 7.0-7.5"),
    ("bravado", "noun", "false courage", "Show bravado.", "Band 8.0+"),
    ("bravery", "noun", "courage", "Acts of bravery.", "Band 6.0-6.5"),
    ("breach", "noun", "violation", "Security breach.", "Band 7.0-7.5"),
    ("breakdown", "noun", "failure", "Mental breakdown.", "Band 6.0-6.5"),
    ("breakthrough", "noun", "discovery", "Scientific breakthrough.", "Band 6.0-6.5"),
    ("brewery", "noun", "beer factory", "Local brewery.", "Band 7.0-7.5"),
    ("bribery", "noun", "corruption", "Political bribery.", "Band 8.0+"),
    ("brickwork", "noun", "brick construction", "Decorative brickwork.", "Band 8.0+"),
    ("bridegroom", "noun", "groom", "Nervous bridegroom.", "Band 7.0-7.5"),
    ("briefcase", "noun", "bag", "Leather briefcase.", "Band 6.0-6.5"),
    ("briefing", "noun", "meeting", "Press briefing.", "Band 7.0-7.5"),
    ("brightness", "noun", "light level", "Adjust brightness.", "Band 6.0-6.5"),
    ("brochure", "noun", "pamphlet", "Travel brochure.", "Band 6.0-6.5"),
    ("broker", "noun", "agent", "Real estate broker.", "Band 7.0-7.5"),
    ("bronchitis", "noun", "lung condition", "Chronic bronchitis.", "Band 8.0+"),
    ("bronze", "noun", "metal", "Bronze medal.", "Band 6.0-6.5"),
    ("brotherhood", "noun", "fellowship", "Sense of brotherhood.", "Band 7.0-7.5"),
    ("bruise", "noun", "injury", "Minor bruise.", "Band 6.0-6.5"),
    ("brunch", "noun", "meal", "Sunday brunch.", "Band 6.0-6.5"),
    ("brutality", "noun", "cruelty", "Police brutality.", "Band 8.0+"),
    ("buckle", "noun", "fastener", "Belt buckle.", "Band 7.0-7.5"),
    ("buddy", "noun", "friend", "Best buddy.", "Band 6.0-6.5"),
    ("buffet", "noun", "food service", "Breakfast buffet.", "Band 6.0-6.5"),
    ("buggy", "noun", "cart", "Baby buggy.", "Band 7.0-7.5"),
    ("bugle", "noun", "instrument", "Military bugle.", "Band 8.0+"),
    ("bulb", "noun", "light source", "Light bulb.", "Band 6.0-6.5"),
    ("bulk", "noun", "mass", "In bulk.", "Band 6.0-6.5"),
    ("bulletin", "noun", "announcement", "News bulletin.", "Band 7.0-7.5"),
    ("bullying", "noun", "harassment", "School bullying.", "Band 6.0-6.5"),
    ("bumper", "noun", "car part", "Front bumper.", "Band 7.0-7.5"),
    ("bungalow", "noun", "house type", "Beach bungalow.", "Band 7.0-7.5"),
    ("bunker", "noun", "shelter", "Underground bunker.", "Band 7.0-7.5"),
]

def translate_batch(texts, lang):
    url = f"https://translation.googleapis.com/language/translate/v2?key={API}"
    result = []
    for i in range(0, len(texts), 100):
        batch = texts[i:i+100]
        try:
            r = requests.post(url, json={"q": batch, "source": "en", "target": lang}, timeout=30)
            if r.status_code == 200:
                result.extend([t['translatedText'] for t in r.json()['data']['translations']])
            else:
                result.extend(batch)
        except:
            result.extend(batch)
        time.sleep(0.1)
    return result

with open('assets/data/words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)
existing = {w['word'].lower() for w in words}
start_id = max(w['id'] for w in words) + 1
cats = ["Academic", "Environment", "Technology", "Health", "Education", "Business", "Science", "Media", "Society", "Culture"]
new_words = []
for word, pos, defn, ex, level in WORDS:
    if word.lower() not in existing:
        new_words.append({"id": start_id + len(new_words), "word": word, "level": level, "partOfSpeech": pos, "definition": defn, "example": ex, "category": cats[(start_id + len(new_words)) % 10]})
        existing.add(word.lower())
print(f"새 단어: {len(new_words)}개")
if new_words:
    defs = [w['definition'] for w in new_words]
    exs = [w['example'] for w in new_words]
    for lang in LANGS:
        print(f"{lang}...")
        td = translate_batch(defs, lang)
        te = translate_batch(exs, lang)
        for i, w in enumerate(new_words):
            if 'translations' not in w: w['translations'] = {}
            w['translations'][lang] = {'definition': td[i], 'example': te[i]}
    words.extend(new_words)
    with open('assets/data/words.json', 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
print(f"총: {len(words)}개")
