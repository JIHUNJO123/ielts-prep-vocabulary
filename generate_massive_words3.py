#!/usr/bin/env python3
"""
IELTS 단어 추가 생성 스크립트 3 - 5000개 목표 달성
"""

import json
import os

# 기존 단어 로드
def load_existing_words():
    existing = set()
    for filename in ['band45_words.json', 'band60_words.json', 'band70_words.json', 'band80_words.json']:
        filepath = f'assets/data/{filename}'
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for w in data:
                    existing.add(w['word'].lower())
    return existing

existing_words = load_existing_words()
print(f"기존 단어 수: {len(existing_words)}개")

# =====================================================================
# BAND 6.0-6.5 추가 단어 - Part 3 (가장 많이 필요)
# =====================================================================
BAND60_PART3 = [
    # Academic Writing Words
    ("aforementioned", "adjective", "previously mentioned", "The aforementioned points are crucial."),
    ("albeit", "conjunction", "although", "He continued, albeit reluctantly."),
    ("analogous", "adjective", "comparable in certain respects", "The situation is analogous."),
    ("arguably", "adverb", "it may be argued", "This is arguably the best solution."),
    ("assertion", "noun", "a confident statement", "The assertion requires evidence."),
    ("attributed", "adjective", "regarded as caused by", "The success was attributed to teamwork."),
    ("commenced", "verb", "began", "The project commenced last month."),
    ("compatible", "adjective", "able to exist together", "The systems are compatible."),
    ("comprised", "verb", "consisted of", "The team comprised five members."),
    ("concurrent", "adjective", "existing at the same time", "Concurrent events occurred."),
    ("conducive", "adjective", "making something possible", "Conditions conducive to growth."),
    ("constitutes", "verb", "makes up", "This constitutes a majority."),
    ("constraints", "noun", "limitations or restrictions", "Budget constraints limit options."),
    ("contrary", "adjective", "opposite in nature", "Contrary to popular belief."),
    ("conversely", "adverb", "in an opposite way", "Conversely, the data shows."),
    
    # Research & Study Terms
    ("correlation", "noun", "a relationship between variables", "A strong correlation exists."),
    ("crucial", "adjective", "of great importance", "This is a crucial point."),
    ("data", "noun", "facts and statistics", "Analyze the data carefully."),
    ("decline", "noun", "a gradual decrease", "A decline in sales occurred."),
    ("demonstrate", "verb", "clearly show", "The study demonstrates the effect."),
    ("denote", "verb", "be a sign of", "Red circles denote errors."),
    ("derived", "adjective", "obtained from a source", "Data derived from surveys."),
    ("detected", "verb", "discovered or noticed", "No errors were detected."),
    ("deviate", "verb", "depart from a norm", "Don't deviate from the plan."),
    ("diminish", "verb", "make or become less", "Interest may diminish over time."),
    ("discrete", "adjective", "individually separate", "Three discrete categories exist."),
    ("disparity", "noun", "a great difference", "Income disparity is growing."),
    ("displacement", "noun", "the moving of something", "Population displacement occurred."),
    ("distortion", "noun", "a change in shape or form", "Avoid data distortion."),
    ("distribution", "noun", "the way things are spread", "Wealth distribution varies."),
    
    # Formal Verbs
    ("elaborate", "verb", "develop in detail", "Please elaborate on your point."),
    ("emerge", "verb", "become apparent", "New patterns emerge from data."),
    ("emphasize", "verb", "give special importance to", "Emphasize the key points."),
    ("enable", "verb", "make possible", "Technology enables progress."),
    ("encounter", "verb", "unexpectedly face", "We may encounter problems."),
    ("enhance", "verb", "intensify or improve", "Enhance your skills."),
    ("ensure", "verb", "make certain", "Ensure accuracy in reports."),
    ("entail", "verb", "involve as a consequence", "The job entails travel."),
    ("equivalence", "noun", "the condition of being equal", "Achieve equivalence."),
    ("erosion", "noun", "gradual destruction", "Erosion of public trust."),
    ("exceed", "verb", "be greater than", "Results exceed expectations."),
    ("exhibit", "verb", "display or show", "The data exhibits trends."),
    ("expansion", "noun", "the action of becoming larger", "Market expansion occurred."),
    ("exploitation", "noun", "the action of using unfairly", "Exploitation of resources."),
    ("exposure", "noun", "the state of being exposed", "Exposure to new ideas."),
    
    # Describing Data & Trends
    ("fluctuation", "noun", "irregular rising and falling", "Price fluctuations are normal."),
    ("framework", "noun", "a basic structure", "A theoretical framework."),
    ("furthermore", "adverb", "in addition", "Furthermore, the study shows."),
    ("gradual", "adjective", "taking place slowly", "A gradual increase occurred."),
    ("hence", "adverb", "as a consequence", "Hence, we conclude."),
    ("hierarchical", "adjective", "arranged in order of rank", "A hierarchical structure."),
    ("identical", "adjective", "exactly alike", "The results are identical."),
    ("ideology", "noun", "a system of ideas", "Political ideology varies."),
    ("illustration", "noun", "an example serving to clarify", "By way of illustration."),
    ("impact", "noun", "a marked effect", "The impact was significant."),
    ("implementation", "noun", "the process of putting into effect", "Policy implementation."),
    ("implication", "noun", "a likely consequence", "The implications are serious."),
    ("incidence", "noun", "the occurrence of something", "The incidence of disease."),
    ("inclination", "noun", "a tendency to act", "A natural inclination."),
    ("inconsistency", "noun", "the fact of being inconsistent", "Data inconsistency found."),
    
    # Analysis Words
    ("increment", "noun", "an increase", "Salary increments annually."),
    ("index", "noun", "a measure of change", "The price index rose."),
    ("indication", "noun", "a sign or piece of information", "An indication of progress."),
    ("induce", "verb", "succeed in persuading", "What induced the change?"),
    ("inevitable", "adjective", "certain to happen", "Change is inevitable."),
    ("inference", "noun", "a conclusion reached", "Draw inferences from data."),
    ("inherent", "adjective", "existing as a basic quality", "An inherent problem."),
    ("inhibit", "verb", "hinder or restrain", "Fear inhibits progress."),
    ("initial", "adjective", "occurring at the beginning", "Initial results are positive."),
    ("innovation", "noun", "a new method or idea", "Encourage innovation."),
    ("input", "noun", "what is put in", "User input is required."),
    ("insertion", "noun", "the action of inserting", "Data insertion completed."),
    ("insight", "noun", "deep understanding", "Valuable insights emerged."),
    ("inspection", "noun", "careful examination", "Regular inspection required."),
    ("instance", "noun", "an example or occurrence", "For instance, consider this."),
    
    # More Academic Terms
    ("integral", "adjective", "essential or fundamental", "An integral part of the system."),
    ("integrity", "noun", "the quality of being honest", "Maintain data integrity."),
    ("intensify", "verb", "become more intense", "Efforts must intensify."),
    ("interaction", "noun", "reciprocal action", "User interaction is key."),
    ("intermediate", "adjective", "between two extremes", "An intermediate level."),
    ("internal", "adjective", "inside", "Internal processes are complex."),
    ("interpretation", "noun", "the action of explaining", "Data interpretation varies."),
    ("intervention", "noun", "the action of intervening", "Government intervention helped."),
    ("intrinsic", "adjective", "belonging naturally", "Intrinsic value."),
    ("investigation", "noun", "formal inquiry", "The investigation continues."),
    ("invoke", "verb", "cite as an authority", "Invoke the regulations."),
    ("isolation", "noun", "the process of isolating", "Social isolation affects health."),
    ("justification", "noun", "the action of showing to be right", "Provide justification."),
    ("label", "noun", "a classifying phrase", "Apply the correct label."),
    ("layer", "noun", "a sheet of material", "Multiple layers of complexity."),
    
    # Social & Political Terms
    ("legislation", "noun", "laws collectively", "New legislation passed."),
    ("levy", "noun", "an imposed tax", "A levy on imports."),
    ("liberal", "adjective", "open to new ideas", "A liberal education."),
    ("licence", "noun", "official permission", "Obtain a licence."),
    ("likewise", "adverb", "in the same way", "Likewise, the second group."),
    ("linkage", "noun", "the action of linking", "Establish linkages."),
    ("location", "noun", "a particular place", "The location is ideal."),
    ("logic", "noun", "reasoning conducted according to rules", "Follow the logic."),
    ("maintenance", "noun", "the process of maintaining", "System maintenance required."),
    ("manipulation", "noun", "the action of handling", "Data manipulation is unethical."),
    ("marginal", "adjective", "minor and not important", "Marginal improvements only."),
    ("mature", "adjective", "fully developed", "A mature market."),
    ("mechanism", "noun", "a system of parts", "The mechanism is complex."),
    ("mediation", "noun", "intervention to resolve a dispute", "Seek mediation."),
    ("medium", "noun", "a means of communication", "Social media is a powerful medium."),
    
    # Professional Terms
    ("methodology", "noun", "a system of methods", "Research methodology."),
    ("migration", "noun", "movement from one place to another", "Mass migration occurred."),
    ("minimal", "adjective", "of a minimum amount", "Minimal impact expected."),
    ("minimise", "verb", "reduce to the smallest amount", "Minimise risks."),
    ("modification", "noun", "the action of modifying", "Slight modifications needed."),
    ("monitoring", "noun", "observing and checking", "Continuous monitoring required."),
    ("motivation", "noun", "the reason for acting", "Strong motivation drives success."),
    ("mutual", "adjective", "experienced by both", "Mutual respect is important."),
    ("negative", "adjective", "showing the absence of", "Negative results obtained."),
    ("network", "noun", "an interconnected group", "Build a professional network."),
    ("neutral", "adjective", "not supporting either side", "Remain neutral."),
    ("nevertheless", "adverb", "in spite of that", "Nevertheless, we continued."),
    ("notwithstanding", "preposition", "in spite of", "Notwithstanding the challenges."),
    ("nuclear", "adjective", "relating to the nucleus", "Nuclear energy."),
    ("objective", "noun", "a thing aimed at", "Achieve your objectives."),
    
    # Environment & Science
    ("obvious", "adjective", "easily perceived", "The solution is obvious."),
    ("occupation", "noun", "a job or profession", "What is your occupation?"),
    ("occurrence", "noun", "an incident or event", "A rare occurrence."),
    ("offset", "verb", "counteract by having an opposite effect", "Offset the costs."),
    ("ongoing", "adjective", "continuing", "An ongoing project."),
    ("option", "noun", "a thing that may be chosen", "Consider all options."),
    ("orientation", "noun", "position relative to surroundings", "Market orientation."),
    ("outcome", "noun", "the way a thing turns out", "A positive outcome."),
    ("output", "noun", "the amount produced", "Increase output."),
    ("overall", "adjective", "taking everything into account", "The overall effect."),
    ("overlap", "verb", "extend over and partly cover", "Responsibilities overlap."),
    ("overseas", "adjective", "in a foreign country", "Overseas markets."),
    ("panel", "noun", "a small group assembled for discussion", "An expert panel."),
    ("paradigm", "noun", "a typical example or pattern", "A paradigm shift."),
    ("parallel", "adjective", "side by side", "Parallel developments occurred."),
    
    # Final Set for Band 6.0-6.5
    ("partnership", "noun", "the state of being a partner", "Form a partnership."),
    ("passive", "adjective", "accepting without resistance", "A passive approach."),
    ("perceive", "verb", "become aware of", "Perceive the difference."),
    ("percentage", "noun", "a rate or proportion", "A high percentage."),
    ("period", "noun", "a length of time", "Over a period of years."),
    ("persistent", "adjective", "continuing firmly", "Persistent efforts paid off."),
    ("perspective", "noun", "a particular attitude", "From a different perspective."),
    ("phase", "noun", "a distinct period", "The first phase completed."),
    ("physical", "adjective", "relating to the body", "Physical activity is important."),
    ("policy", "noun", "a course of action", "Government policy changed."),
    ("portion", "noun", "a part of a whole", "A significant portion."),
    ("pose", "verb", "present or constitute", "This poses a challenge."),
    ("positive", "adjective", "consisting in the presence of", "Positive results achieved."),
    ("potential", "noun", "latent qualities that may be developed", "Realize your potential."),
    ("practitioner", "noun", "a person actively engaged", "A medical practitioner."),
]

