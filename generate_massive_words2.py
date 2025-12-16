#!/usr/bin/env python3
"""
IELTS 단어 추가 생성 스크립트 2 - 5000개 목표 달성
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
# BAND 6.0-6.5 추가 단어 (가장 많이 필요 - 목표 1800개)
# =====================================================================
BAND60_MORE = [
    # Politics & Government
    ("administration", "noun", "the management of public affairs", "The administration announced new policies."),
    ("campaign", "noun", "organized course of action", "The election campaign started early."),
    ("candidate", "noun", "a person who applies for a position", "She is a strong candidate for the job."),
    ("coalition", "noun", "an alliance for combined action", "The coalition government was formed."),
    ("consensus", "noun", "general agreement", "They reached a consensus on the issue."),
    ("constituent", "noun", "a member of a constituency", "The politician met with constituents."),
    ("delegate", "noun", "a person sent to represent others", "Delegates attended the conference."),
    ("electorate", "noun", "all the people entitled to vote", "The electorate will decide."),
    ("governance", "noun", "the action of governing", "Good governance is essential."),
    ("manifesto", "noun", "a public declaration of policy", "The party released its manifesto."),
    ("parliament", "noun", "the highest legislative body", "Parliament debated the bill."),
    ("referendum", "noun", "a general vote on a single issue", "The referendum was held nationwide."),
    ("sanction", "noun", "an official penalty", "Economic sanctions were imposed."),
    ("statute", "noun", "a written law passed by a legislature", "The statute came into effect."),
    ("treaty", "noun", "a formally concluded agreement", "The treaty was signed by both nations."),
    
    # Technology & Computing
    ("application", "noun", "a program for a specific purpose", "Download the application on your phone."),
    ("authentication", "noun", "the process of verifying identity", "Two-factor authentication adds security."),
    ("automation", "noun", "use of machines to reduce human effort", "Automation increases productivity."),
    ("browser", "noun", "software for accessing the internet", "Open your web browser."),
    ("cache", "noun", "stored data for quick access", "Clear the browser cache."),
    ("compatible", "adjective", "able to work together", "The software is compatible with Windows."),
    ("configure", "verb", "arrange or set up", "Configure the settings properly."),
    ("connectivity", "noun", "the state of being connected", "Internet connectivity is essential."),
    ("cursor", "noun", "a movable indicator on a screen", "Move the cursor to click."),
    ("default", "noun", "a preset value or option", "Reset to default settings."),
    ("download", "verb", "copy data from one system to another", "Download the file from the website."),
    ("firewall", "noun", "a security system for networks", "The firewall blocked the attack."),
    ("hardware", "noun", "physical components of a computer", "The hardware needs upgrading."),
    ("malware", "noun", "software designed to cause damage", "Malware infected the computer."),
    ("software", "noun", "programs used by a computer", "Install the latest software update."),
    
    # Environment & Sustainability
    ("carbon", "noun", "a chemical element", "Reduce your carbon footprint."),
    ("climate", "noun", "weather conditions over time", "Climate change is a global concern."),
    ("drought", "noun", "prolonged period of low rainfall", "The drought affected crops severely."),
    ("endangered", "adjective", "at risk of extinction", "Many endangered species need protection."),
    ("fossil", "noun", "preserved remains of organisms", "Fossil fuels are non-renewable."),
    ("glacier", "noun", "a large mass of ice", "The glacier is melting rapidly."),
    ("greenhouse", "noun", "a glass building for plants", "Greenhouse gases trap heat."),
    ("landslide", "noun", "collapse of earth down a slope", "The landslide blocked the road."),
    ("ozone", "noun", "a form of oxygen", "The ozone layer protects us."),
    ("recycle", "verb", "convert waste into reusable material", "Recycle paper and plastic."),
    ("renewable", "adjective", "able to be replenished naturally", "Renewable energy sources include solar."),
    ("toxic", "adjective", "poisonous", "Toxic chemicals pollute rivers."),
    ("vegetation", "noun", "plants considered collectively", "Dense vegetation covered the area."),
    ("waste", "noun", "unwanted material", "Reduce waste by reusing items."),
    ("wildlife", "noun", "wild animals collectively", "Protect the local wildlife."),
    
    # Economics & Finance
    ("acquisition", "noun", "the act of acquiring something", "The company announced an acquisition."),
    ("asset", "noun", "a useful or valuable thing", "Property is a valuable asset."),
    ("bankruptcy", "noun", "state of being unable to pay debts", "The company filed for bankruptcy."),
    ("bond", "noun", "a certificate of debt", "Government bonds are safe investments."),
    ("broker", "noun", "an agent who arranges transactions", "The broker handled the deal."),
    ("capital", "noun", "wealth used to generate more wealth", "They raised capital for expansion."),
    ("credit", "noun", "the ability to borrow money", "She has good credit history."),
    ("currency", "noun", "a system of money", "The local currency is the dollar."),
    ("debt", "noun", "money owed to another", "Pay off your debt gradually."),
    ("dividend", "noun", "a payment to shareholders", "The company declared a dividend."),
    ("entrepreneur", "noun", "a person who starts a business", "The entrepreneur founded a startup."),
    ("franchise", "noun", "an authorization to sell products", "They bought a fast-food franchise."),
    ("gross", "adjective", "total before deductions", "The gross income was high."),
    ("inventory", "noun", "a complete list of items", "Check the inventory regularly."),
    ("investment", "noun", "the action of investing money", "Real estate is a good investment."),
    
    # Social Issues
    ("abuse", "noun", "cruel treatment", "Child abuse must be reported."),
    ("addiction", "noun", "the state of being dependent", "Addiction requires professional help."),
    ("advocacy", "noun", "public support for a cause", "Advocacy for human rights."),
    ("bias", "noun", "prejudice for or against something", "The report showed bias."),
    ("charity", "noun", "an organization helping those in need", "Donate to charity."),
    ("crisis", "noun", "a time of intense difficulty", "The housing crisis worsened."),
    ("discrimination", "noun", "unfair treatment", "Discrimination is prohibited."),
    ("diversity", "noun", "variety of different types", "Promote diversity in the workplace."),
    ("equality", "noun", "the state of being equal", "Equality before the law."),
    ("ethnic", "adjective", "relating to a population subgroup", "Ethnic diversity enriches society."),
    ("gender", "noun", "state of being male or female", "Gender equality is important."),
    ("harassment", "noun", "aggressive pressure or intimidation", "Report workplace harassment."),
    ("homeless", "adjective", "without a place to live", "Shelters help homeless people."),
    ("minority", "noun", "a smaller group in a community", "Protect minority rights."),
    ("poverty", "noun", "the state of being extremely poor", "Poverty affects millions."),
    
    # Arts & Culture
    ("aesthetic", "adjective", "concerned with beauty", "The aesthetic value is high."),
    ("artifact", "noun", "an object made by humans", "The museum displays ancient artifacts."),
    ("contemporary", "adjective", "living or occurring at same time", "Contemporary art is innovative."),
    ("creativity", "noun", "the use of imagination", "Creativity drives innovation."),
    ("exhibition", "noun", "a public display of items", "The exhibition opened yesterday."),
    ("gallery", "noun", "a room for displaying art", "Visit the art gallery."),
    ("heritage", "noun", "property that is inherited", "Cultural heritage must be preserved."),
    ("masterpiece", "noun", "an outstanding work of art", "The painting is a masterpiece."),
    ("monument", "noun", "a statue or building in memory", "The monument honors veterans."),
    ("orchestra", "noun", "a large group of musicians", "The orchestra performed brilliantly."),
    ("portrait", "noun", "a painting of a person", "The portrait hangs in the hall."),
    ("sculpture", "noun", "a carved or cast figure", "The sculpture is made of bronze."),
    ("symphony", "noun", "an elaborate musical composition", "Beethoven's symphony is famous."),
    ("theater", "noun", "a building for performances", "We went to the theater."),
    ("tradition", "noun", "a long-established custom", "Honor your family traditions."),
    
    # Media & Communication
    ("advertisement", "noun", "a public notice promoting something", "The advertisement was effective."),
    ("audience", "noun", "people watching or listening", "The audience applauded loudly."),
    ("broadcast", "verb", "transmit by radio or television", "The news will broadcast at six."),
    ("celebrity", "noun", "a famous person", "The celebrity attended the event."),
    ("channel", "noun", "a TV station", "Change the channel."),
    ("circulation", "noun", "the extent of newspaper distribution", "The paper has wide circulation."),
    ("column", "noun", "a regular article in a newspaper", "She writes a weekly column."),
    ("editor", "noun", "a person who prepares text", "The editor reviewed the manuscript."),
    ("headline", "noun", "a heading in a newspaper", "The headline caught my attention."),
    ("journalist", "noun", "a person who writes for media", "The journalist investigated the story."),
    ("magazine", "noun", "a periodical publication", "Subscribe to the magazine."),
    ("mainstream", "adjective", "conventional or widely accepted", "Mainstream media covered the story."),
    ("network", "noun", "a group of connected stations", "The TV network has many channels."),
    ("publicity", "noun", "notice or attention from the media", "The event received good publicity."),
    ("reporter", "noun", "a person who reports news", "The reporter covered the trial."),
    
    # Travel & Tourism
    ("accommodation", "noun", "a room or building for staying", "Book your accommodation early."),
    ("adventure", "noun", "an exciting experience", "Seek adventure when traveling."),
    ("attraction", "noun", "a place of interest to tourists", "The attraction draws millions."),
    ("cruise", "noun", "a voyage on a ship for pleasure", "The cruise was relaxing."),
    ("destination", "noun", "the place to which one travels", "Hawaii is a popular destination."),
    ("excursion", "noun", "a short journey for pleasure", "We took an excursion to the island."),
    ("expedition", "noun", "a journey for a specific purpose", "The expedition reached the summit."),
    ("guidebook", "noun", "a book of information for tourists", "Buy a guidebook before traveling."),
    ("itinerary", "noun", "a planned route or journey", "Check your itinerary carefully."),
    ("landmark", "noun", "an important recognizable feature", "The tower is a famous landmark."),
    ("luggage", "noun", "suitcases and bags", "Collect your luggage at the carousel."),
    ("passport", "noun", "an official travel document", "Don't forget your passport."),
    ("reservation", "noun", "an arrangement to secure a place", "Make a reservation for dinner."),
    ("souvenir", "noun", "an item bought as a reminder", "Buy a souvenir for your family."),
    ("tourist", "noun", "a person traveling for pleasure", "Tourists visit the museum daily."),
    
    # Health & Wellness
    ("allergy", "noun", "an adverse reaction to a substance", "He has a peanut allergy."),
    ("antibiotic", "noun", "a medicine that kills bacteria", "The doctor prescribed antibiotics."),
    ("calorie", "noun", "a unit of energy in food", "Count your calories daily."),
    ("cholesterol", "noun", "a fatty substance in blood", "High cholesterol is dangerous."),
    ("clinic", "noun", "a place for medical treatment", "Visit the clinic for a checkup."),
    ("contagious", "adjective", "spread by contact", "The disease is contagious."),
    ("diabetes", "noun", "a disease affecting blood sugar", "Manage diabetes with diet."),
    ("diet", "noun", "the kinds of food one eats", "Follow a healthy diet."),
    ("exercise", "noun", "physical activity for fitness", "Exercise regularly for good health."),
    ("hygiene", "noun", "conditions for maintaining health", "Practice good hygiene."),
    ("immune", "adjective", "resistant to a disease", "The vaccine makes you immune."),
    ("nutrition", "noun", "the process of taking in food", "Good nutrition is essential."),
    ("obesity", "noun", "the state of being very overweight", "Obesity increases health risks."),
    ("pharmacy", "noun", "a place where medicines are sold", "Buy medicine at the pharmacy."),
    ("stress", "noun", "mental or emotional strain", "Reduce stress through relaxation."),
    
    # Law & Justice
    ("attorney", "noun", "a person appointed to act for another", "Hire an attorney for legal advice."),
    ("bail", "noun", "money paid to release a prisoner", "The judge set bail at $10,000."),
    ("conviction", "noun", "a formal declaration of guilt", "The conviction was appealed."),
    ("custody", "noun", "the protective care of something", "The child is in custody."),
    ("defendant", "noun", "a person accused in a court", "The defendant pleaded not guilty."),
    ("evidence", "noun", "information supporting a conclusion", "The evidence was compelling."),
    ("jury", "noun", "a body of people giving a verdict", "The jury reached a verdict."),
    ("lawsuit", "noun", "a claim in a court of law", "File a lawsuit for damages."),
    ("legislation", "noun", "laws collectively", "New legislation was passed."),
    ("penalty", "noun", "a punishment for breaking a rule", "The penalty was severe."),
    ("plaintiff", "noun", "a person who brings a case", "The plaintiff sought damages."),
    ("prosecution", "noun", "the institution of legal proceedings", "The prosecution presented evidence."),
    ("sentence", "noun", "the punishment given by a court", "He received a light sentence."),
    ("testimony", "noun", "a formal statement under oath", "Her testimony was crucial."),
    ("verdict", "noun", "a decision on a disputed issue", "The verdict was guilty."),
    
    # Education Extended
    ("assessment", "noun", "the evaluation of someone's ability", "Regular assessment helps track progress."),
    ("attendance", "noun", "the action of being present", "Attendance is mandatory."),
    ("certificate", "noun", "an official document of achievement", "She received a certificate."),
    ("curriculum", "noun", "the subjects taught in a school", "The curriculum was updated."),
    ("degree", "noun", "an academic qualification", "He earned a master's degree."),
    ("diploma", "noun", "a certificate of academic achievement", "She received her diploma."),
    ("discipline", "noun", "a branch of knowledge", "History is an important discipline."),
    ("dormitory", "noun", "a residential hall at a school", "Students live in the dormitory."),
    ("enrollment", "noun", "the action of enrolling", "Enrollment begins next week."),
    ("examination", "noun", "a formal test of knowledge", "The examination was difficult."),
    ("graduate", "verb", "complete a course of study", "She will graduate next year."),
    ("lecture", "noun", "an educational talk", "Attend the lecture on history."),
    ("literacy", "noun", "the ability to read and write", "Promote literacy in schools."),
    ("semester", "noun", "half of an academic year", "The semester ends in May."),
    ("tuition", "noun", "a fee for instruction", "Tuition costs have increased."),
    
    # More Academic Words
    ("abstract", "adjective", "existing in thought rather than matter", "The concept is abstract."),
    ("academic", "adjective", "relating to education or scholarship", "Academic research requires rigor."),
    ("accurate", "adjective", "correct in all details", "The report was accurate."),
    ("achieve", "verb", "successfully reach a goal", "She achieved her dream."),
    ("acknowledge", "verb", "accept or recognize as true", "He acknowledged his mistake."),
    ("acquire", "verb", "buy or obtain", "Acquire new skills through training."),
    ("adequate", "adjective", "sufficient for a purpose", "The resources were adequate."),
    ("adjust", "verb", "alter or move slightly", "Adjust the settings as needed."),
    ("affect", "verb", "have an effect on", "Weather affects mood."),
    ("alternative", "noun", "another choice", "Consider the alternative options."),
    ("analyse", "verb", "examine in detail", "Analyse the data carefully."),
    ("apparent", "adjective", "clearly visible or understood", "The solution was apparent."),
    ("approach", "noun", "a way of dealing with something", "Try a different approach."),
    ("appropriate", "adjective", "suitable for a purpose", "Choose an appropriate response."),
    ("area", "noun", "a region or part of something", "The research area is narrow."),
]

# =====================================================================
# BAND 7.0-7.5 추가 단어
# =====================================================================
BAND70_MORE = [
    # Philosophy & Ethics
    ("aesthetic", "noun", "a set of principles about beauty", "The aesthetic of minimalism."),
    ("axiological", "adjective", "relating to the study of values", "An axiological approach to ethics."),
    ("benevolent", "adjective", "well meaning and kindly", "A benevolent ruler."),
    ("categorical", "adjective", "unconditional; absolute", "A categorical statement."),
    ("coherence", "noun", "logical and consistent connection", "The argument lacks coherence."),
    ("conundrum", "noun", "a confusing and difficult problem", "The ethical conundrum remains."),
    ("dialectic", "noun", "the art of investigating truth", "Socratic dialectic method."),
    ("dogma", "noun", "a principle laid down as truth", "Challenge established dogma."),
    ("egalitarian", "adjective", "believing in equality", "An egalitarian society."),
    ("empirical", "adjective", "based on observation", "Empirical evidence is key."),
    ("enigmatic", "adjective", "mysterious and puzzling", "An enigmatic smile."),
    ("esoteric", "adjective", "intended for a small group", "Esoteric knowledge."),
    ("existential", "adjective", "relating to existence", "An existential crisis."),
    ("fallacy", "noun", "a mistaken belief", "A logical fallacy."),
    ("hegemony", "noun", "leadership or dominance", "Cultural hegemony spreads."),
    
    # Law & Governance
    ("adjudicate", "verb", "make a formal judgment", "The court will adjudicate."),
    ("arbitration", "noun", "use of an arbitrator to settle dispute", "Seek arbitration for disputes."),
    ("codify", "verb", "arrange into a systematic code", "Codify the laws."),
    ("compliance", "noun", "acting in accordance with rules", "Ensure compliance with regulations."),
    ("culpable", "adjective", "deserving blame", "He was found culpable."),
    ("decree", "noun", "an official order", "The decree was issued."),
    ("deposition", "noun", "testimony under oath", "The deposition was recorded."),
    ("due diligence", "noun", "reasonable steps taken", "Perform due diligence."),
    ("eminent domain", "noun", "government's power to take property", "Eminent domain was invoked."),
    ("fiduciary", "adjective", "involving trust", "A fiduciary duty."),
    ("indemnity", "noun", "security against damage or loss", "Seek indemnity insurance."),
    ("injunction", "noun", "an authoritative warning or order", "The court issued an injunction."),
    ("jurisprudence", "noun", "the theory of law", "Study jurisprudence."),
    ("litigation", "noun", "the process of taking legal action", "Avoid costly litigation."),
    ("precedent", "noun", "an earlier event used as a guide", "Set a legal precedent."),
    
    # Science & Research
    ("anomalous", "adjective", "deviating from what is standard", "An anomalous result."),
    ("catalyze", "verb", "cause or accelerate a reaction", "The enzyme catalyzes the process."),
    ("causality", "noun", "the relationship between cause and effect", "Establish causality."),
    ("confounding", "adjective", "causing confusion or surprise", "A confounding variable."),
    ("correlate", "verb", "have a mutual relationship", "The factors correlate."),
    ("deriving", "verb", "obtaining from a source", "Deriving conclusions from data."),
    ("empiricism", "noun", "theory that knowledge comes from experience", "Empiricism guides science."),
    ("extrapolation", "noun", "extending known data into unknown", "Extrapolation of trends."),
    ("homogeneous", "adjective", "of the same kind", "A homogeneous mixture."),
    ("heterogeneous", "adjective", "diverse in character", "A heterogeneous population."),
    ("longitudinal", "adjective", "relating to development over time", "A longitudinal study."),
    ("null hypothesis", "noun", "the hypothesis that no difference exists", "Test the null hypothesis."),
    ("operationalize", "verb", "define in measurable terms", "Operationalize the concept."),
    ("replication", "noun", "the action of copying", "Replication of results is essential."),
    ("validity", "noun", "the quality of being logically sound", "Test validity is important."),
    
    # Economics Advanced
    ("amortization", "noun", "paying off debt over time", "Calculate amortization."),
    ("arbitrage", "noun", "exploiting price differences", "Arbitrage opportunities exist."),
    ("asymmetric", "adjective", "not identical on both sides", "Asymmetric information."),
    ("cartel", "noun", "an association of producers", "The oil cartel controls prices."),
    ("deflation", "noun", "reduction in prices", "Deflation affects the economy."),
    ("deregulation", "noun", "removal of regulations", "Financial deregulation occurred."),
    ("diversification", "noun", "making varied", "Portfolio diversification reduces risk."),
    ("elasticity", "noun", "responsiveness to price changes", "Price elasticity of demand."),
    ("externality", "noun", "a side effect on third parties", "Pollution is an externality."),
    ("fiscal", "adjective", "relating to government revenue", "Fiscal policy matters."),
    ("leverage", "noun", "use of borrowed capital", "High leverage increases risk."),
    ("liquidity", "noun", "availability of liquid assets", "Maintain liquidity."),
    ("macroeconomics", "noun", "economics of large-scale factors", "Study macroeconomics."),
    ("microeconomics", "noun", "economics of individual units", "Microeconomics analyzes firms."),
    ("monetarism", "noun", "theory emphasizing money supply", "Monetarism influenced policy."),
    
    # Psychology & Sociology
    ("attribution", "noun", "regarding something as caused by", "Attribution theory explains behavior."),
    ("cognition", "noun", "the mental action of acquiring knowledge", "Cognition declines with age."),
    ("conditioning", "noun", "training to behave in a certain way", "Classical conditioning experiments."),
    ("conformity", "noun", "compliance with standards", "Social conformity pressure."),
    ("deviance", "noun", "departure from usual standards", "Study social deviance."),
    ("dysfunction", "noun", "abnormality or impairment", "Family dysfunction affects children."),
    ("extrovert", "noun", "an outgoing person", "She is an extrovert."),
    ("heuristics", "noun", "mental shortcuts for decisions", "Heuristics simplify choices."),
    ("introvert", "noun", "a shy, reticent person", "Introverts need alone time."),
    ("longitudinal", "adjective", "over an extended time period", "A longitudinal research design."),
    ("neuroticism", "noun", "a tendency toward anxiety", "High neuroticism scores."),
    ("operant", "adjective", "involving the modification of behavior", "Operant conditioning."),
    ("pathology", "noun", "the science of diseases", "Study pathology."),
    ("psychometric", "adjective", "relating to psychological measurement", "Psychometric testing."),
    ("socialization", "noun", "the process of learning social norms", "Socialization begins early."),
    
    # More Band 7 Words
    ("acquiesce", "verb", "accept something reluctantly", "She acquiesced to the demands."),
    ("admonish", "verb", "warn or reprimand firmly", "The teacher admonished the student."),
    ("amalgamate", "verb", "combine or unite", "The companies amalgamated."),
    ("anathema", "noun", "something detested", "Violence is anathema to peace."),
    ("apprehension", "noun", "anxiety about the future", "She felt apprehension."),
    ("ascertain", "verb", "find something out for certain", "Ascertain the facts first."),
    ("aspiration", "noun", "a hope or ambition", "Her aspiration is to succeed."),
    ("assimilate", "verb", "absorb and integrate", "Assimilate new information."),
    ("attrition", "noun", "gradual reduction in strength", "Employee attrition is high."),
    ("austere", "adjective", "severe or strict", "An austere lifestyle."),
    ("averse", "adjective", "having a strong dislike", "He is averse to risk."),
    ("belie", "verb", "fail to give a true impression", "His smile belied his anger."),
    ("bolster", "verb", "support or strengthen", "Bolster the argument with evidence."),
    ("candid", "adjective", "truthful and straightforward", "A candid assessment."),
    ("capricious", "adjective", "given to sudden changes", "Capricious weather."),
]

# =====================================================================
# BAND 8.0+ 추가 단어
# =====================================================================
BAND80_MORE = [
    # Extremely Advanced Words
    ("abstruse", "adjective", "difficult to understand", "Abstruse philosophical arguments."),
    ("acrimonious", "adjective", "angry and bitter", "An acrimonious dispute."),
    ("adumbrate", "verb", "outline or foreshadow", "The report adumbrates future plans."),
    ("aggrandize", "verb", "increase power or reputation", "He sought to aggrandize himself."),
    ("alacrity", "noun", "brisk and cheerful readiness", "She accepted with alacrity."),
    ("ameliorative", "adjective", "making something better", "Ameliorative measures were taken."),
    ("anodyne", "adjective", "not likely to cause offense", "An anodyne statement."),
    ("antediluvian", "adjective", "extremely old-fashioned", "Antediluvian attitudes persist."),
    ("apostate", "noun", "one who abandons a belief", "He was branded an apostate."),
    ("approbation", "noun", "approval or praise", "Seek approbation from peers."),
    ("asperity", "noun", "harshness of tone or manner", "He spoke with asperity."),
    ("aspersion", "noun", "an attack on reputation", "Cast aspersions on character."),
    ("assiduous", "adjective", "showing great care and effort", "Assiduous research."),
    ("atavistic", "adjective", "relating to ancestral characteristics", "An atavistic fear."),
    ("aver", "verb", "state or assert to be the case", "She averred her innocence."),
    
    # More Sophisticated Vocabulary
    ("blandishment", "noun", "a flattering or pleasing statement", "Blandishments failed to persuade."),
    ("bombast", "noun", "high-sounding language with little meaning", "Political bombast."),
    ("cadge", "verb", "ask for or obtain by begging", "Cadge money from friends."),
    ("calumny", "noun", "the making of false statements", "Spread calumny about rivals."),
    ("captious", "adjective", "tending to find fault", "A captious critic."),
    ("caveat", "noun", "a warning or proviso", "A caveat to the agreement."),
    ("censure", "verb", "express severe disapproval", "The committee censured him."),
    ("chagrin", "noun", "distress or embarrassment", "Much to his chagrin."),
    ("chary", "adjective", "cautious or wary", "Chary of making promises."),
    ("chimera", "noun", "a thing hoped for but impossible", "The project is a chimera."),
    ("churlish", "adjective", "rude in a mean-spirited way", "A churlish response."),
    ("circumspect", "adjective", "wary and unwilling to take risks", "A circumspect approach."),
    ("clamorous", "adjective", "making a loud and confused noise", "Clamorous demands for change."),
    ("clandestine", "adjective", "kept secret or hidden", "A clandestine meeting."),
    ("cogent", "adjective", "clear, logical, and convincing", "A cogent argument."),
    
    # Rare Academic Terms
    ("complaisant", "adjective", "willing to please others", "A complaisant attitude."),
    ("concomitant", "adjective", "naturally accompanying", "Concomitant problems arose."),
    ("confound", "verb", "cause surprise or confusion", "The results confounded expectations."),
    ("contrite", "adjective", "feeling remorse", "A contrite apology."),
    ("contumacious", "adjective", "stubbornly disobedient", "Contumacious behavior."),
    ("convivial", "adjective", "friendly and lively", "A convivial atmosphere."),
    ("copious", "adjective", "abundant in supply", "Copious notes were taken."),
    ("countervail", "verb", "offset the effect of", "Countervail the criticism."),
    ("credulity", "noun", "tendency to believe readily", "Test one's credulity."),
    ("cursory", "adjective", "hasty and superficial", "A cursory glance."),
    ("decorous", "adjective", "in keeping with good taste", "Decorous behavior."),
    ("deleterious", "adjective", "causing harm or damage", "Deleterious effects on health."),
    ("demur", "verb", "raise doubts or objections", "She demurred at the suggestion."),
    ("denigrate", "verb", "criticize unfairly", "Denigrate the opposition."),
    ("denouement", "noun", "the final outcome", "An unexpected denouement."),
    
    # Additional Complex Words
    ("deprecate", "verb", "express disapproval of", "He deprecated the decision."),
    ("dereliction", "noun", "the state of being abandoned", "Dereliction of duty."),
    ("desultory", "adjective", "lacking a plan or purpose", "A desultory conversation."),
    ("diffident", "adjective", "modest or shy", "A diffident manner."),
    ("dilettante", "noun", "a person with superficial interest", "A mere dilettante."),
    ("discursive", "adjective", "digressing from subject to subject", "A discursive essay."),
    ("dispassionate", "adjective", "not influenced by emotion", "A dispassionate analysis."),
    ("dissemble", "verb", "conceal one's true feelings", "He dissembled his intentions."),
    ("dissolution", "noun", "the closing down of an assembly", "The dissolution of parliament."),
    ("ebullient", "adjective", "cheerful and full of energy", "An ebullient personality."),
    ("eclectic", "adjective", "deriving from various sources", "An eclectic taste."),
    ("edify", "verb", "instruct or improve morally", "An edifying experience."),
    ("effrontery", "noun", "insolent behavior", "The effrontery of his demands."),
    ("egregious", "adjective", "outstandingly bad", "An egregious error."),
    ("elucidate", "verb", "make clear", "Elucidate the point."),
    
    # Final Set
    ("enervate", "verb", "cause to feel drained", "The heat enervated everyone."),
    ("engender", "verb", "cause or give rise to", "Engender trust among partners."),
    ("ennui", "noun", "a feeling of listlessness", "Overcome by ennui."),
    ("ephemeral", "adjective", "lasting for a very short time", "Ephemeral fame."),
    ("equanimity", "noun", "mental calmness and composure", "Accept with equanimity."),
    ("equivocal", "adjective", "open to more than one interpretation", "An equivocal statement."),
    ("erudite", "adjective", "having great knowledge", "An erudite scholar."),
    ("eschew", "verb", "deliberately avoid", "Eschew violence."),
    ("esoteric", "adjective", "intended for a small group", "Esoteric knowledge."),
    ("eulogy", "noun", "a speech praising someone", "Deliver a eulogy."),
    ("evanescent", "adjective", "soon passing out of existence", "An evanescent moment."),
    ("excoriate", "verb", "criticize severely", "The review excoriated the book."),
    ("exigent", "adjective", "pressing; demanding", "Exigent circumstances."),
    ("expiate", "verb", "atone for wrongdoing", "Expiate one's sins."),
    ("expunge", "verb", "erase or remove completely", "Expunge the record."),
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
print("📚 IELTS 단어 추가 생성 2")
print("="*50 + "\n")

total_band60 = add_words_to_file('band60_words.json', BAND60_MORE, 'Band 6.0-6.5')
total_band70 = add_words_to_file('band70_words.json', BAND70_MORE, 'Band 7.0-7.5')
total_band80 = add_words_to_file('band80_words.json', BAND80_MORE, 'Band 8.0+')

# 기존 파일 로드하여 총계 계산
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
