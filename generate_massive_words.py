#!/usr/bin/env python3
"""
IELTS 단어 대량 생성 스크립트 - 5000개 목표 달성을 위한 대규모 추가
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
# IELTS BAND 6.0-6.5 단어 대량 추가 (가장 많이 필요)
# =====================================================================
BAND60_MASSIVE = [
    # Academic Vocabulary - Education & Learning
    ("curriculum", "noun", "the subjects in a course of study", "The school has updated its curriculum."),
    ("thesis", "noun", "a long essay involving personal research", "She completed her thesis on climate change."),
    ("hypothesis", "noun", "a proposed explanation for something", "The scientist tested the hypothesis."),
    ("methodology", "noun", "a system of methods used in a study", "The research methodology was sound."),
    ("dissertation", "noun", "a long piece of writing on a particular subject", "He is writing his dissertation."),
    ("seminar", "noun", "a small class for discussion", "We attended a seminar on economics."),
    ("symposium", "noun", "a conference on a particular subject", "The medical symposium attracted many doctors."),
    ("tuition", "noun", "teaching or instruction fees", "University tuition has increased."),
    ("scholarship", "noun", "money given to a student for study", "She won a scholarship to Harvard."),
    ("undergraduate", "noun", "a university student who has not yet taken a first degree", "She is an undergraduate student."),
    ("postgraduate", "noun", "a student who has completed a first degree", "He is a postgraduate researcher."),
    ("academia", "noun", "the environment of colleges and universities", "She chose a career in academia."),
    ("alumni", "noun", "former students of a school or college", "The alumni donated generously."),
    ("faculty", "noun", "the teaching staff of a university", "The faculty voted on the proposal."),
    ("enrollment", "noun", "the act of officially joining a course", "Enrollment begins next week."),
    
    # Science & Technology
    ("phenomenon", "noun", "an observable fact or event", "Global warming is a concerning phenomenon."),
    ("hypothesis", "noun", "a supposition as a starting point", "We need to test this hypothesis."),
    ("variable", "noun", "an element that may change", "Control the variable in the experiment."),
    ("correlation", "noun", "a mutual relationship between things", "There is a correlation between exercise and health."),
    ("parameter", "noun", "a limit or boundary", "We need to set the parameters."),
    ("mechanism", "noun", "a system of parts working together", "The mechanism of the machine is complex."),
    ("infrastructure", "noun", "basic systems and services", "The city needs better infrastructure."),
    ("innovation", "noun", "a new method or idea", "Innovation drives economic growth."),
    ("simulation", "noun", "an imitation of a situation or process", "They ran a computer simulation."),
    ("algorithm", "noun", "a process for solving problems", "The algorithm calculates the result."),
    ("interface", "noun", "a point where two systems meet", "The user interface is intuitive."),
    ("database", "noun", "a structured set of data", "The database stores customer information."),
    ("bandwidth", "noun", "the capacity for data transfer", "We need more bandwidth."),
    ("encryption", "noun", "converting data into a secure code", "Encryption protects sensitive data."),
    ("prototype", "noun", "an early sample or model", "They built a prototype of the car."),
    
    # Business & Economics
    ("revenue", "noun", "income generated from business", "The company increased its revenue."),
    ("expenditure", "noun", "the action of spending funds", "Government expenditure has risen."),
    ("deficit", "noun", "the amount by which spending exceeds income", "The country has a budget deficit."),
    ("surplus", "noun", "an excess of income over expenditure", "There was a trade surplus."),
    ("inflation", "noun", "a general increase in prices", "Inflation affects purchasing power."),
    ("recession", "noun", "a period of temporary economic decline", "The recession caused job losses."),
    ("commodity", "noun", "a raw material or primary product", "Oil is an important commodity."),
    ("monopoly", "noun", "exclusive control of a market", "The company has a monopoly."),
    ("subsidiary", "noun", "a company controlled by another", "The subsidiary operates independently."),
    ("dividend", "noun", "a payment made to shareholders", "They declared a quarterly dividend."),
    ("equity", "noun", "the value of shares in a company", "The equity market is volatile."),
    ("liability", "noun", "something a person is responsible for", "The company has significant liabilities."),
    ("collateral", "noun", "security pledged for repayment of a loan", "The house served as collateral."),
    ("depreciation", "noun", "reduction in value over time", "Calculate the depreciation of assets."),
    ("procurement", "noun", "the action of obtaining something", "The procurement process is complex."),
    
    # Environment & Nature
    ("ecosystem", "noun", "a biological community", "The ecosystem is fragile."),
    ("biodiversity", "noun", "variety of life in a habitat", "We must protect biodiversity."),
    ("sustainability", "noun", "the ability to be maintained", "Sustainability is crucial for the future."),
    ("conservation", "noun", "preservation of natural resources", "Conservation efforts are increasing."),
    ("deforestation", "noun", "the clearing of forests", "Deforestation is a major problem."),
    ("emission", "noun", "the production of gas or radiation", "We need to reduce emissions."),
    ("pollutant", "noun", "a substance that pollutes", "The pollutant contaminated the water."),
    ("contamination", "noun", "the action of making something impure", "Contamination of the soil occurred."),
    ("habitat", "noun", "the natural home of an organism", "The habitat is being destroyed."),
    ("species", "noun", "a group of living organisms", "Many species are endangered."),
    ("extinction", "noun", "the state of no longer existing", "Dinosaurs faced extinction."),
    ("organism", "noun", "an individual living thing", "The organism adapted to its environment."),
    ("photosynthesis", "noun", "process by which plants convert light", "Photosynthesis produces oxygen."),
    ("erosion", "noun", "the gradual destruction by natural forces", "Soil erosion is a serious issue."),
    ("precipitation", "noun", "rain, snow, or hail", "Precipitation levels vary seasonally."),
    
    # Health & Medicine
    ("diagnosis", "noun", "identification of an illness", "The diagnosis was accurate."),
    ("symptom", "noun", "a sign of disease", "Fever is a common symptom."),
    ("therapy", "noun", "treatment intended to relieve a disorder", "The therapy was effective."),
    ("vaccination", "noun", "treatment with a vaccine", "Vaccination prevents diseases."),
    ("immunity", "noun", "resistance to disease", "The body develops immunity."),
    ("chronic", "adjective", "persisting for a long time", "He has chronic back pain."),
    ("acute", "adjective", "severe or intense", "She experienced acute pain."),
    ("epidemic", "noun", "a widespread occurrence of disease", "The epidemic spread quickly."),
    ("pandemic", "noun", "a disease prevalent over a whole country or world", "The pandemic affected millions."),
    ("contagious", "adjective", "able to be transmitted", "The disease is highly contagious."),
    ("prescription", "noun", "a doctor's instruction for medicine", "She got a prescription from the doctor."),
    ("dosage", "noun", "the size of a dose of medicine", "Follow the recommended dosage."),
    ("surgical", "adjective", "relating to surgery", "The surgical procedure was successful."),
    ("rehabilitation", "noun", "restoration to health", "Physical rehabilitation takes time."),
    ("disorder", "noun", "an illness that disrupts function", "He was diagnosed with a sleep disorder."),
    
    # Society & Culture
    ("demographic", "noun", "a particular sector of population", "The demographic is changing."),
    ("migration", "noun", "movement from one region to another", "Migration patterns have shifted."),
    ("immigration", "noun", "coming to live in a foreign country", "Immigration policy is debated."),
    ("integration", "noun", "the act of combining into a whole", "Integration of cultures takes time."),
    ("discrimination", "noun", "unjust treatment based on category", "Discrimination is illegal."),
    ("inequality", "noun", "difference in status or opportunity", "Social inequality persists."),
    ("ideology", "noun", "a system of ideas and ideals", "The ideology influenced politics."),
    ("democracy", "noun", "government by the people", "Democracy requires participation."),
    ("bureaucracy", "noun", "a system of government administration", "The bureaucracy is complex."),
    ("legislation", "noun", "laws collectively", "New legislation was passed."),
    ("jurisdiction", "noun", "the official power to make legal decisions", "The court has jurisdiction."),
    ("amendment", "noun", "a change to a document or law", "The amendment was approved."),
    ("constitution", "noun", "fundamental principles of governance", "The constitution protects rights."),
    ("sovereignty", "noun", "supreme power or authority", "National sovereignty is important."),
    ("diplomacy", "noun", "the management of international relations", "Diplomacy resolved the conflict."),
    
    # Psychology & Behavior
    ("cognitive", "adjective", "relating to mental processes", "Cognitive abilities decline with age."),
    ("perception", "noun", "the way something is understood", "Perception varies among individuals."),
    ("motivation", "noun", "the reason for acting", "Motivation drives success."),
    ("stimulus", "noun", "something that causes a response", "The stimulus triggered a reaction."),
    ("response", "noun", "a reaction to something", "The response was immediate."),
    ("behavior", "noun", "the way one acts or conducts oneself", "Behavior can be learned."),
    ("consciousness", "noun", "the state of being aware", "Consciousness is complex."),
    ("subconscious", "noun", "the part of mind not fully aware", "The subconscious influences behavior."),
    ("emotion", "noun", "a strong feeling", "Emotions affect decision-making."),
    ("anxiety", "noun", "a feeling of worry or unease", "Anxiety is common before exams."),
    ("depression", "noun", "feelings of severe despondency", "Depression requires treatment."),
    ("trauma", "noun", "a deeply distressing experience", "The trauma left lasting effects."),
    ("phobia", "noun", "an extreme or irrational fear", "She has a phobia of heights."),
    ("instinct", "noun", "an innate pattern of behavior", "Survival instinct is strong."),
    ("personality", "noun", "the combination of characteristics", "Personality affects relationships."),
    
    # Communication & Language
    ("discourse", "noun", "written or spoken communication", "Academic discourse is formal."),
    ("rhetoric", "noun", "the art of persuasive speaking", "Political rhetoric can be powerful."),
    ("narrative", "noun", "a spoken or written account", "The narrative was compelling."),
    ("metaphor", "noun", "a figure of speech", "Life is a journey is a metaphor."),
    ("context", "noun", "the circumstances around an event", "Context is important for understanding."),
    ("interpretation", "noun", "the action of explaining meaning", "Interpretation varies by reader."),
    ("implication", "noun", "a conclusion drawn indirectly", "The implication was clear."),
    ("connotation", "noun", "an idea suggested by a word", "The word has negative connotations."),
    ("ambiguity", "noun", "uncertainty of meaning", "The ambiguity caused confusion."),
    ("articulate", "verb", "express thoughts clearly", "She can articulate her ideas well."),
    ("coherent", "adjective", "logical and consistent", "The argument was coherent."),
    ("eloquent", "adjective", "fluent and persuasive", "He gave an eloquent speech."),
    ("linguistic", "adjective", "relating to language", "Linguistic skills are valuable."),
    ("bilingual", "adjective", "speaking two languages fluently", "She is bilingual in English and Spanish."),
    ("terminology", "noun", "terms used in a subject", "Medical terminology is complex."),
    
    # Research & Analysis
    ("analyze", "verb", "examine in detail", "We need to analyze the data."),
    ("evaluate", "verb", "assess the value of something", "Evaluate the results carefully."),
    ("synthesize", "verb", "combine into a coherent whole", "Synthesize information from sources."),
    ("conclude", "verb", "bring to an end or reach a judgment", "We can conclude that the theory is valid."),
    ("verify", "verb", "make sure something is true", "Verify the information before publishing."),
    ("validate", "verb", "check or prove the validity of", "The study validated the hypothesis."),
    ("quantify", "verb", "express as a quantity", "It is difficult to quantify happiness."),
    ("qualitative", "adjective", "relating to quality not quantity", "The study used qualitative methods."),
    ("quantitative", "adjective", "relating to quantity", "Quantitative data supports the claim."),
    ("empirical", "adjective", "based on observation", "Empirical evidence is essential."),
    ("theoretical", "adjective", "based on theory rather than practice", "The model is theoretical."),
    ("objective", "adjective", "not influenced by personal feelings", "Remain objective in your analysis."),
    ("subjective", "adjective", "based on personal opinions", "Art appreciation is subjective."),
    ("criterion", "noun", "a standard for judging", "What is the selection criterion?"),
    ("criteria", "noun", "standards for judging (plural)", "The criteria are strict."),
    
    # Abstract Concepts
    ("concept", "noun", "an abstract idea", "The concept is difficult to grasp."),
    ("theory", "noun", "a system of ideas explaining something", "Einstein's theory changed physics."),
    ("principle", "noun", "a fundamental truth or proposition", "The principle guides our decisions."),
    ("framework", "noun", "a basic structure underlying a system", "We need a theoretical framework."),
    ("paradigm", "noun", "a typical example or pattern", "The paradigm shift transformed science."),
    ("perspective", "noun", "a particular way of viewing things", "Consider different perspectives."),
    ("dimension", "noun", "an aspect or feature", "The problem has many dimensions."),
    ("aspect", "noun", "a particular part or feature", "Consider every aspect of the issue."),
    ("factor", "noun", "a circumstance contributing to a result", "Many factors influence success."),
    ("element", "noun", "a component or part", "The key element is timing."),
    ("component", "noun", "a part of a larger whole", "Each component is essential."),
    ("attribute", "noun", "a quality or feature", "Patience is a valuable attribute."),
    ("characteristic", "noun", "a distinguishing feature", "Honesty is his main characteristic."),
    ("phenomenon", "noun", "a fact that is observed to exist", "The phenomenon is unexplained."),
    ("entity", "noun", "a thing with distinct existence", "The company is a legal entity."),
    
    # Action & Process
    ("implement", "verb", "put into effect", "We will implement the plan tomorrow."),
    ("facilitate", "verb", "make easier", "Technology facilitates communication."),
    ("enhance", "verb", "intensify or improve", "Exercise enhances well-being."),
    ("modify", "verb", "make partial changes to", "We need to modify the design."),
    ("adapt", "verb", "make suitable for a new purpose", "Species adapt to their environment."),
    ("transform", "verb", "change in form or character", "Technology has transformed society."),
    ("convert", "verb", "change from one form to another", "Convert the file to PDF format."),
    ("generate", "verb", "produce or create", "The project will generate jobs."),
    ("establish", "verb", "set up on a permanent basis", "They established a new company."),
    ("maintain", "verb", "cause to continue", "Maintain a healthy lifestyle."),
    ("sustain", "verb", "strengthen or support", "Sustain the economic growth."),
    ("eliminate", "verb", "completely remove", "Eliminate unnecessary expenses."),
    ("diminish", "verb", "make or become less", "The pain will diminish over time."),
    ("minimize", "verb", "reduce to the smallest amount", "Minimize the risk of error."),
    ("maximize", "verb", "make as large as possible", "Maximize your potential."),
    
    # Describing Change
    ("significant", "adjective", "sufficiently great or important", "There was a significant improvement."),
    ("substantial", "adjective", "of considerable importance or size", "Substantial changes were made."),
    ("marginal", "adjective", "minor and not important", "The difference is marginal."),
    ("gradual", "adjective", "taking place by degrees", "The change was gradual."),
    ("dramatic", "adjective", "sudden and striking", "There was a dramatic increase."),
    ("steady", "adjective", "regular and continuous", "The economy showed steady growth."),
    ("constant", "adjective", "occurring continuously", "There is constant demand."),
    ("fluctuating", "adjective", "rising and falling irregularly", "Prices are fluctuating."),
    ("stable", "adjective", "not likely to change", "The situation is stable."),
    ("volatile", "adjective", "liable to change rapidly", "The market is volatile."),
    ("consistent", "adjective", "unchanging in achievement", "Results have been consistent."),
    ("prevalent", "adjective", "widespread in a particular area", "The disease is prevalent in Africa."),
    ("dominant", "adjective", "most important or powerful", "The dominant view prevailed."),
    ("prominent", "adjective", "important; famous", "She is a prominent scientist."),
    ("emerging", "adjective", "becoming apparent or prominent", "Emerging markets show potential."),
    
    # Relationships & Connections
    ("relevant", "adjective", "closely connected to the matter", "The information is relevant."),
    ("pertinent", "adjective", "relevant or applicable", "The pertinent facts were presented."),
    ("corresponding", "adjective", "analogous or equivalent", "The corresponding chapter explains more."),
    ("inherent", "adjective", "existing as a natural part", "Risk is inherent in investment."),
    ("intrinsic", "adjective", "belonging naturally; essential", "The intrinsic value is high."),
    ("implicit", "adjective", "implied though not directly expressed", "The criticism was implicit."),
    ("explicit", "adjective", "stated clearly and in detail", "The instructions were explicit."),
    ("subsequent", "adjective", "coming after something in time", "Subsequent events proved him right."),
    ("preliminary", "adjective", "done in preparation", "Preliminary results are positive."),
    ("fundamental", "adjective", "forming a necessary base", "This is a fundamental concept."),
    ("underlying", "adjective", "being the basis of", "The underlying cause is unclear."),
    ("comprehensive", "adjective", "complete; including all elements", "A comprehensive report was prepared."),
    ("extensive", "adjective", "covering a large area", "Extensive research was conducted."),
    ("intensive", "adjective", "concentrated; thorough", "Intensive training is required."),
    ("exclusive", "adjective", "restricted to a particular group", "The club has exclusive membership."),
    
    # More IELTS Essential Words
    ("advocate", "verb", "publicly support or recommend", "She advocates for human rights."),
    ("allocate", "verb", "distribute for a particular purpose", "Allocate resources efficiently."),
    ("anticipate", "verb", "regard as probable", "We anticipate high demand."),
    ("approximate", "adjective", "close to the actual", "The approximate cost is $500."),
    ("arbitrary", "adjective", "based on random choice", "The decision seemed arbitrary."),
    ("assert", "verb", "state a fact confidently", "He asserted his innocence."),
    ("assume", "verb", "suppose to be the case", "I assume you have read the report."),
    ("attain", "verb", "succeed in achieving", "She attained her goal."),
    ("authority", "noun", "the power to give orders", "The authority approved the plan."),
    ("benefit", "noun", "an advantage or profit gained", "Exercise has many benefits."),
    ("capacity", "noun", "the maximum amount that can be contained", "The stadium has a capacity of 50,000."),
    ("category", "noun", "a class or division", "The product falls into this category."),
    ("cease", "verb", "come or bring to an end", "Fighting will cease at midnight."),
    ("challenge", "noun", "a difficult task", "The project presents a challenge."),
    ("circumstance", "noun", "a fact related to an event", "Circumstances forced the decision."),
]

# =====================================================================
# IELTS BAND 7.0-7.5 단어 대량 추가
# =====================================================================
BAND70_MASSIVE = [
    # Advanced Academic Vocabulary
    ("paradigmatic", "adjective", "serving as a typical example", "This is a paradigmatic case of corruption."),
    ("epistemological", "adjective", "relating to the theory of knowledge", "The epistemological question remains unanswered."),
    ("ontological", "adjective", "relating to the nature of being", "An ontological argument for existence."),
    ("axiom", "noun", "a statement accepted as true", "This is a fundamental axiom."),
    ("postulate", "noun", "a thing suggested as true", "The postulate requires proof."),
    ("dichotomy", "noun", "a division into two contrasting things", "The dichotomy between rich and poor."),
    ("juxtaposition", "noun", "the fact of being placed side by side", "The juxtaposition of old and new."),
    ("paradox", "noun", "a seemingly contradictory statement", "The paradox puzzled philosophers."),
    ("anomaly", "noun", "something that deviates from what is standard", "The data anomaly was investigated."),
    ("ambivalence", "noun", "having mixed feelings", "She felt ambivalence about the offer."),
    ("nuance", "noun", "a subtle difference in meaning", "The nuance was lost in translation."),
    ("subtlety", "noun", "the quality of being delicate", "Appreciate the subtlety of the argument."),
    ("intricacy", "noun", "the quality of being complex", "The intricacy of the design is impressive."),
    ("abstraction", "noun", "the quality of dealing with ideas", "Art often relies on abstraction."),
    ("contingency", "noun", "a future event that may occur", "Plan for every contingency."),
    
    # Sophisticated Verbs
    ("ameliorate", "verb", "make something bad better", "Measures to ameliorate the situation."),
    ("exacerbate", "verb", "make a problem worse", "The crisis exacerbated tensions."),
    ("mitigate", "verb", "make less severe", "Steps to mitigate the damage."),
    ("alleviate", "verb", "make suffering less severe", "Medicine to alleviate pain."),
    ("precipitate", "verb", "cause to happen suddenly", "The scandal precipitated his resignation."),
    ("perpetuate", "verb", "make something continue indefinitely", "The system perpetuates inequality."),
    ("proliferate", "verb", "increase rapidly in number", "Weapons continue to proliferate."),
    ("disseminate", "verb", "spread information widely", "Disseminate the research findings."),
    ("consolidate", "verb", "make stronger or more solid", "Consolidate your position."),
    ("corroborate", "verb", "confirm or support with evidence", "Evidence corroborates the testimony."),
    ("substantiate", "verb", "provide evidence to support", "Substantiate your claims with data."),
    ("postulate", "verb", "suggest or assume as a fact", "Scientists postulate that..."),
    ("hypothesize", "verb", "put forward as a hypothesis", "Researchers hypothesized that..."),
    ("extrapolate", "verb", "extend known data into unknown area", "We can extrapolate from the data."),
    ("interpolate", "verb", "insert between fixed points", "Interpolate the missing values."),
    
    # Complex Adjectives
    ("pervasive", "adjective", "spreading widely throughout", "The pervasive influence of media."),
    ("ubiquitous", "adjective", "present everywhere", "Smartphones are ubiquitous today."),
    ("incessant", "adjective", "continuing without pause", "The incessant noise was disturbing."),
    ("intermittent", "adjective", "occurring at irregular intervals", "Intermittent rain throughout the day."),
    ("sporadic", "adjective", "occurring at irregular intervals", "Sporadic violence in the region."),
    ("endemic", "adjective", "native to a certain area", "Corruption is endemic in the system."),
    ("ephemeral", "adjective", "lasting for a very short time", "Fame can be ephemeral."),
    ("transient", "adjective", "lasting only for a short time", "The effects are transient."),
    ("immutable", "adjective", "unchanging over time", "The laws of physics are immutable."),
    ("malleable", "adjective", "easily influenced", "Gold is a malleable metal."),
    ("tangible", "adjective", "perceptible by touch", "Tangible results were achieved."),
    ("intangible", "adjective", "unable to be touched", "Intangible assets like goodwill."),
    ("congruent", "adjective", "in agreement or harmony", "The results are congruent."),
    ("incongruous", "adjective", "not in harmony", "The incongruous behavior puzzled everyone."),
    ("commensurate", "adjective", "corresponding in size or degree", "Salary commensurate with experience."),
    
    # Advanced Nouns
    ("ramification", "noun", "a complex consequence of an action", "Consider the ramifications carefully."),
    ("repercussion", "noun", "an unintended consequence", "The repercussions were severe."),
    ("implication", "noun", "a likely consequence", "The implications are far-reaching."),
    ("connotation", "noun", "an idea suggested by a word", "The word has negative connotations."),
    ("denotation", "noun", "the literal meaning of a word", "Consider both denotation and connotation."),
    ("inference", "noun", "a conclusion reached from evidence", "Draw inferences from the data."),
    ("conjecture", "noun", "an opinion based on incomplete information", "The theory is mere conjecture."),
    ("speculation", "noun", "forming a theory without evidence", "Speculation drove up prices."),
    ("assertion", "noun", "a confident statement of fact", "The assertion lacks evidence."),
    ("contention", "noun", "a heated disagreement", "The point of contention remained."),
    ("disparity", "noun", "a great difference", "The disparity in wealth is growing."),
    ("discrepancy", "noun", "a lack of compatibility", "There is a discrepancy in the accounts."),
    ("manifestation", "noun", "a display or demonstration", "The manifestation of symptoms."),
    ("propagation", "noun", "the spreading of something", "The propagation of ideas."),
    ("proliferation", "noun", "rapid increase in numbers", "The proliferation of nuclear weapons."),
    
    # More Band 7 Words
    ("circumvent", "verb", "find a way around an obstacle", "They circumvented the regulations."),
    ("circumscribe", "verb", "restrict or limit", "His powers are circumscribed by law."),
    ("encapsulate", "verb", "express the essential features", "The summary encapsulates the main points."),
    ("exemplify", "verb", "be a typical example of", "This case exemplifies the problem."),
    ("underscore", "verb", "emphasize", "The report underscores the need for change."),
    ("illuminate", "verb", "help to clarify or explain", "The study illuminates the issue."),
    ("elucidate", "verb", "make something clear", "Please elucidate your position."),
    ("delineate", "verb", "describe or portray precisely", "Delineate the boundaries clearly."),
    ("differentiate", "verb", "recognize or identify as different", "Differentiate between facts and opinions."),
    ("discriminate", "verb", "recognize a distinction", "Discriminate between right and wrong."),
    ("predicate", "verb", "found or base on", "The theory is predicated on assumptions."),
    ("presuppose", "verb", "require as a precondition", "The argument presupposes certain facts."),
    ("transcend", "verb", "be or go beyond the limits of", "Art can transcend cultural boundaries."),
    ("supersede", "verb", "take the place of", "New regulations supersede the old ones."),
    ("supplant", "verb", "take the place of", "Technology has supplanted traditional methods."),
    
    # Academic Writing Terms
    ("notwithstanding", "preposition", "in spite of", "Notwithstanding the difficulties, we succeeded."),
    ("albeit", "conjunction", "although", "The project succeeded, albeit with delays."),
    ("hitherto", "adverb", "until now", "Hitherto unknown facts emerged."),
    ("henceforth", "adverb", "from this time on", "Henceforth, new rules apply."),
    ("whereby", "adverb", "by which", "A system whereby all benefit."),
    ("wherein", "adverb", "in which", "The situation wherein we find ourselves."),
    ("thereof", "adverb", "of the thing just mentioned", "The terms and conditions thereof."),
    ("therein", "adverb", "in that place or document", "The answer lies therein."),
    ("insofar", "adverb", "to the extent that", "Insofar as it concerns us."),
    ("inasmuch", "adverb", "since; to such a degree", "Inasmuch as it is possible."),
    ("nonetheless", "adverb", "in spite of that", "The task was difficult; nonetheless, they succeeded."),
    ("furthermore", "adverb", "in addition; moreover", "Furthermore, the evidence supports this."),
    ("consequently", "adverb", "as a result", "Consequently, changes were made."),
    ("subsequently", "adverb", "after a particular thing has happened", "He subsequently apologized."),
    ("conversely", "adverb", "in an opposite way", "Conversely, the other group showed no change."),
    
    # Scientific Terms
    ("empiricism", "noun", "theory based on observation", "Empiricism is fundamental to science."),
    ("rationalism", "noun", "theory based on reason", "Rationalism emphasizes logical thinking."),
    ("determinism", "noun", "the doctrine that events are predetermined", "Determinism challenges free will."),
    ("reductionism", "noun", "analyzing complex things as simpler elements", "Reductionism has its limits."),
    ("holism", "noun", "treating the whole as more than parts", "Holism provides a broader view."),
    ("pragmatism", "noun", "dealing with things sensibly and realistically", "Pragmatism guides decision-making."),
    ("utilitarianism", "noun", "maximizing overall well-being", "Utilitarianism considers the greatest good."),
    ("egalitarianism", "noun", "belief in equality for all", "Egalitarianism promotes fairness."),
    ("pluralism", "noun", "coexistence of diverse elements", "Cultural pluralism enriches society."),
    ("relativism", "noun", "knowledge is relative to culture", "Moral relativism raises ethical questions."),
    ("skepticism", "noun", "an attitude of doubt", "Healthy skepticism is valuable."),
    ("cynicism", "noun", "belief that people are motivated by self-interest", "Cynicism can be counterproductive."),
    ("altruism", "noun", "selfless concern for others", "Altruism benefits society."),
    ("egoism", "noun", "ethical theory based on self-interest", "Egoism contrasts with altruism."),
    ("hedonism", "noun", "pursuit of pleasure", "Hedonism has philosophical roots."),
    
    # Complex Expressions
    ("predisposition", "noun", "a liability or tendency", "A genetic predisposition to disease."),
    ("predetermination", "noun", "the action of determining beforehand", "Predetermination of outcomes."),
    ("preconception", "noun", "a preconceived idea", "Challenge your preconceptions."),
    ("presupposition", "noun", "a thing assumed beforehand", "The presupposition is flawed."),
    ("misconception", "noun", "a wrong or inaccurate idea", "A common misconception about science."),
    ("juxtapose", "verb", "place side by side for contrast", "Juxtapose the old with the new."),
    ("superimpose", "verb", "place something on top of another", "Superimpose the images."),
    ("interpose", "verb", "place between", "Interpose a buffer between them."),
    ("transpose", "verb", "cause to exchange places", "Transpose the rows and columns."),
    ("predispose", "verb", "make susceptible", "Genetics predispose individuals to conditions."),
]

# =====================================================================
# IELTS BAND 8.0+ 단어 대량 추가
# =====================================================================
BAND80_MASSIVE = [
    # Extremely Sophisticated Vocabulary
    ("obfuscate", "verb", "make unclear or unintelligible", "The report obfuscates the real issues."),
    ("obviate", "verb", "remove a need or difficulty", "This solution obviates the problem."),
    ("ostracize", "verb", "exclude from a society or group", "He was ostracized by his peers."),
    ("ossify", "verb", "cease developing; become rigid", "The institution has ossified over time."),
    ("promulgate", "verb", "promote or make widely known", "Promulgate the new regulations."),
    ("propitiate", "verb", "win or regain the favor of", "Attempts to propitiate the critics."),
    ("proscribe", "verb", "forbid by law", "The practice was proscribed."),
    ("prescribe", "verb", "recommend with authority", "The doctor prescribed medicine."),
    ("prevaricate", "verb", "speak evasively", "Politicians often prevaricate."),
    ("procrastinate", "verb", "delay or postpone action", "Don't procrastinate on important tasks."),
    ("prognosticate", "verb", "foretell or prophesy", "Experts prognosticate economic trends."),
    ("recapitulate", "verb", "summarize and state again", "Let me recapitulate the main points."),
    ("reconstitute", "verb", "reconstruct or reorganize", "Reconstitute the committee."),
    ("remonstrate", "verb", "make a forcefully reproachful protest", "She remonstrated against the decision."),
    ("repudiate", "verb", "refuse to accept or support", "He repudiated the allegations."),
    
    # Rare but Powerful Words
    ("perspicacious", "adjective", "having keen mental perception", "A perspicacious observation."),
    ("prescient", "adjective", "having knowledge of events before they happen", "A prescient prediction."),
    ("punctilious", "adjective", "showing great attention to detail", "A punctilious administrator."),
    ("querulous", "adjective", "complaining in a petulant way", "The querulous patient complained constantly."),
    ("quixotic", "adjective", "extremely idealistic; unrealistic", "A quixotic attempt to reform society."),
    ("recondite", "adjective", "little known; abstruse", "Recondite philosophical arguments."),
    ("recalcitrant", "adjective", "having an obstinately uncooperative attitude", "A recalcitrant student."),
    ("refractory", "adjective", "stubborn or unmanageable", "The refractory child refused to listen."),
    ("sanguine", "adjective", "optimistic in a difficult situation", "She remained sanguine about the outcome."),
    ("sycophantic", "adjective", "behaving obsequiously to gain advantage", "Sycophantic praise for the boss."),
    ("taciturn", "adjective", "reserved or uncommunicative", "A taciturn man of few words."),
    ("tendentious", "adjective", "expressing a strong opinion", "A tendentious interpretation of events."),
    ("truculent", "adjective", "eager or quick to argue", "His truculent manner alienated colleagues."),
    ("turgid", "adjective", "pompous or bombastic", "Turgid academic prose."),
    ("unctuous", "adjective", "excessively flattering", "An unctuous salesman."),
    
    # Academic Rarities
    ("anachronism", "noun", "something belonging to a former time", "The practice is an anachronism."),
    ("antithesis", "noun", "the exact opposite", "War is the antithesis of peace."),
    ("apotheosis", "noun", "the highest point of development", "The apotheosis of his career."),
    ("archetype", "noun", "a very typical example", "The archetype of the tragic hero."),
    ("chicanery", "noun", "the use of trickery to achieve a goal", "Political chicanery is common."),
    ("circumlocution", "noun", "the use of many words to avoid direct statement", "The circumlocution obscured the meaning."),
    ("conflation", "noun", "the merging of two distinct things", "The conflation of two separate issues."),
    ("conflagration", "noun", "an extensive fire; conflict", "The conflagration destroyed the building."),
    ("denouement", "noun", "the final outcome of a situation", "The denouement was unexpected."),
    ("diatribe", "noun", "a forceful and bitter verbal attack", "A diatribe against corruption."),
    ("didacticism", "noun", "intended to teach or instruct", "The novel's didacticism is obvious."),
    ("dissimulation", "noun", "concealment of one's true feelings", "His dissimulation fooled everyone."),
    ("equivocation", "noun", "the use of ambiguous language", "His equivocation raised suspicions."),
    ("exegesis", "noun", "critical explanation of a text", "Biblical exegesis requires scholarship."),
    ("harangue", "noun", "a lengthy and aggressive speech", "He delivered a harangue against injustice."),
    
    # Philosophical & Literary Terms
    ("hermeneutics", "noun", "the branch of knowledge dealing with interpretation", "Hermeneutics of ancient texts."),
    ("heuristic", "adjective", "enabling a person to discover for themselves", "A heuristic approach to learning."),
    ("hubris", "noun", "excessive pride or self-confidence", "His hubris led to his downfall."),
    ("iconoclast", "noun", "a person who attacks cherished beliefs", "An iconoclast who challenged tradition."),
    ("idiosyncrasy", "noun", "a distinctive individual characteristic", "His idiosyncrasies were endearing."),
    ("ignominy", "noun", "public shame or disgrace", "He resigned in ignominy."),
    ("imprimatur", "noun", "an official approval or sanction", "The project received official imprimatur."),
    ("inchoate", "adjective", "just begun and so incomplete", "An inchoate plan that needs development."),
    ("ineffable", "adjective", "too great to be expressed in words", "An ineffable sense of wonder."),
    ("inexorable", "adjective", "impossible to stop or prevent", "The inexorable march of time."),
    ("inimical", "adjective", "tending to obstruct or harm", "Conditions inimical to success."),
    ("insidious", "adjective", "proceeding in a harmful way", "The insidious effects of propaganda."),
    ("intransigent", "adjective", "unwilling to compromise", "An intransigent negotiating position."),
    ("invective", "noun", "insulting or abusive language", "Political invective reached new heights."),
    ("jejune", "adjective", "naive, simplistic, and superficial", "A jejune remark that showed his inexperience."),
    
    # More Band 8+ Words
    ("laconic", "adjective", "using very few words", "A laconic reply that conveyed everything."),
    ("legerdemain", "noun", "skillful deception", "Political legerdemain confused the voters."),
    ("magnanimous", "adjective", "generous or forgiving", "A magnanimous gesture by the winner."),
    ("malfeasance", "noun", "wrongdoing by a public official", "Corporate malfeasance was exposed."),
    ("mendacious", "adjective", "not telling the truth", "A mendacious account of events."),
    ("mercurial", "adjective", "subject to sudden changes of mood", "Her mercurial temperament made planning difficult."),
    ("nascent", "adjective", "just beginning to develop", "A nascent democracy still finding its way."),
    ("nebulous", "adjective", "unclear or vague", "A nebulous concept that needs definition."),
    ("nefarious", "adjective", "wicked or criminal", "Nefarious activities were uncovered."),
    ("obsequious", "adjective", "excessively compliant or deferential", "Obsequious behavior toward superiors."),
    ("opaque", "adjective", "not able to be seen through; unclear", "The language was opaque to outsiders."),
    ("opprobrium", "noun", "harsh criticism or censure", "He faced public opprobrium."),
    ("ostensible", "adjective", "stated or appearing to be true", "The ostensible reason for his visit."),
    ("palliative", "adjective", "relieving pain without curing", "Palliative care for terminal patients."),
    ("paradigmatic", "adjective", "serving as a typical example", "A paradigmatic case of mismanagement."),
    
    # Extremely Rare Academic Words
    ("penultimate", "adjective", "last but one in a series", "The penultimate chapter of the book."),
    ("peripatetic", "adjective", "traveling from place to place", "A peripatetic lifestyle."),
    ("perfidious", "adjective", "deceitful and untrustworthy", "A perfidious ally who betrayed us."),
    ("perfunctory", "adjective", "carried out with minimum effort", "A perfunctory inspection."),
    ("pernicious", "adjective", "having a harmful effect", "The pernicious influence of prejudice."),
    ("perspicuous", "adjective", "clearly expressed and easily understood", "A perspicuous explanation."),
    ("pertinacious", "adjective", "holding firmly to an opinion", "A pertinacious advocate for change."),
    ("platitudinous", "adjective", "dull or unoriginal", "Platitudinous remarks that bored everyone."),
    ("plethora", "noun", "an excess or overabundance", "A plethora of options."),
    ("polemic", "noun", "a strong verbal or written attack", "A political polemic."),
    ("portentous", "adjective", "giving a sign of future events", "A portentous warning."),
    ("precarious", "adjective", "not securely held or in position", "A precarious financial situation."),
    ("proclivity", "noun", "a tendency to choose or do something", "A proclivity for exaggeration."),
    ("prodigious", "adjective", "remarkably great in extent", "A prodigious achievement."),
    ("propensity", "noun", "an inclination or tendency", "A propensity for risk-taking."),
    
    # Final Set of Band 8+ Words
    ("prosaic", "adjective", "lacking imagination; dull", "A prosaic account of events."),
    ("puerile", "adjective", "childishly silly and immature", "Puerile behavior is unacceptable."),
    ("pugnacious", "adjective", "eager or quick to quarrel", "A pugnacious attitude."),
    ("punctiliously", "adverb", "with great attention to detail", "He punctiliously followed the rules."),
    ("quotidian", "adjective", "occurring every day; ordinary", "The quotidian concerns of daily life."),
    ("rapacious", "adjective", "aggressively greedy", "A rapacious corporation."),
    ("redolent", "adjective", "strongly reminiscent of", "A style redolent of the 19th century."),
    ("reticent", "adjective", "not revealing one's thoughts readily", "She was reticent about her plans."),
    ("sagacious", "adjective", "having keen mental discernment", "A sagacious leader."),
    ("salient", "adjective", "most noticeable or important", "The salient points of the argument."),
    ("scrupulous", "adjective", "diligent, thorough, and attentive", "Scrupulous attention to detail."),
    ("sedulous", "adjective", "showing dedication and diligence", "A sedulous researcher."),
    ("specious", "adjective", "superficially plausible but wrong", "A specious argument."),
    ("spurious", "adjective", "not genuine or authentic", "Spurious claims were dismissed."),
    ("surreptitious", "adjective", "kept secret because improper", "A surreptitious glance."),
]

# =====================================================================
# BAND 4.5-5.5 추가 단어 (목표 근접, 약간만 추가)
# =====================================================================
BAND45_MORE = [
    ("adventure", "noun", "an exciting experience", "They had an adventure in the mountains."),
    ("afraid", "adjective", "feeling fear or anxiety", "The child was afraid of the dark."),
    ("afternoon", "noun", "the time from noon to evening", "We'll meet this afternoon."),
    ("airport", "noun", "a place where planes land and take off", "The airport was crowded."),
    ("amazing", "adjective", "causing great surprise or wonder", "The view was amazing."),
    ("ancient", "adjective", "belonging to the very distant past", "Ancient civilizations built pyramids."),
    ("angry", "adjective", "feeling strong displeasure", "She was angry about the delay."),
    ("apartment", "noun", "a flat in a building", "They live in a small apartment."),
    ("appearance", "noun", "the way something looks", "His appearance changed dramatically."),
    ("appointment", "noun", "an arrangement to meet", "I have a doctor's appointment."),
    ("arrive", "verb", "reach a destination", "We arrive at noon."),
    ("artist", "noun", "a person who creates art", "The artist painted beautiful pictures."),
    ("attention", "noun", "notice taken of something", "Pay attention to the teacher."),
    ("attractive", "adjective", "pleasing in appearance", "The garden is very attractive."),
    ("average", "adjective", "typical; ordinary", "The average student studies hard."),
    ("balance", "noun", "a state of equilibrium", "Keep your balance while walking."),
    ("baseball", "noun", "a bat-and-ball game", "He plays baseball every weekend."),
    ("basketball", "noun", "a game with a ball and hoop", "Basketball is popular worldwide."),
    ("bathroom", "noun", "a room with a bath or shower", "The bathroom needs cleaning."),
    ("beach", "noun", "sandy shore by the sea", "We spent the day at the beach."),
    ("bedroom", "noun", "a room for sleeping", "Her bedroom has a large window."),
    ("beginning", "noun", "the start of something", "This is just the beginning."),
    ("believe", "verb", "accept as true", "I believe you are right."),
    ("bicycle", "noun", "a two-wheeled vehicle", "She rides her bicycle to work."),
    ("birthday", "noun", "the anniversary of one's birth", "Happy birthday to you!"),
    ("blanket", "noun", "a covering for warmth", "The baby needs a warm blanket."),
    ("borrow", "verb", "take and use temporarily", "Can I borrow your pen?"),
    ("bottle", "noun", "a container for liquids", "The bottle is full of water."),
    ("bottom", "noun", "the lowest part", "The answer is at the bottom."),
    ("brave", "adjective", "showing courage", "The brave firefighter saved lives."),
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
    
    # 기존 데이터 로드
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
    
    # 저장
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ {filename}: {len(existing_data)}개 (추가: {added}개)")
    return len(existing_data)

# 각 밴드에 단어 추가
print("\n" + "="*50)
print("📚 IELTS 단어 대량 추가 시작")
print("="*50 + "\n")

total_band45 = add_words_to_file('band45_words.json', BAND45_MORE, 'Band 4.5-5.5')
total_band60 = add_words_to_file('band60_words.json', BAND60_MASSIVE, 'Band 6.0-6.5')
total_band70 = add_words_to_file('band70_words.json', BAND70_MASSIVE, 'Band 7.0-7.5')
total_band80 = add_words_to_file('band80_words.json', BAND80_MASSIVE, 'Band 8.0+')

print("\n" + "="*50)
print(f"📊 총 단어 현황:")
print(f"   Band 4.5-5.5: {total_band45}개")
print(f"   Band 6.0-6.5: {total_band60}개")
print(f"   Band 7.0-7.5: {total_band70}개")
print(f"   Band 8.0+: {total_band80}개")
print(f"   총계: {total_band45 + total_band60 + total_band70 + total_band80}개")
print("="*50)