# =====================================================================
# BAND 7.0-7.5 추가 단어 - Part 2
# =====================================================================
BAND70_PART2 = [
    # Sophisticated Academic Words
    ("antecedent", "noun", "a thing that existed before", "Historical antecedents."),
    ("antipathy", "noun", "a deep-seated feeling of dislike", "Antipathy towards change."),
    ("apportion", "verb", "divide and distribute", "Apportion the resources fairly."),
    ("archaic", "adjective", "very old or old-fashioned", "Archaic language."),
    ("arduous", "adjective", "involving great exertion", "An arduous journey."),
    ("articulate", "adjective", "expressing oneself readily and clearly", "An articulate speaker."),
    ("ascribe", "verb", "attribute to a cause", "Ascribe the success to hard work."),
    ("aspire", "verb", "direct one's hopes towards", "Aspire to greatness."),
    ("authenticate", "verb", "prove to be genuine", "Authenticate the documents."),
    ("autonomy", "noun", "the right to self-government", "Regional autonomy."),
    ("benchmark", "noun", "a standard or point of reference", "Set a benchmark."),
    ("benign", "adjective", "gentle and kind", "A benign tumor."),
    ("bilateral", "adjective", "involving two parties", "A bilateral agreement."),
    ("burgeon", "verb", "begin to grow or increase rapidly", "The industry burgeoned."),
    ("catalyst", "noun", "a person or thing that precipitates an event", "A catalyst for change."),
    
    # Legal & Formal Terms
    ("cessation", "noun", "the fact of ending", "The cessation of hostilities."),
    ("circumvent", "verb", "find a way around", "Circumvent the regulations."),
    ("coerce", "verb", "persuade using force or threats", "Coerced into signing."),
    ("coherence", "noun", "the quality of being logical", "Textual coherence is important."),
    ("collaborate", "verb", "work jointly on an activity", "Collaborate on the project."),
    ("collateral", "adjective", "secondary; accompanying", "Collateral damage."),
    ("compel", "verb", "force or oblige", "Compelled to act."),
    ("competence", "noun", "the ability to do something", "Demonstrate competence."),
    ("complement", "verb", "add to in a way that enhances", "The colors complement each other."),
    ("compliance", "noun", "the action of complying", "Ensure compliance with regulations."),
    ("concede", "verb", "admit that something is true", "He conceded the point."),
    ("conceive", "verb", "form or devise in the mind", "Conceive a plan."),
    ("confer", "verb", "grant or bestow", "Confer a degree."),
    ("confine", "verb", "keep within certain limits", "Confine the discussion."),
    ("conform", "verb", "comply with rules or standards", "Conform to expectations."),
    
    # Research & Analysis
    ("conjecture", "noun", "an opinion based on incomplete information", "Mere conjecture."),
    ("consensus", "noun", "general agreement", "Reach a consensus."),
    ("consolidate", "verb", "make stronger or more solid", "Consolidate gains."),
    ("constrain", "verb", "severely restrict", "Constrained by resources."),
    ("contemplate", "verb", "think about carefully", "Contemplate the options."),
    ("contend", "verb", "struggle to surmount", "Contend with difficulties."),
    ("contingent", "adjective", "dependent on certain conditions", "Contingent on approval."),
    ("contradict", "verb", "deny the truth of", "The evidence contradicts the claim."),
    ("contravene", "verb", "violate a law or agreement", "Contravene regulations."),
    ("converge", "verb", "come together from different directions", "Views converge."),
    ("convey", "verb", "make known", "Convey the message clearly."),
    ("correspond", "verb", "have a close similarity", "The data corresponds."),
    ("counterpart", "noun", "a person or thing with the same function", "Meet your counterpart."),
    ("criterion", "noun", "a principle or standard", "A key criterion."),
    ("culminate", "verb", "reach a climax", "Efforts culminated in success."),
    
    # High-Level Adjectives
    ("decisive", "adjective", "settling an issue", "A decisive victory."),
    ("deficient", "adjective", "not having enough", "Nutritionally deficient."),
    ("definitive", "adjective", "decisive or authoritative", "The definitive answer."),
    ("deliberate", "adjective", "done consciously and intentionally", "A deliberate choice."),
    ("detrimental", "adjective", "tending to cause harm", "Detrimental effects."),
    ("devoid", "adjective", "entirely lacking", "Devoid of meaning."),
    ("discernible", "adjective", "able to be perceived", "A discernible pattern."),
    ("discreet", "adjective", "careful and prudent", "Be discreet."),
    ("disparate", "adjective", "essentially different", "Disparate views."),
    ("distinct", "adjective", "recognizably different", "Two distinct categories."),
    ("distort", "verb", "give a misleading account of", "Don't distort the facts."),
    ("diverge", "verb", "separate from a common path", "Opinions diverge."),
    ("dominant", "adjective", "most important or powerful", "The dominant view."),
    ("dynamic", "adjective", "characterized by constant change", "A dynamic environment."),
    ("elicit", "verb", "evoke or draw out", "Elicit a response."),
    
    # Process & Action Words
    ("embark", "verb", "begin a course of action", "Embark on a new project."),
    ("embody", "verb", "be an expression of", "Embody the principles."),
    ("embrace", "verb", "accept willingly", "Embrace change."),
    ("encompass", "verb", "surround and have within", "The plan encompasses all aspects."),
    ("endeavor", "verb", "try hard to do", "Endeavor to succeed."),
    ("enforce", "verb", "compel observance of", "Enforce the rules."),
    ("engage", "verb", "participate or become involved", "Engage with the community."),
    ("engender", "verb", "cause or give rise to", "Engender trust."),
    ("enhance", "verb", "intensify or improve quality", "Enhance performance."),
    ("enlighten", "verb", "give spiritual or intellectual insight", "Enlighten the audience."),
    ("enrich", "verb", "improve the quality of", "Enrich the experience."),
    ("ensue", "verb", "happen as a result", "Chaos ensued."),
    ("entail", "verb", "involve as a necessary part", "What does this entail?"),
    ("envisage", "verb", "contemplate or conceive of", "Envisage the future."),
    ("erode", "verb", "gradually destroy", "Trust was eroded."),
    
    # Final Band 7 Words
    ("escalate", "verb", "increase rapidly", "Tensions escalated."),
    ("evoke", "verb", "bring to mind", "Evoke memories."),
    ("exacerbate", "verb", "make worse", "Exacerbate the problem."),
    ("exceed", "verb", "be greater than", "Exceed expectations."),
    ("exclude", "verb", "deny access to", "Exclude certain groups."),
    ("exemplify", "verb", "be a typical example of", "This exemplifies the issue."),
    ("exert", "verb", "apply or bring to bear", "Exert influence."),
    ("expedite", "verb", "make happen sooner", "Expedite the process."),
    ("explicit", "adjective", "stated clearly", "Explicit instructions."),
    ("exploit", "verb", "make full use of", "Exploit opportunities."),
    ("expound", "verb", "present and explain systematically", "Expound the theory."),
    ("extract", "verb", "remove or take out", "Extract the data."),
    ("fabricate", "verb", "invent or concoct", "Fabricate evidence."),
    ("facilitate", "verb", "make easier", "Facilitate communication."),
    ("feasible", "adjective", "possible to do easily", "A feasible solution."),
]

