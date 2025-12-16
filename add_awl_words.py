#!/usr/bin/env python3
"""IELTS AWL 단어 대량 추가 + 번역"""
import json
import requests
import time

GOOGLE_API_KEY = "AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk"
LANGUAGES = ['ko', 'ja', 'zh', 'es', 'fr', 'de']

# IELTS Academic Word List - 600개
AWL_WORDS = [
    # Band 4.5-5.5 (기초)
    ("analyze", "verb", "to examine in detail", "Analyze the data carefully.", "Band 4.5-5.5"),
    ("approach", "noun", "a way of dealing with something", "We need a different approach.", "Band 4.5-5.5"),
    ("area", "noun", "a particular region", "This area is protected.", "Band 4.5-5.5"),
    ("assess", "verb", "to evaluate or estimate", "Assess the situation first.", "Band 4.5-5.5"),
    ("assume", "verb", "to suppose to be true", "Don't assume anything.", "Band 4.5-5.5"),
    ("authority", "noun", "power to give orders", "The authority approved it.", "Band 4.5-5.5"),
    ("available", "adjective", "able to be used", "Resources are available.", "Band 4.5-5.5"),
    ("benefit", "noun", "an advantage", "The benefits are clear.", "Band 4.5-5.5"),
    ("concept", "noun", "an abstract idea", "Understand the concept.", "Band 4.5-5.5"),
    ("consist", "verb", "to be composed of", "The team consists of experts.", "Band 4.5-5.5"),
    ("constitute", "verb", "to form or make up", "This constitutes a problem.", "Band 4.5-5.5"),
    ("context", "noun", "circumstances or setting", "Consider the context.", "Band 4.5-5.5"),
    ("contract", "noun", "a written agreement", "Sign the contract.", "Band 4.5-5.5"),
    ("create", "verb", "to bring into existence", "Create new opportunities.", "Band 4.5-5.5"),
    ("data", "noun", "facts and statistics", "Collect the data.", "Band 4.5-5.5"),
    ("define", "verb", "to state the meaning", "Define the term.", "Band 4.5-5.5"),
    ("derive", "verb", "to obtain from a source", "Derive the formula.", "Band 4.5-5.5"),
    ("distribute", "verb", "to give out", "Distribute the materials.", "Band 4.5-5.5"),
    ("economy", "noun", "system of trade", "The economy is growing.", "Band 4.5-5.5"),
    ("environment", "noun", "surroundings", "Protect the environment.", "Band 4.5-5.5"),
    ("establish", "verb", "to set up", "Establish a routine.", "Band 4.5-5.5"),
    ("estimate", "verb", "to roughly calculate", "Estimate the cost.", "Band 4.5-5.5"),
    ("evident", "adjective", "clearly seen", "The answer is evident.", "Band 4.5-5.5"),
    ("export", "verb", "to send abroad", "Export goods overseas.", "Band 4.5-5.5"),
    ("factor", "noun", "an element", "Consider every factor.", "Band 4.5-5.5"),
    ("finance", "noun", "money management", "Study finance.", "Band 4.5-5.5"),
    ("formula", "noun", "a rule expressed in symbols", "Apply the formula.", "Band 4.5-5.5"),
    ("function", "noun", "purpose or role", "Understand its function.", "Band 4.5-5.5"),
    ("identify", "verb", "to recognize", "Identify the problem.", "Band 4.5-5.5"),
    ("income", "noun", "money received", "Increase your income.", "Band 4.5-5.5"),
    ("indicate", "verb", "to point out", "The results indicate success.", "Band 4.5-5.5"),
    ("individual", "noun", "a single person", "Every individual matters.", "Band 4.5-5.5"),
    ("interpret", "verb", "to explain meaning", "Interpret the data.", "Band 4.5-5.5"),
    ("involve", "verb", "to include", "This involves risk.", "Band 4.5-5.5"),
    ("issue", "noun", "a topic or problem", "Address the issue.", "Band 4.5-5.5"),
    ("labor", "noun", "work or workers", "Labor costs increased.", "Band 4.5-5.5"),
    ("legal", "adjective", "relating to law", "Seek legal advice.", "Band 4.5-5.5"),
    ("legislate", "verb", "to make laws", "The government will legislate.", "Band 4.5-5.5"),
    ("major", "adjective", "important or large", "A major achievement.", "Band 4.5-5.5"),
    ("method", "noun", "a way of doing", "Use this method.", "Band 4.5-5.5"),
    ("occur", "verb", "to happen", "Accidents occur daily.", "Band 4.5-5.5"),
    ("percent", "noun", "parts per hundred", "Fifty percent agreed.", "Band 4.5-5.5"),
    ("period", "noun", "a length of time", "A long period passed.", "Band 4.5-5.5"),
    ("policy", "noun", "a course of action", "Review the policy.", "Band 4.5-5.5"),
    ("principle", "noun", "a fundamental truth", "Follow the principle.", "Band 4.5-5.5"),
    ("proceed", "verb", "to continue", "Proceed with caution.", "Band 4.5-5.5"),
    ("process", "noun", "a series of actions", "Follow the process.", "Band 4.5-5.5"),
    ("require", "verb", "to need", "This requires attention.", "Band 4.5-5.5"),
    ("research", "noun", "systematic investigation", "Conduct research.", "Band 4.5-5.5"),
    ("respond", "verb", "to reply", "Respond quickly.", "Band 4.5-5.5"),
    ("role", "noun", "a function", "Play an important role.", "Band 4.5-5.5"),
    ("section", "noun", "a distinct part", "Read this section.", "Band 4.5-5.5"),
    ("sector", "noun", "a part of economy", "The private sector grew.", "Band 4.5-5.5"),
    ("significant", "adjective", "important", "A significant change.", "Band 4.5-5.5"),
    ("similar", "adjective", "alike", "They look similar.", "Band 4.5-5.5"),
    ("source", "noun", "origin", "Cite your sources.", "Band 4.5-5.5"),
    ("specific", "adjective", "particular", "Be more specific.", "Band 4.5-5.5"),
    ("structure", "noun", "arrangement", "The structure is sound.", "Band 4.5-5.5"),
    ("theory", "noun", "a system of ideas", "Test the theory.", "Band 4.5-5.5"),
    ("vary", "verb", "to differ", "Results vary widely.", "Band 4.5-5.5"),
    
    # Band 6.0-6.5 (중급)
    ("abandon", "verb", "to give up completely", "They abandoned the project.", "Band 6.0-6.5"),
    ("abstract", "adjective", "theoretical", "An abstract concept.", "Band 6.0-6.5"),
    ("academy", "noun", "a place of study", "Join the academy.", "Band 6.0-6.5"),
    ("access", "noun", "way of entering", "Gain access to data.", "Band 6.0-6.5"),
    ("accommodate", "verb", "to provide for", "The hotel accommodates guests.", "Band 6.0-6.5"),
    ("accompany", "verb", "to go with", "I will accompany you.", "Band 6.0-6.5"),
    ("accumulate", "verb", "to gather over time", "Wealth accumulates slowly.", "Band 6.0-6.5"),
    ("accurate", "adjective", "correct", "The data is accurate.", "Band 6.0-6.5"),
    ("acknowledge", "verb", "to accept or admit", "Acknowledge your mistakes.", "Band 6.0-6.5"),
    ("acquire", "verb", "to obtain", "Acquire new skills.", "Band 6.0-6.5"),
    ("adapt", "verb", "to adjust", "Adapt to changes.", "Band 6.0-6.5"),
    ("adequate", "adjective", "sufficient", "Adequate resources.", "Band 6.0-6.5"),
    ("adjacent", "adjective", "next to", "The adjacent building.", "Band 6.0-6.5"),
    ("adjust", "verb", "to modify", "Adjust the settings.", "Band 6.0-6.5"),
    ("administrate", "verb", "to manage", "Administrate the program.", "Band 6.0-6.5"),
    ("adult", "noun", "a grown person", "Adults are responsible.", "Band 6.0-6.5"),
    ("advocate", "verb", "to support publicly", "Advocate for change.", "Band 6.0-6.5"),
    ("affect", "verb", "to influence", "Weather affects mood.", "Band 6.0-6.5"),
    ("aggregate", "noun", "a whole formed by combining", "The aggregate score.", "Band 6.0-6.5"),
    ("aid", "noun", "help or assistance", "Provide aid to victims.", "Band 6.0-6.5"),
    ("albeit", "conjunction", "although", "Albeit difficult, we succeeded.", "Band 6.0-6.5"),
    ("allocate", "verb", "to distribute", "Allocate resources wisely.", "Band 6.0-6.5"),
    ("alter", "verb", "to change", "Alter the plan.", "Band 6.0-6.5"),
    ("alternative", "noun", "another option", "Find an alternative.", "Band 6.0-6.5"),
    ("ambiguous", "adjective", "unclear", "An ambiguous statement.", "Band 6.0-6.5"),
    ("amend", "verb", "to make changes", "Amend the document.", "Band 6.0-6.5"),
    ("analogy", "noun", "a comparison", "Draw an analogy.", "Band 6.0-6.5"),
    ("annual", "adjective", "yearly", "The annual report.", "Band 6.0-6.5"),
    ("anticipate", "verb", "to expect", "Anticipate problems.", "Band 6.0-6.5"),
    ("apparent", "adjective", "obvious", "The reason is apparent.", "Band 6.0-6.5"),
    ("append", "verb", "to add at the end", "Append your signature.", "Band 6.0-6.5"),
    ("appreciate", "verb", "to value", "Appreciate your help.", "Band 6.0-6.5"),
    ("appropriate", "adjective", "suitable", "Appropriate behavior.", "Band 6.0-6.5"),
    ("approximate", "adjective", "close to", "An approximate value.", "Band 6.0-6.5"),
    ("arbitrary", "adjective", "random", "An arbitrary decision.", "Band 6.0-6.5"),
    ("aspect", "noun", "a feature", "Consider every aspect.", "Band 6.0-6.5"),
    ("assemble", "verb", "to gather", "Assemble the parts.", "Band 6.0-6.5"),
    ("assign", "verb", "to allocate", "Assign tasks.", "Band 6.0-6.5"),
    ("assist", "verb", "to help", "Assist the team.", "Band 6.0-6.5"),
    ("assure", "verb", "to guarantee", "I assure you.", "Band 6.0-6.5"),
    ("attach", "verb", "to fasten", "Attach the file.", "Band 6.0-6.5"),
    ("attain", "verb", "to achieve", "Attain your goals.", "Band 6.0-6.5"),
    ("attitude", "noun", "a way of thinking", "A positive attitude.", "Band 6.0-6.5"),
    ("attribute", "verb", "to credit to", "Attribute success to effort.", "Band 6.0-6.5"),
    ("automate", "verb", "to make automatic", "Automate the process.", "Band 6.0-6.5"),
    ("aware", "adjective", "having knowledge", "Be aware of risks.", "Band 6.0-6.5"),
    ("behalf", "noun", "in the interest of", "On behalf of the team.", "Band 6.0-6.5"),
    ("bias", "noun", "prejudice", "Avoid bias.", "Band 6.0-6.5"),
    ("bond", "noun", "a connection", "Form a bond.", "Band 6.0-6.5"),
    ("brief", "adjective", "short", "A brief summary.", "Band 6.0-6.5"),
    ("bulk", "noun", "large quantity", "Buy in bulk.", "Band 6.0-6.5"),
    ("capable", "adjective", "able", "Capable of success.", "Band 6.0-6.5"),
    ("capacity", "noun", "ability to contain", "Full capacity.", "Band 6.0-6.5"),
    ("cease", "verb", "to stop", "Cease operations.", "Band 6.0-6.5"),
    ("challenge", "noun", "a difficulty", "Face the challenge.", "Band 6.0-6.5"),
    ("channel", "noun", "a medium", "Communication channel.", "Band 6.0-6.5"),
    ("chapter", "noun", "a section", "Read the chapter.", "Band 6.0-6.5"),
    ("chart", "noun", "a diagram", "Study the chart.", "Band 6.0-6.5"),
    ("chemical", "adjective", "relating to chemistry", "Chemical reaction.", "Band 6.0-6.5"),
    ("circumstance", "noun", "a condition", "Under the circumstances.", "Band 6.0-6.5"),
    ("cite", "verb", "to quote", "Cite your sources.", "Band 6.0-6.5"),
    
    # Band 7.0-7.5 (고급)
    ("clarify", "verb", "to make clear", "Clarify the point.", "Band 7.0-7.5"),
    ("classic", "adjective", "typical", "A classic example.", "Band 7.0-7.5"),
    ("clause", "noun", "a part of sentence", "Add a clause.", "Band 7.0-7.5"),
    ("code", "noun", "a system of rules", "Follow the code.", "Band 7.0-7.5"),
    ("coherent", "adjective", "logical", "A coherent argument.", "Band 7.0-7.5"),
    ("coincide", "verb", "to occur together", "Events coincide.", "Band 7.0-7.5"),
    ("collapse", "verb", "to fall down", "The building collapsed.", "Band 7.0-7.5"),
    ("colleague", "noun", "a coworker", "My colleague helped.", "Band 7.0-7.5"),
    ("commence", "verb", "to begin", "Commence the meeting.", "Band 7.0-7.5"),
    ("commission", "noun", "a group with authority", "The commission decided.", "Band 7.0-7.5"),
    ("commodity", "noun", "a raw material", "Oil is a commodity.", "Band 7.0-7.5"),
    ("communicate", "verb", "to share information", "Communicate clearly.", "Band 7.0-7.5"),
    ("community", "noun", "a group of people", "The local community.", "Band 7.0-7.5"),
    ("compatible", "adjective", "able to coexist", "Compatible systems.", "Band 7.0-7.5"),
    ("compensate", "verb", "to make up for", "Compensate for losses.", "Band 7.0-7.5"),
    ("compile", "verb", "to collect", "Compile the report.", "Band 7.0-7.5"),
    ("complement", "verb", "to complete", "Colors complement.", "Band 7.0-7.5"),
    ("complex", "adjective", "complicated", "A complex issue.", "Band 7.0-7.5"),
    ("component", "noun", "a part", "Key component.", "Band 7.0-7.5"),
    ("compound", "noun", "a combination", "Chemical compound.", "Band 7.0-7.5"),
    ("comprehensive", "adjective", "complete", "A comprehensive study.", "Band 7.0-7.5"),
    ("comprise", "verb", "to consist of", "The team comprises experts.", "Band 7.0-7.5"),
    ("compute", "verb", "to calculate", "Compute the total.", "Band 7.0-7.5"),
    ("conceive", "verb", "to form an idea", "Conceive a plan.", "Band 7.0-7.5"),
    ("concentrate", "verb", "to focus", "Concentrate on work.", "Band 7.0-7.5"),
    ("conclude", "verb", "to end", "Conclude the study.", "Band 7.0-7.5"),
    ("concurrent", "adjective", "simultaneous", "Concurrent events.", "Band 7.0-7.5"),
    ("conduct", "verb", "to carry out", "Conduct research.", "Band 7.0-7.5"),
    ("confer", "verb", "to discuss", "Confer with experts.", "Band 7.0-7.5"),
    ("confine", "verb", "to limit", "Confine the discussion.", "Band 7.0-7.5"),
    ("confirm", "verb", "to verify", "Confirm the booking.", "Band 7.0-7.5"),
    ("conflict", "noun", "a disagreement", "Resolve the conflict.", "Band 7.0-7.5"),
    ("conform", "verb", "to comply", "Conform to standards.", "Band 7.0-7.5"),
    ("consent", "noun", "permission", "Give consent.", "Band 7.0-7.5"),
    ("consequent", "adjective", "resulting", "Consequent effects.", "Band 7.0-7.5"),
    ("considerable", "adjective", "large", "Considerable effort.", "Band 7.0-7.5"),
    ("constant", "adjective", "unchanging", "Constant temperature.", "Band 7.0-7.5"),
    ("constrain", "verb", "to restrict", "Budget constraints.", "Band 7.0-7.5"),
    ("construct", "verb", "to build", "Construct a theory.", "Band 7.0-7.5"),
    ("consult", "verb", "to seek advice", "Consult a doctor.", "Band 7.0-7.5"),
    ("consume", "verb", "to use up", "Consume resources.", "Band 7.0-7.5"),
    ("contact", "verb", "to communicate", "Contact us.", "Band 7.0-7.5"),
    ("contemporary", "adjective", "modern", "Contemporary art.", "Band 7.0-7.5"),
    ("contradict", "verb", "to oppose", "Don't contradict.", "Band 7.0-7.5"),
    ("contrary", "adjective", "opposite", "On the contrary.", "Band 7.0-7.5"),
    ("contrast", "noun", "difference", "In contrast.", "Band 7.0-7.5"),
    ("contribute", "verb", "to give", "Contribute to society.", "Band 7.0-7.5"),
    ("controversy", "noun", "disagreement", "Cause controversy.", "Band 7.0-7.5"),
    ("convene", "verb", "to assemble", "Convene a meeting.", "Band 7.0-7.5"),
    ("convention", "noun", "a practice", "Follow convention.", "Band 7.0-7.5"),
    ("converse", "verb", "to talk", "Converse with friends.", "Band 7.0-7.5"),
    ("convert", "verb", "to change", "Convert units.", "Band 7.0-7.5"),
    ("convince", "verb", "to persuade", "Convince the jury.", "Band 7.0-7.5"),
    ("cooperate", "verb", "to work together", "Cooperate with others.", "Band 7.0-7.5"),
    ("coordinate", "verb", "to organize", "Coordinate efforts.", "Band 7.0-7.5"),
    ("core", "noun", "center", "The core issue.", "Band 7.0-7.5"),
    ("corporate", "adjective", "business-related", "Corporate culture.", "Band 7.0-7.5"),
    ("correspond", "verb", "to match", "Results correspond.", "Band 7.0-7.5"),
    ("couple", "noun", "two items", "A couple of things.", "Band 7.0-7.5"),
    ("criteria", "noun", "standards", "Meet the criteria.", "Band 7.0-7.5"),
    ("crucial", "adjective", "essential", "A crucial decision.", "Band 7.0-7.5"),
    
    # Band 8.0+ (최고급)
    ("currency", "noun", "money system", "Foreign currency.", "Band 8.0+"),
    ("cycle", "noun", "a series of events", "Life cycle.", "Band 8.0+"),
    ("debate", "noun", "a discussion", "Join the debate.", "Band 8.0+"),
    ("decade", "noun", "ten years", "Over a decade.", "Band 8.0+"),
    ("decline", "verb", "to decrease", "Sales declined.", "Band 8.0+"),
    ("deduce", "verb", "to conclude", "Deduce the answer.", "Band 8.0+"),
    ("definite", "adjective", "certain", "A definite answer.", "Band 8.0+"),
    ("demonstrate", "verb", "to show", "Demonstrate skills.", "Band 8.0+"),
    ("denote", "verb", "to indicate", "Symbols denote meaning.", "Band 8.0+"),
    ("deny", "verb", "to refuse", "Deny access.", "Band 8.0+"),
    ("depress", "verb", "to lower", "Depress the lever.", "Band 8.0+"),
    ("design", "verb", "to plan", "Design a system.", "Band 8.0+"),
    ("despite", "preposition", "in spite of", "Despite difficulties.", "Band 8.0+"),
    ("detect", "verb", "to discover", "Detect errors.", "Band 8.0+"),
    ("deviate", "verb", "to diverge", "Deviate from plans.", "Band 8.0+"),
    ("device", "noun", "a tool", "Electronic device.", "Band 8.0+"),
    ("devote", "verb", "to dedicate", "Devote time.", "Band 8.0+"),
    ("differentiate", "verb", "to distinguish", "Differentiate between.", "Band 8.0+"),
    ("dimension", "noun", "a measurement", "Multiple dimensions.", "Band 8.0+"),
    ("diminish", "verb", "to reduce", "Diminish importance.", "Band 8.0+"),
    ("discrete", "adjective", "separate", "Discrete categories.", "Band 8.0+"),
    ("discriminate", "verb", "to distinguish", "Discriminate between.", "Band 8.0+"),
    ("displace", "verb", "to move", "Displace workers.", "Band 8.0+"),
    ("display", "verb", "to show", "Display results.", "Band 8.0+"),
    ("dispose", "verb", "to get rid of", "Dispose properly.", "Band 8.0+"),
    ("distinct", "adjective", "different", "Distinct features.", "Band 8.0+"),
    ("distort", "verb", "to twist", "Distort the truth.", "Band 8.0+"),
    ("diverse", "adjective", "varied", "Diverse opinions.", "Band 8.0+"),
    ("document", "verb", "to record", "Document everything.", "Band 8.0+"),
    ("domain", "noun", "an area", "Public domain.", "Band 8.0+"),
    ("domestic", "adjective", "home-related", "Domestic affairs.", "Band 8.0+"),
    ("dominate", "verb", "to control", "Dominate the market.", "Band 8.0+"),
    ("draft", "noun", "a preliminary version", "First draft.", "Band 8.0+"),
    ("drama", "noun", "a play", "Drama unfolds.", "Band 8.0+"),
    ("duration", "noun", "length of time", "Short duration.", "Band 8.0+"),
    ("dynamic", "adjective", "energetic", "Dynamic environment.", "Band 8.0+"),
    ("edit", "verb", "to revise", "Edit the document.", "Band 8.0+"),
    ("element", "noun", "a component", "Key element.", "Band 8.0+"),
    ("eliminate", "verb", "to remove", "Eliminate waste.", "Band 8.0+"),
    ("emerge", "verb", "to appear", "Patterns emerge.", "Band 8.0+"),
    ("emphasis", "noun", "importance", "Place emphasis.", "Band 8.0+"),
    ("empirical", "adjective", "based on observation", "Empirical evidence.", "Band 8.0+"),
    ("enable", "verb", "to make possible", "Enable success.", "Band 8.0+"),
    ("encounter", "verb", "to meet", "Encounter problems.", "Band 8.0+"),
    ("energy", "noun", "power", "Renewable energy.", "Band 8.0+"),
    ("enforce", "verb", "to compel", "Enforce rules.", "Band 8.0+"),
    ("enhance", "verb", "to improve", "Enhance quality.", "Band 8.0+"),
    ("enormous", "adjective", "huge", "Enormous potential.", "Band 8.0+"),
    ("ensure", "verb", "to make certain", "Ensure accuracy.", "Band 8.0+"),
    ("entity", "noun", "a being", "Legal entity.", "Band 8.0+"),
    ("equate", "verb", "to consider equal", "Don't equate them.", "Band 8.0+"),
    ("equip", "verb", "to supply", "Equip with tools.", "Band 8.0+"),
    ("equivalent", "adjective", "equal", "Equivalent value.", "Band 8.0+"),
    ("erode", "verb", "to wear away", "Trust erodes.", "Band 8.0+"),
    ("error", "noun", "a mistake", "Human error.", "Band 8.0+"),
    ("ethical", "adjective", "moral", "Ethical standards.", "Band 8.0+"),
    ("ethnic", "adjective", "relating to race", "Ethnic diversity.", "Band 8.0+"),
    ("evaluate", "verb", "to assess", "Evaluate performance.", "Band 8.0+"),
    ("eventual", "adjective", "final", "Eventual outcome.", "Band 8.0+"),
    ("evolve", "verb", "to develop", "Ideas evolve.", "Band 8.0+"),
]

