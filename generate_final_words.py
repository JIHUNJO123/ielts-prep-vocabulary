#!/usr/bin/env python3
"""
IELTS 단어 최종 생성 스크립트 - 5000개 목표 달성
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
# BAND 6.0-6.5 최종 추가 (목표 1800개까지)
# =====================================================================
BAND60_FINAL = [
    # Academic Word List (AWL) - Sublist 1-10 핵심 단어
    ("analyze", "verb", "examine methodically", "Analyze the results carefully."),
    ("approach", "verb", "come near or nearer", "Approach the problem systematically."),
    ("area", "noun", "a region or part", "The research area is broad."),
    ("assess", "verb", "evaluate or estimate", "Assess the situation first."),
    ("assume", "verb", "suppose to be true", "Don't assume anything."),
    ("authority", "noun", "the power to give orders", "The authority granted permission."),
    ("available", "adjective", "able to be used", "Resources are available."),
    ("benefit", "noun", "an advantage or profit", "The benefits outweigh costs."),
    ("concept", "noun", "an abstract idea", "A complex concept to grasp."),
    ("consistent", "adjective", "unchanging in achievement", "Results were consistent."),
    ("constitutional", "adjective", "relating to a constitution", "Constitutional rights matter."),
    ("context", "noun", "the circumstances around an event", "Consider the context."),
    ("contract", "noun", "a written agreement", "Sign the contract today."),
    ("create", "verb", "bring into existence", "Create new opportunities."),
    ("data", "noun", "facts and statistics", "Collect and analyze data."),
    ("define", "verb", "state the meaning of", "Define the key terms."),
    ("derive", "verb", "obtain from a source", "Derive conclusions from evidence."),
    ("distribute", "verb", "give shares of something", "Distribute resources fairly."),
    ("economy", "noun", "the wealth of a country", "The economy is growing."),
    ("environment", "noun", "the surroundings", "Protect the environment."),
    ("establish", "verb", "set up on a permanent basis", "Establish clear guidelines."),
    ("estimate", "verb", "roughly calculate", "Estimate the total cost."),
    ("evident", "adjective", "clearly seen or understood", "The problem was evident."),
    ("export", "verb", "send goods to another country", "Export goods worldwide."),
    ("factor", "noun", "a circumstance contributing to a result", "Consider all factors."),
    ("finance", "noun", "the management of money", "Study finance and economics."),
    ("formula", "noun", "a mathematical relationship", "Apply the formula correctly."),
    ("function", "noun", "an activity appropriate to a person", "The function of the device."),
    ("identify", "verb", "establish the identity of", "Identify the main issues."),
    ("income", "noun", "money received for work", "A stable income is important."),
    ("indicate", "verb", "point out; show", "Results indicate success."),
    ("individual", "noun", "a single human being", "Each individual matters."),
    ("interpret", "verb", "explain the meaning of", "Interpret the data carefully."),
    ("involve", "verb", "have as a necessary part", "The project involves teamwork."),
    ("issue", "noun", "an important topic for debate", "Address the key issues."),
    ("labour", "noun", "work or workers collectively", "Labour costs are rising."),
    ("legal", "adjective", "relating to the law", "Legal requirements must be met."),
    ("legislate", "verb", "make or enact laws", "Legislate for change."),
    ("major", "adjective", "important or serious", "A major development occurred."),
    ("method", "noun", "a particular way of doing something", "Use the correct method."),
    ("occur", "verb", "happen; take place", "Events occur naturally."),
    ("percent", "noun", "one part in every hundred", "Ten percent increase."),
    ("period", "noun", "a length of time", "A historical period."),
    ("policy", "noun", "a course of action", "Government policy changed."),
    ("principle", "noun", "a fundamental truth", "Basic principles apply."),
    ("proceed", "verb", "begin a course of action", "Proceed with caution."),
    ("process", "noun", "a series of actions", "The manufacturing process."),
    ("require", "verb", "need for a purpose", "Require additional resources."),
    ("research", "noun", "systematic investigation", "Conduct thorough research."),
    ("respond", "verb", "say something in reply", "Respond to the question."),
    
    # More AWL Essential Words
    ("role", "noun", "the function assumed by a person", "Play an important role."),
    ("section", "noun", "a distinct part", "Read the first section."),
    ("sector", "noun", "an area of activity", "The private sector."),
    ("significant", "adjective", "sufficiently great", "A significant improvement."),
    ("similar", "adjective", "resembling another", "Similar results obtained."),
    ("source", "noun", "a place from which something comes", "Cite your sources."),
    ("specific", "adjective", "clearly defined", "Specific requirements exist."),
    ("structure", "noun", "the arrangement of parts", "The organizational structure."),
    ("theory", "noun", "a system of ideas", "Test the theory carefully."),
    ("vary", "verb", "differ in size or amount", "Results may vary."),
    ("achieve", "verb", "successfully reach a goal", "Achieve your objectives."),
    ("acquire", "verb", "buy or obtain", "Acquire new skills."),
    ("administration", "noun", "the management of affairs", "University administration."),
    ("affect", "verb", "have an effect on", "Weather affects mood."),
    ("appropriate", "adjective", "suitable for a purpose", "Choose appropriate methods."),
    ("aspect", "noun", "a particular part or feature", "Every aspect was considered."),
    ("assist", "verb", "help", "Assist with the project."),
    ("category", "noun", "a class or division", "Organize by category."),
    ("chapter", "noun", "a main division of a book", "Read chapter three."),
    ("commission", "noun", "a group given authority", "The commission reported."),
    ("community", "noun", "a group of people living together", "The local community."),
    ("complex", "adjective", "consisting of many parts", "A complex situation."),
    ("compute", "verb", "calculate using a computer", "Compute the average."),
    ("conclude", "verb", "bring to an end", "Conclude the discussion."),
    ("conduct", "verb", "organize and carry out", "Conduct an experiment."),
    ("consequent", "adjective", "following as a result", "The consequent effects."),
    ("construct", "verb", "build or make", "Construct a model."),
    ("consume", "verb", "use up a resource", "Consume less energy."),
    ("credit", "noun", "public acknowledgement", "Give credit where due."),
    ("culture", "noun", "the customs of a society", "Cultural differences exist."),
    ("design", "verb", "plan and make artistically", "Design a new system."),
    ("distinct", "adjective", "recognizably different", "Two distinct approaches."),
    ("element", "noun", "a component part", "A key element of success."),
    ("equate", "verb", "consider to be equal", "Don't equate the two."),
    ("evaluate", "verb", "assess the value of", "Evaluate the results."),
    ("feature", "noun", "a distinctive attribute", "A special feature."),
    ("final", "adjective", "coming at the end", "The final decision."),
    ("focus", "verb", "concentrate on", "Focus on priorities."),
    ("impact", "noun", "a marked effect", "The impact was significant."),
    ("injure", "verb", "do physical harm to", "Don't injure yourself."),
    ("institute", "noun", "an organization for a purpose", "A research institute."),
    ("invest", "verb", "put money into for profit", "Invest wisely."),
    ("item", "noun", "an individual article", "Each item was checked."),
    ("journal", "noun", "a periodical publication", "Published in a journal."),
    ("maintain", "verb", "cause to continue", "Maintain high standards."),
    ("normal", "adjective", "conforming to a standard", "Normal procedures apply."),
    ("obtain", "verb", "get or acquire", "Obtain permission first."),
    ("participate", "verb", "take part in", "Participate in activities."),
    ("perceive", "verb", "become aware of", "Perceive the difference."),
    ("positive", "adjective", "consisting in the presence of", "A positive outcome."),
    
    # IELTS Topic-Specific Vocabulary
    ("abandon", "verb", "give up completely", "Abandon the project."),
    ("abolish", "verb", "formally put an end to", "Abolish outdated laws."),
    ("absorb", "verb", "take in or soak up", "Plants absorb sunlight."),
    ("abstract", "adjective", "existing in thought only", "An abstract concept."),
    ("abundant", "adjective", "existing in large quantities", "Abundant resources."),
    ("accelerate", "verb", "increase in rate or speed", "Accelerate development."),
    ("access", "noun", "the means of approaching", "Access to education."),
    ("accommodate", "verb", "provide lodging for", "Accommodate guests."),
    ("accompany", "verb", "go somewhere with", "Accompany the delegation."),
    ("accomplish", "verb", "achieve or complete", "Accomplish your goals."),
    ("accumulate", "verb", "gather together", "Accumulate knowledge."),
    ("accurate", "adjective", "correct in all details", "Accurate information."),
    ("acknowledge", "verb", "accept or recognize", "Acknowledge the problem."),
    ("adapt", "verb", "make suitable for a new use", "Adapt to changes."),
    ("adequate", "adjective", "sufficient for a purpose", "Adequate funding."),
    ("adjacent", "adjective", "next to or adjoining", "Adjacent buildings."),
    ("adjust", "verb", "alter or move slightly", "Adjust the settings."),
    ("administer", "verb", "manage or be responsible for", "Administer the program."),
    ("advocate", "verb", "publicly recommend", "Advocate for change."),
    ("aggregate", "noun", "a whole formed by combining", "In aggregate terms."),
    ("allocate", "verb", "distribute for a purpose", "Allocate resources."),
    ("alter", "verb", "change in character", "Alter the plan."),
    ("alternative", "noun", "one of two choices", "Consider alternatives."),
    ("ambiguous", "adjective", "open to interpretation", "An ambiguous statement."),
    ("amend", "verb", "make minor changes to", "Amend the document."),
    ("analogy", "noun", "a comparison", "Draw an analogy."),
    ("annual", "adjective", "occurring once a year", "Annual reports."),
    ("anticipate", "verb", "regard as probable", "Anticipate problems."),
    ("apparent", "adjective", "clearly visible", "The reason was apparent."),
    ("append", "verb", "add to the end", "Append additional notes."),
    ("appreciate", "verb", "recognize the full worth of", "Appreciate the effort."),
    ("arbitrary", "adjective", "based on random choice", "An arbitrary decision."),
    ("assemble", "verb", "gather together", "Assemble the team."),
    ("assign", "verb", "allocate a task", "Assign responsibilities."),
    ("attach", "verb", "fasten or join", "Attach the document."),
    ("attain", "verb", "succeed in achieving", "Attain your goals."),
    ("attribute", "verb", "regard as caused by", "Attribute success to effort."),
    ("automate", "verb", "convert to automatic operation", "Automate the process."),
    
    # Common IELTS Writing Terms
    ("bias", "noun", "prejudice for or against", "Avoid bias in research."),
    ("bond", "noun", "a thing used to tie", "A strong bond."),
    ("brief", "adjective", "of short duration", "A brief summary."),
    ("bulk", "noun", "the mass or magnitude", "The bulk of evidence."),
    ("capable", "adjective", "having ability", "Capable of achieving."),
    ("capacity", "noun", "the maximum amount", "At full capacity."),
    ("cease", "verb", "bring or come to an end", "Cease operations."),
    ("challenge", "noun", "a task requiring effort", "A significant challenge."),
    ("channel", "noun", "a course for communication", "Communication channels."),
    ("chart", "noun", "a sheet of information", "The chart shows trends."),
    ("chemical", "adjective", "relating to chemistry", "Chemical reactions."),
    ("circumstance", "noun", "a fact related to an event", "Under the circumstances."),
    ("cite", "verb", "quote as evidence", "Cite your sources."),
    ("civil", "adjective", "relating to citizens", "Civil rights."),
    ("clarify", "verb", "make less confused", "Clarify the issue."),
    ("classic", "adjective", "judged over time to be of quality", "A classic example."),
    ("clause", "noun", "a unit of a sentence", "The main clause."),
    ("code", "noun", "a system of words or symbols", "A code of conduct."),
    ("coherent", "adjective", "logical and consistent", "A coherent argument."),
    ("coincide", "verb", "occur at the same time", "Events coincided."),
    ("collapse", "verb", "fall down suddenly", "The building collapsed."),
    ("colleague", "noun", "a person with whom one works", "Ask your colleagues."),
    ("commence", "verb", "begin", "Commence the project."),
    ("comment", "noun", "a verbal or written remark", "Please comment."),
    ("commodity", "noun", "a raw material", "A valuable commodity."),
    ("communicate", "verb", "share or exchange information", "Communicate effectively."),
    ("compatible", "adjective", "able to exist together", "Compatible systems."),
    ("compensate", "verb", "make up for", "Compensate for losses."),
    ("compile", "verb", "produce by assembling", "Compile the data."),
    ("complement", "noun", "a thing that completes", "A perfect complement."),
    ("comprehensive", "adjective", "complete and including all", "A comprehensive review."),
    ("comprise", "verb", "consist of", "The team comprises experts."),
    ("conceive", "verb", "form or devise in the mind", "Conceive a plan."),
    ("concentrate", "verb", "focus attention", "Concentrate on the task."),
    ("confirm", "verb", "establish the truth of", "Confirm the details."),
    ("conflict", "noun", "a serious disagreement", "A conflict of interest."),
    ("conform", "verb", "comply with rules", "Conform to standards."),
    ("consent", "noun", "permission for something", "Give informed consent."),
    ("considerable", "adjective", "notably large", "A considerable amount."),
    ("constrain", "verb", "compel or force", "Constrained by budget."),
    ("consult", "verb", "seek information from", "Consult an expert."),
    ("contemporary", "adjective", "living or occurring now", "Contemporary issues."),
    ("contradiction", "noun", "a combination of statements opposing each other", "A logical contradiction."),
    ("contrary", "adjective", "opposite in nature", "Contrary to expectations."),
    ("contribute", "verb", "give in order to help", "Contribute to the cause."),
    ("controversy", "noun", "prolonged public disagreement", "A major controversy."),
    ("convene", "verb", "come together for a meeting", "Convene a committee."),
    ("convention", "noun", "a way things are done", "Follow the convention."),
    ("convert", "verb", "change in form or function", "Convert to renewable energy."),
    ("convince", "verb", "cause to believe", "Convince the audience."),
    ("cooperate", "verb", "act jointly with another", "Cooperate on the project."),
    ("coordinate", "verb", "bring into proper relation", "Coordinate activities."),
    ("core", "noun", "the central part", "The core issue."),
    ("corporate", "adjective", "relating to a corporation", "Corporate responsibility."),
    ("correspond", "verb", "have a close similarity", "The results correspond."),
    ("couple", "noun", "two things of the same sort", "A couple of issues."),
    ("criteria", "noun", "standards by which to judge", "Meet the criteria."),
    ("crucial", "adjective", "of great importance", "A crucial decision."),
    ("currency", "noun", "a system of money", "Foreign currency."),
    ("cycle", "noun", "a series of events repeated", "The economic cycle."),
]

# =====================================================================
# BAND 7.0-7.5 최종 추가
# =====================================================================
BAND70_FINAL = [
    ("adhere", "verb", "stick fast to a surface", "Adhere to the guidelines."),
    ("adjacent", "adjective", "next to or adjoining", "Adjacent properties."),
    ("albeit", "conjunction", "although", "Successful, albeit slowly."),
    ("allege", "verb", "claim without proof", "He alleged wrongdoing."),
    ("allocate", "verb", "distribute for a purpose", "Allocate funds wisely."),
    ("allude", "verb", "suggest or call attention indirectly", "He alluded to the problem."),
    ("amass", "verb", "gather together in large amount", "Amass a fortune."),
    ("analogy", "noun", "a comparison between two things", "Draw an analogy."),
    ("anonymous", "adjective", "of unknown name or authorship", "An anonymous donor."),
    ("apparatus", "noun", "technical equipment or machinery", "Scientific apparatus."),
    ("arbitrary", "adjective", "based on random choice", "An arbitrary rule."),
    ("array", "noun", "an impressive display", "A wide array of options."),
    ("articulate", "verb", "express thoughts clearly", "Articulate your ideas."),
    ("aspiration", "noun", "a hope or ambition", "Career aspirations."),
    ("assertion", "noun", "a confident statement", "A bold assertion."),
    ("assimilate", "verb", "absorb and integrate", "Assimilate information."),
    ("attenuate", "verb", "reduce the force of", "Attenuate the signal."),
    ("attribute", "noun", "a quality or feature", "A key attribute."),
    ("augment", "verb", "make greater by adding", "Augment income."),
    ("auspicious", "adjective", "favorable; promising", "An auspicious start."),
    ("autonomous", "adjective", "having self-government", "An autonomous region."),
    ("averse", "adjective", "having a strong dislike", "Averse to risk."),
    ("belie", "verb", "fail to give a true impression", "Appearances belie reality."),
    ("beneficial", "adjective", "favorable or advantageous", "Mutually beneficial."),
    ("biased", "adjective", "unfairly prejudiced", "A biased opinion."),
    ("brevity", "noun", "concise and exact use of words", "Known for brevity."),
    ("bureaucratic", "adjective", "relating to a bureaucracy", "Bureaucratic procedures."),
    ("candid", "adjective", "truthful and straightforward", "A candid assessment."),
    ("capitalize", "verb", "take advantage of", "Capitalize on opportunities."),
    ("catalyst", "noun", "an agent that provokes change", "A catalyst for reform."),
    ("categorize", "verb", "place in a particular class", "Categorize the data."),
    ("cede", "verb", "give up power or territory", "Cede control."),
    ("censure", "verb", "express severe disapproval", "Censure the official."),
    ("certify", "verb", "confirm formally", "Certify the results."),
    ("circumscribe", "verb", "restrict within limits", "Powers are circumscribed."),
    ("cite", "verb", "quote as evidence", "Cite relevant studies."),
    ("clarify", "verb", "make clear or easier to understand", "Clarify your position."),
    ("coalesce", "verb", "come together to form one mass", "Ideas coalesced."),
    ("coerce", "verb", "persuade using force", "Cannot coerce compliance."),
    ("coherent", "adjective", "logical and consistent", "A coherent strategy."),
    ("coincide", "verb", "occur at the same time", "Events coincided."),
    ("collaborate", "verb", "work jointly with others", "Collaborate effectively."),
    ("commence", "verb", "begin", "Commence proceedings."),
    ("commensurate", "adjective", "corresponding in size or degree", "Salary commensurate with experience."),
    ("commodity", "noun", "a raw material or product", "A valuable commodity."),
    ("compatible", "adjective", "able to exist together", "Compatible approaches."),
    ("compel", "verb", "force or oblige", "Compelling evidence."),
    ("compensate", "verb", "make up for something", "Compensate for losses."),
    ("competence", "noun", "the ability to do something well", "Demonstrate competence."),
    ("compile", "verb", "produce by assembling", "Compile a report."),
    ("complement", "verb", "add to in a way that enhances", "Skills that complement."),
    ("complexity", "noun", "the state of being complex", "The complexity of the issue."),
    ("comply", "verb", "act in accordance with rules", "Comply with regulations."),
    ("comprise", "verb", "consist of; be composed of", "The committee comprises."),
    ("conceive", "verb", "form or devise in the mind", "Hard to conceive."),
    ("concise", "adjective", "giving much information briefly", "A concise summary."),
    ("concurrent", "adjective", "existing at the same time", "Concurrent developments."),
    ("condone", "verb", "accept behavior without criticism", "Cannot condone violence."),
    ("conducive", "adjective", "making something likely to happen", "Conducive to learning."),
    ("confer", "verb", "grant or bestow", "Confer authority."),
    ("confine", "verb", "keep within certain limits", "Confined to barracks."),
    ("confirm", "verb", "establish the truth of", "Confirm the findings."),
    ("conform", "verb", "comply with rules or standards", "Conform to norms."),
    ("confront", "verb", "face up to and deal with", "Confront the challenge."),
    ("consecutive", "adjective", "following continuously", "Three consecutive years."),
    ("consensus", "noun", "general agreement", "Reach a consensus."),
    ("consent", "noun", "permission for something to happen", "Informed consent."),
    ("consequent", "adjective", "following as a result", "Consequent changes."),
    ("considerable", "adjective", "notably large or important", "Considerable progress."),
    ("consistent", "adjective", "acting in the same way over time", "Consistent results."),
    ("consolidate", "verb", "make stronger or more solid", "Consolidate gains."),
    ("constitute", "verb", "be a part of a whole", "This constitutes progress."),
    ("constrain", "verb", "severely restrict", "Constrained by budget."),
    ("construct", "verb", "build or erect", "Construct a theory."),
    ("consult", "verb", "seek information or advice from", "Consult experts."),
    ("consume", "verb", "use up a resource", "Consume energy."),
    ("contemporary", "adjective", "living or occurring now", "Contemporary art."),
    ("contempt", "noun", "the feeling that someone is worthless", "Held in contempt."),
    ("contend", "verb", "struggle to surmount", "Contend with difficulties."),
    ("context", "noun", "the circumstances surrounding an event", "In this context."),
    ("contingent", "adjective", "dependent on circumstances", "Contingent upon approval."),
    ("contradict", "verb", "deny the truth of a statement", "Evidence contradicts claims."),
    ("contrary", "adjective", "opposite in nature or direction", "On the contrary."),
    ("contribute", "verb", "give something to help", "Contribute significantly."),
    ("controversy", "noun", "prolonged public disagreement", "Sparked controversy."),
    ("convene", "verb", "come or bring together for a meeting", "Convene a summit."),
    ("convention", "noun", "a way things are typically done", "By convention."),
    ("conversion", "noun", "the process of changing", "Energy conversion."),
    ("convert", "verb", "change in form or function", "Convert currencies."),
    ("convey", "verb", "make an idea known", "Convey the message."),
    ("convince", "verb", "persuade someone", "Convince stakeholders."),
    ("cooperate", "verb", "work together", "Countries cooperate."),
    ("coordinate", "verb", "bring into a common action", "Coordinate efforts."),
    ("core", "adjective", "central; most important", "Core principles."),
    ("corporate", "adjective", "relating to a large company", "Corporate culture."),
    ("correlate", "verb", "have a mutual relationship", "Factors correlate."),
    ("correspond", "verb", "have a close similarity", "Data corresponds."),
    ("counterpart", "noun", "a person or thing with the same function", "International counterparts."),
    ("credibility", "noun", "the quality of being trusted", "Damage credibility."),
]

# =====================================================================
# BAND 8.0+ 최종 추가
# =====================================================================
BAND80_FINAL = [
    ("judicious", "adjective", "having good judgment", "A judicious decision."),
    ("juxtapose", "verb", "place side by side", "Juxtapose the two views."),
    ("kinetic", "adjective", "relating to motion", "Kinetic energy."),
    ("labyrinthine", "adjective", "complicated like a maze", "Labyrinthine regulations."),
    ("lachrymose", "adjective", "tearful or given to weeping", "A lachrymose performance."),
    ("lambaste", "verb", "criticize harshly", "Critics lambasted the policy."),
    ("languid", "adjective", "displaying a lack of vigor", "A languid afternoon."),
    ("latent", "adjective", "existing but not yet developed", "Latent potential."),
    ("laudable", "adjective", "deserving praise", "A laudable effort."),
    ("laud", "verb", "praise highly", "Lauded for achievements."),
    ("lavish", "adjective", "sumptuously rich", "A lavish ceremony."),
    ("litigious", "adjective", "tending to engage in lawsuits", "A litigious society."),
    ("lucid", "adjective", "expressed clearly", "A lucid explanation."),
    ("ludicrous", "adjective", "so foolish as to be amusing", "A ludicrous suggestion."),
    ("luminous", "adjective", "full of or shedding light", "A luminous display."),
    ("machination", "noun", "a crafty scheme", "Political machinations."),
    ("magnanimity", "noun", "generosity", "Show magnanimity in victory."),
    ("malign", "verb", "speak about in a spitefully critical manner", "Malign someone's reputation."),
    ("malleable", "adjective", "easily influenced", "A malleable substance."),
    ("mandate", "noun", "an official order to do something", "A clear mandate."),
    ("manifest", "adjective", "clear and obvious", "A manifest improvement."),
    ("manipulate", "verb", "control or influence skillfully", "Manipulate data."),
    ("maudlin", "adjective", "self-pityingly sentimental", "Maudlin sentimentality."),
    ("maverick", "noun", "an independent-minded person", "A political maverick."),
    ("meander", "verb", "follow a winding course", "The river meanders."),
    ("mediate", "verb", "intervene to settle a dispute", "Mediate between parties."),
    ("mediocre", "adjective", "of only moderate quality", "A mediocre performance."),
    ("melancholy", "noun", "a feeling of pensive sadness", "A sense of melancholy."),
    ("melee", "noun", "a confused fight or scuffle", "A melee ensued."),
    ("meticulous", "adjective", "showing great attention to detail", "Meticulous planning."),
    ("miasma", "noun", "an unpleasant or unhealthy atmosphere", "A miasma of corruption."),
    ("milieu", "noun", "a person's social environment", "The academic milieu."),
    ("minuscule", "adjective", "extremely small", "A minuscule amount."),
    ("misanthrope", "noun", "a person who dislikes humankind", "A bitter misanthrope."),
    ("misnomer", "noun", "a wrong or inaccurate name", "A complete misnomer."),
    ("modicum", "noun", "a small quantity", "A modicum of truth."),
    ("mollify", "verb", "appease the anger of", "Attempts to mollify."),
    ("momentous", "adjective", "of great importance", "A momentous decision."),
    ("monotonous", "adjective", "dull and repetitive", "A monotonous task."),
    ("moot", "adjective", "subject to debate", "A moot point."),
    ("moribund", "adjective", "at the point of death", "A moribund industry."),
    ("mundane", "adjective", "lacking interest or excitement", "Mundane tasks."),
    ("munificent", "adjective", "more generous than is usual", "Munificent donations."),
    ("myriad", "noun", "a countless number", "A myriad of options."),
    ("nadir", "noun", "the lowest point", "Reached its nadir."),
    ("naive", "adjective", "showing lack of experience", "A naive assumption."),
    ("negate", "verb", "nullify or make ineffective", "Negate the effects."),
    ("negligent", "adjective", "failing to take proper care", "Negligent behavior."),
    ("nemesis", "noun", "a long-standing rival", "His political nemesis."),
    ("nomadic", "adjective", "living the life of a nomad", "Nomadic tribes."),
    ("nominal", "adjective", "existing in name only", "A nominal fee."),
    ("nonchalant", "adjective", "feeling casually calm", "A nonchalant attitude."),
    ("nostalgia", "noun", "a sentimental longing for the past", "A sense of nostalgia."),
    ("notorious", "adjective", "famous for something bad", "A notorious criminal."),
    ("novel", "adjective", "new or unusual", "A novel approach."),
    ("nuance", "noun", "a subtle difference", "Appreciate the nuances."),
    ("nullify", "verb", "make legally null", "Nullify the contract."),
    ("obdurate", "adjective", "stubbornly refusing to change", "Obdurate opposition."),
    ("objective", "adjective", "not influenced by personal feelings", "An objective analysis."),
    ("obligatory", "adjective", "required by rule", "Obligatory attendance."),
    ("oblique", "adjective", "neither parallel nor at right angles", "An oblique reference."),
    ("obliterate", "verb", "destroy utterly", "Obliterate all traces."),
    ("oblivious", "adjective", "not aware of what is happening", "Oblivious to danger."),
    ("obnoxious", "adjective", "extremely unpleasant", "Obnoxious behavior."),
    ("obscure", "adjective", "not discovered or known about", "An obscure reference."),
    ("obsolete", "adjective", "no longer produced or used", "Obsolete technology."),
    ("obstinate", "adjective", "stubbornly refusing to change", "An obstinate refusal."),
    ("obtuse", "adjective", "annoyingly insensitive or slow to understand", "Somewhat obtuse."),
    ("obviate", "verb", "remove a need or difficulty", "Obviate the need."),
    ("occlude", "verb", "stop, close up, or obstruct", "Occluded arteries."),
    ("odious", "adjective", "extremely unpleasant", "An odious task."),
    ("officious", "adjective", "assertive of authority in an annoying way", "An officious manner."),
    ("ominous", "adjective", "giving the impression that something bad will happen", "An ominous sign."),
    ("omnipotent", "adjective", "having unlimited power", "An omnipotent ruler."),
    ("onerous", "adjective", "involving heavy obligations", "Onerous duties."),
    ("opaque", "adjective", "not able to be seen through", "An opaque explanation."),
    ("opportune", "adjective", "well-chosen or particularly favorable", "An opportune moment."),
    ("oppress", "verb", "keep in subservience by force", "Oppress minorities."),
    ("optimal", "adjective", "best or most favorable", "Optimal conditions."),
    ("optimum", "adjective", "most conducive to a favorable outcome", "Optimum levels."),
    ("opulent", "adjective", "ostentatiously rich and luxurious", "An opulent lifestyle."),
    ("oration", "noun", "a formal speech", "A powerful oration."),
    ("orthodox", "adjective", "following traditional beliefs", "Orthodox views."),
    ("oscillate", "verb", "move back and forth", "Prices oscillate."),
    ("ostensible", "adjective", "stated or appearing to be true", "The ostensible reason."),
    ("ostentatious", "adjective", "characterized by pretentious display", "Ostentatious wealth."),
    ("oust", "verb", "drive out or expel", "Oust from power."),
    ("outmoded", "adjective", "old-fashioned", "Outmoded practices."),
    ("outweigh", "verb", "be heavier or more significant than", "Benefits outweigh risks."),
    ("overhaul", "verb", "examine thoroughly and make necessary repairs", "Overhaul the system."),
    ("overt", "adjective", "done openly", "Overt hostility."),
    ("overwrought", "adjective", "in a state of nervous excitement", "An overwrought response."),
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
print("📚 IELTS 단어 최종 생성 - 5000개 목표")
print("="*50 + "\n")

total_band60 = add_words_to_file('band60_words.json', BAND60_FINAL, 'Band 6.0-6.5')
total_band70 = add_words_to_file('band70_words.json', BAND70_FINAL, 'Band 7.0-7.5')
total_band80 = add_words_to_file('band80_words.json', BAND80_FINAL, 'Band 8.0+')

with open('assets/data/band45_words.json', 'r', encoding='utf-8') as f:
    band45_count = len(json.load(f))

total = band45_count + total_band60 + total_band70 + total_band80

print("\n" + "="*50)
print(f"📊 총 단어 현황:")
print(f"   Band 4.5-5.5: {band45_count}개")
print(f"   Band 6.0-6.5: {total_band60}개")
print(f"   Band 7.0-7.5: {total_band70}개")
print(f"   Band 8.0+: {total_band80}개")
print(f"   총계: {total}개")
print("="*50)

if total < 5000:
    print(f"\n⚠️ 5000개 목표까지 {5000-total}개 더 필요합니다.")
else:
    print(f"\n🎉 5000개 목표 달성!")