# =====================================================================
# BAND 8.0+ 추가 단어 - Part 2
# =====================================================================
BAND80_PART2 = [
    # Extremely Sophisticated Terms
    ("fatuous", "adjective", "silly and pointless", "A fatuous remark."),
    ("feckless", "adjective", "lacking initiative or strength", "A feckless leader."),
    ("felicitous", "adjective", "well chosen or suited", "A felicitous phrase."),
    ("fervent", "adjective", "having passionate intensity", "Fervent supporters."),
    ("fester", "verb", "become worse", "Resentment festered."),
    ("flagrant", "adjective", "conspicuously offensive", "A flagrant violation."),
    ("flout", "verb", "openly disregard a rule", "Flout the regulations."),
    ("foment", "verb", "instigate or stir up", "Foment unrest."),
    ("forbearance", "noun", "patient self-control", "Show forbearance."),
    ("forestall", "verb", "prevent by taking advance action", "Forestall criticism."),
    ("fortuitous", "adjective", "happening by chance", "A fortuitous encounter."),
    ("furtive", "adjective", "attempting to avoid notice", "A furtive glance."),
    ("gainsay", "verb", "deny or contradict", "No one could gainsay him."),
    ("galvanize", "verb", "shock into action", "Galvanize public opinion."),
    ("garrulous", "adjective", "excessively talkative", "A garrulous old man."),
    
    # More Academic Rarities
    ("germane", "adjective", "relevant to a subject", "A germane point."),
    ("grandiloquent", "adjective", "pompous in language", "Grandiloquent speeches."),
    ("gratuitous", "adjective", "uncalled for; lacking reason", "Gratuitous violence."),
    ("gregarious", "adjective", "fond of company", "A gregarious personality."),
    ("gullible", "adjective", "easily persuaded to believe", "Don't be gullible."),
    ("hackneyed", "adjective", "lacking originality", "A hackneyed phrase."),
    ("hapless", "adjective", "unfortunate", "A hapless victim."),
    ("harbinger", "noun", "a person or thing that announces the approach of another", "A harbinger of change."),
    ("hiatus", "noun", "a pause or gap", "A brief hiatus."),
    ("idiosyncratic", "adjective", "relating to individual peculiarity", "An idiosyncratic style."),
    ("ignoble", "adjective", "not honorable", "Ignoble motives."),
    ("illicit", "adjective", "forbidden by law or rules", "Illicit activities."),
    ("imminent", "adjective", "about to happen", "Imminent danger."),
    ("immutable", "adjective", "unchanging over time", "Immutable laws."),
    ("impartial", "adjective", "treating all rivals equally", "An impartial judge."),
    
    # Complex Verbs
    ("impede", "verb", "delay or prevent", "Impede progress."),
    ("impel", "verb", "drive or force", "Impelled to act."),
    ("imperative", "adjective", "of vital importance", "An imperative need."),
    ("impervious", "adjective", "not allowing passage", "Impervious to criticism."),
    ("implacable", "adjective", "unable to be appeased", "An implacable enemy."),
    ("implicate", "verb", "show to be involved in a crime", "Implicate in the scandal."),
    ("implicit", "adjective", "implied though not stated", "An implicit agreement."),
    ("importune", "verb", "harass with persistent requests", "Importuned for money."),
    ("impugn", "verb", "dispute the truth of", "Impugn their motives."),
    ("impute", "verb", "attribute to a cause", "Impute blame."),
    ("inadvertent", "adjective", "not resulting from deliberate intent", "An inadvertent error."),
    ("incipient", "adjective", "in an initial stage", "An incipient problem."),
    ("incontrovertible", "adjective", "not able to be denied", "Incontrovertible evidence."),
    ("incorrigible", "adjective", "not able to be corrected", "An incorrigible optimist."),
    ("incumbent", "adjective", "necessary as a duty", "It is incumbent upon us."),
    
    # Final Advanced Words
    ("indeterminate", "adjective", "not exactly known", "An indeterminate period."),
    ("indigenous", "adjective", "originating in a particular place", "Indigenous peoples."),
    ("indolent", "adjective", "wanting to avoid activity", "An indolent lifestyle."),
    ("inefficacious", "adjective", "not producing the desired effect", "An inefficacious remedy."),
    ("ineluctable", "adjective", "unable to be resisted", "An ineluctable conclusion."),
    ("inexplicable", "adjective", "unable to be explained", "Inexplicable behavior."),
    ("infallible", "adjective", "incapable of making mistakes", "No one is infallible."),
    ("ingenuous", "adjective", "innocent and unsuspecting", "An ingenuous young man."),
    ("inimitable", "adjective", "so good as to be impossible to copy", "Her inimitable style."),
    ("innate", "adjective", "inborn; natural", "An innate ability."),
    ("innocuous", "adjective", "not harmful or offensive", "An innocuous remark."),
    ("inscrutable", "adjective", "impossible to understand", "An inscrutable expression."),
    ("insinuate", "verb", "suggest or hint in an unpleasant way", "Insinuate wrongdoing."),
    ("insipid", "adjective", "lacking flavor or interest", "An insipid performance."),
    ("insolent", "adjective", "showing rude disrespect", "An insolent reply."),
    
    # More Sophisticated Terms
    ("insubstantial", "adjective", "lacking strength and solidity", "Insubstantial evidence."),
    ("insurgent", "noun", "a rebel", "Insurgent forces."),
    ("integral", "adjective", "necessary for completeness", "An integral part."),
    ("interlocutor", "noun", "a person who takes part in a dialogue", "My interlocutor disagreed."),
    ("intractable", "adjective", "hard to control or deal with", "An intractable problem."),
    ("intrepid", "adjective", "fearless; adventurous", "An intrepid explorer."),
    ("inundate", "verb", "overwhelm with things to be dealt with", "Inundated with requests."),
    ("inured", "adjective", "accustomed to something unpleasant", "Inured to hardship."),
    ("inveigle", "verb", "persuade by flattery or deception", "Inveigle into participating."),
    ("inveterate", "adjective", "having a habit that is unlikely to change", "An inveterate liar."),
    ("invidious", "adjective", "likely to arouse resentment", "An invidious comparison."),
    ("irascible", "adjective", "having a tendency to be easily angered", "An irascible temperament."),
    ("irrefutable", "adjective", "impossible to deny or disprove", "Irrefutable proof."),
    ("irreproachable", "adjective", "beyond criticism", "Irreproachable conduct."),
    ("itinerant", "adjective", "traveling from place to place", "An itinerant worker."),
]