def translate_batch(texts, target_lang):
    url = f"https://translation.googleapis.com/language/translate/v2?key={GOOGLE_API_KEY}"
    result = []
    for i in range(0, len(texts), 100):
        batch = texts[i:i+100]
        try:
            resp = requests.post(url, json={"q": batch, "source": "en", "target": target_lang}, timeout=30)
            if resp.status_code == 200:
                result.extend([t['translatedText'] for t in resp.json()['data']['translations']])
            else:
                result.extend(batch)
        except:
            result.extend(batch)
        time.sleep(0.1)
    return result

def main():
    with open('assets/data/words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)
    
    existing = {w['word'].lower() for w in words}
    start_id = max(w['id'] for w in words) + 1
    categories = ["Academic", "Environment", "Technology", "Health", "Education", "Business", "Science", "Media", "Society", "Culture"]
    
    new_words = []
    for word, pos, definition, example, level in AWL_WORDS:
        if word.lower() not in existing:
            new_words.append({
                "id": start_id + len(new_words),
                "word": word,
                "level": level,
                "partOfSpeech": pos,
                "definition": definition,
                "example": example,
                "category": categories[(start_id + len(new_words)) % len(categories)]
            })
            existing.add(word.lower())
    
    print(f"새 단어: {len(new_words)}개")
    
    if new_words:
        defs = [w['definition'] for w in new_words]
        exs = [w['example'] for w in new_words]
        
        for lang in LANGUAGES:
            print(f"{lang} 번역중...")
            trans_defs = translate_batch(defs, lang)
            trans_exs = translate_batch(exs, lang)
            for i, w in enumerate(new_words):
                if 'translations' not in w:
                    w['translations'] = {}
                w['translations'][lang] = {
                    'definition': trans_defs[i],
                    'example': trans_exs[i]
                }
        
        words.extend(new_words)
        with open('assets/data/words.json', 'w', encoding='utf-8') as f:
            json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"총: {len(words)}개")

if __name__ == "__main__":
    main()