def create_word_entry(word, pos, definition, example, level, word_id):
    return {
        "id": word_id,
        "word": word,
        "level": level,
        "partOfSpeech": pos,
        "definition": definition,
        "example": example,
        "translations": {
            "ko": {"definition": "", "example": ""},
            "ja": {"definition": "", "example": ""},
            "zh": {"definition": "", "example": ""},
            "es": {"definition": "", "example": ""},
            "de": {"definition": "", "example": ""},
            "fr": {"definition": "", "example": ""},
            "pt": {"definition": "", "example": ""},
            "vi": {"definition": "", "example": ""},
            "ar": {"definition": "", "example": ""}
        }
    }

def add_words_to_file(filename, new_words_list, level):
    filepath = f'assets/data/{filename}'
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = []
    
    existing_word_set = set(w['word'].lower() for w in existing_data)
    max_id = max([w['id'] for w in existing_data], default=0)
    
    added = 0
    for word, pos, definition, example in new_words_list:
        if word.lower() not in existing_word_set and word.lower() not in existing_words:
            max_id += 1
            entry = create_word_entry(word, pos, definition, example, level, max_id)
            existing_data.append(entry)
            existing_word_set.add(word.lower())
            added += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ {filename}: {len(existing_data)}개 (추가: {added}개)")
    return len(existing_data)

print("\n" + "="*50)
print("📚 IELTS 단어 추가 생성 3")
print("="*50 + "\n")

total_band60 = add_words_to_file('band60_words.json', BAND60_PART3, 'Band 6.0-6.5')
total_band70 = add_words_to_file('band70_words.json', BAND70_PART2, 'Band 7.0-7.5')
total_band80 = add_words_to_file('band80_words.json', BAND80_PART2, 'Band 8.0+')

with open('assets/data/band45_words.json', 'r', encoding='utf-8') as f:
    band45_count = len(json.load(f))

print("\n" + "="*50)
print(f"📊 총 단어 현황:")
print(f"   Band 4.5-5.5: {band45_count}개")
print(f"   Band 6.0-6.5: {total_band60}개")
print(f"   Band 7.0-7.5: {total_band70}개")
print(f"   Band 8.0+: {total_band80}개")
print(f"   총계: {band45_count + total_band60 + total_band70 + total_band80}개")
print("="*50)
