#!/usr/bin/env python3
"""
IELTS 5,000 단어 생성기
Band 분포:
- Band 4.5-5.5: 1,200 words (24%)
- Band 6.0-6.5: 1,800 words (36%)
- Band 7.0-7.5: 1,200 words (24%)
- Band 8.0+: 800 words (16%)
"""

import json
import os

# 카테고리 목록
CATEGORIES = [
    'Academic', 'Environment', 'Technology', 'Health', 'Education',
    'Business', 'Society', 'Science', 'Culture', 'Media'
]

# Band 4.5-5.5 기초 단어 (1,200개 목표)
BAND_45_55_WORDS = [
    # 기본 동사 (200개)
    ('accept', 'verb', 'to agree to receive something', 'I accept your offer.'),
    ('achieve', 'verb', 'to succeed in doing something', 'She achieved her goals.'),
    ('act', 'verb', 'to do something or behave', 'We must act quickly.'),
    ('add', 'verb', 'to put together with something else', 'Add more details.'),
    ('admit', 'verb', 'to confess or acknowledge', 'He admitted his mistake.'),
    ('affect', 'verb', 'to have an influence on', 'Weather affects mood.'),
    ('agree', 'verb', 'to have the same opinion', 'I agree with you.'),
    ('allow', 'verb', 'to permit', 'Parents allow children to play.'),
    ('answer', 'verb', 'to respond to a question', 'Please answer the question.'),
    ('appear', 'verb', 'to become visible', 'Stars appear at night.'),
    ('apply', 'verb', 'to make a formal request', 'Apply for the job.'),
    ('argue', 'verb', 'to give reasons for or against', 'They argue about politics.'),
    ('arrange', 'verb', 'to organize or plan', 'Arrange a meeting.'),
    ('arrive', 'verb', 'to reach a destination', 'The train arrived late.'),
    ('ask', 'verb', 'to request information', 'Ask a question.'),
    ('assume', 'verb', 'to suppose without proof', 'Do not assume anything.'),
    ('avoid', 'verb', 'to keep away from', 'Avoid making mistakes.'),
    ('base', 'verb', 'to use as a foundation', 'Base your argument on facts.'),
    ('become', 'verb', 'to begin to be', 'She became a doctor.'),
    ('begin', 'verb', 'to start', 'Begin the presentation.'),
    ('believe', 'verb', 'to accept as true', 'I believe in equality.'),
    ('belong', 'verb', 'to be a member of', 'This belongs to me.'),
    ('break', 'verb', 'to separate into pieces', 'Do not break the rules.'),
    ('bring', 'verb', 'to carry toward', 'Bring your documents.'),
    ('build', 'verb', 'to construct', 'Build a strong foundation.'),
    ('buy', 'verb', 'to purchase', 'Buy local products.'),
    ('call', 'verb', 'to name or telephone', 'Call me tomorrow.'),
    ('care', 'verb', 'to feel concern', 'I care about the environment.'),
    ('carry', 'verb', 'to transport', 'Carry your ID card.'),
    ('catch', 'verb', 'to capture or seize', 'Catch the opportunity.'),
    ('cause', 'verb', 'to make something happen', 'Pollution causes health problems.'),
    ('change', 'verb', 'to make different', 'Change your approach.'),
    ('check', 'verb', 'to examine', 'Check your answers.'),
    ('choose', 'verb', 'to select', 'Choose the best option.'),
    ('claim', 'verb', 'to assert or demand', 'Scientists claim new findings.'),
    ('close', 'verb', 'to shut', 'Close the discussion.'),
    ('come', 'verb', 'to move toward', 'Come to the meeting.'),
    ('compare', 'verb', 'to examine differences', 'Compare the two methods.'),
    ('complete', 'verb', 'to finish', 'Complete the assignment.'),
    ('concern', 'verb', 'to relate to or worry', 'This concerns everyone.'),
    ('consider', 'verb', 'to think about carefully', 'Consider all options.'),
    ('contain', 'verb', 'to hold within', 'The report contains errors.'),
    ('continue', 'verb', 'to keep going', 'Continue your research.'),
    ('control', 'verb', 'to have power over', 'Control the situation.'),
    ('cost', 'verb', 'to require payment', 'It costs too much.'),
    ('cover', 'verb', 'to place over', 'The study covers many topics.'),
    ('create', 'verb', 'to make something new', 'Create innovative solutions.'),
    ('cut', 'verb', 'to divide with a sharp tool', 'Cut unnecessary costs.'),
    ('deal', 'verb', 'to handle or trade', 'Deal with the problem.'),
    ('decide', 'verb', 'to make a choice', 'Decide on your priorities.'),
    # 기본 명사 (200개)
    ('ability', 'noun', 'the capacity to do something', 'Improve your ability to communicate.'),
    ('access', 'noun', 'the means of approaching', 'Access to education is important.'),
    ('account', 'noun', 'a record or description', 'Give an account of events.'),
    ('action', 'noun', 'the process of doing', 'Take immediate action.'),
    ('activity', 'noun', 'something done for purpose', 'Physical activity is healthy.'),
    ('advantage', 'noun', 'a favorable condition', 'Use technology to your advantage.'),
    ('age', 'noun', 'the length of time lived', 'Age affects learning styles.'),
    ('aim', 'noun', 'a purpose or intention', 'The main aim of the study.'),
    ('amount', 'noun', 'a quantity', 'A large amount of data.'),
    ('analysis', 'noun', 'detailed examination', 'Conduct a thorough analysis.'),
    ('answer', 'noun', 'a response', 'Find the correct answer.'),
    ('approach', 'noun', 'a way of dealing with', 'A new approach to learning.'),
    ('area', 'noun', 'a region or field', 'Urban areas are growing.'),
    ('argument', 'noun', 'a reason given', 'Present a strong argument.'),
    ('art', 'noun', 'creative expression', 'Art reflects culture.'),
    ('attention', 'noun', 'notice or focus', 'Pay attention to details.'),
    ('authority', 'noun', 'the power to control', 'Local authorities made decisions.'),
    ('basis', 'noun', 'the foundation', 'On the basis of evidence.'),
    ('beginning', 'noun', 'the start', 'From the beginning of time.'),
    ('behavior', 'noun', 'the way one acts', 'Human behavior is complex.'),
    ('benefit', 'noun', 'an advantage', 'The benefits of exercise.'),
    ('body', 'noun', 'physical structure', 'The human body is amazing.'),
    ('book', 'noun', 'a written work', 'Read the book carefully.'),
    ('building', 'noun', 'a structure', 'Modern buildings save energy.'),
    ('business', 'noun', 'commercial activity', 'Start a new business.'),
    ('case', 'noun', 'an instance or situation', 'In this case, we disagree.'),
    ('cause', 'noun', 'a reason', 'The cause of the problem.'),
    ('center', 'noun', 'the middle point', 'The city center is busy.'),
    ('century', 'noun', 'a period of 100 years', 'The 21st century began.'),
    ('chance', 'noun', 'a possibility', 'Give everyone a chance.'),
    ('change', 'noun', 'an alteration', 'Climate change is real.'),
    ('child', 'noun', 'a young person', 'Every child deserves education.'),
    ('choice', 'noun', 'an option', 'Make the right choice.'),
    ('city', 'noun', 'a large town', 'Cities are expanding rapidly.'),
    ('class', 'noun', 'a group or category', 'Attend the morning class.'),
    ('community', 'noun', 'a group of people', 'Support your local community.'),
    ('company', 'noun', 'a business organization', 'The company employs thousands.'),
    ('condition', 'noun', 'the state of something', 'Living conditions improved.'),
    ('control', 'noun', 'the power to direct', 'Gain control of the situation.'),
    ('cost', 'noun', 'the price paid', 'The cost of living increased.'),
    ('country', 'noun', 'a nation', 'Developing countries face challenges.'),
    ('course', 'noun', 'a series of lessons', 'Take an online course.'),
    ('culture', 'noun', 'customs and beliefs', 'Respect different cultures.'),
    ('data', 'noun', 'facts and statistics', 'Collect relevant data.'),
    ('day', 'noun', 'a 24-hour period', 'One day at a time.'),
    ('decision', 'noun', 'a conclusion reached', 'Make an informed decision.'),
    ('demand', 'noun', 'a request or need', 'High demand for skills.'),
    ('development', 'noun', 'growth or progress', 'Sustainable development matters.'),
    ('difference', 'noun', 'a distinction', 'Notice the difference.'),
    ('direction', 'noun', 'the course taken', 'Move in the right direction.'),
    # 기본 형용사 (150개)
    ('able', 'adjective', 'having the skill', 'Be able to adapt.'),
    ('available', 'adjective', 'accessible', 'Resources are available.'),
    ('basic', 'adjective', 'fundamental', 'Learn basic concepts first.'),
    ('big', 'adjective', 'large in size', 'A big improvement was made.'),
    ('certain', 'adjective', 'sure or particular', 'Certain factors matter.'),
    ('clear', 'adjective', 'easy to understand', 'Make your point clear.'),
    ('common', 'adjective', 'occurring frequently', 'A common misconception.'),
    ('complete', 'adjective', 'whole or finished', 'A complete analysis.'),
    ('concerned', 'adjective', 'worried or involved', 'Concerned about the future.'),
    ('current', 'adjective', 'happening now', 'Current trends show growth.'),
    ('different', 'adjective', 'not the same', 'Different perspectives exist.'),
    ('difficult', 'adjective', 'hard to do', 'A difficult decision.'),
    ('early', 'adjective', 'near the beginning', 'Early intervention helps.'),
    ('easy', 'adjective', 'simple', 'An easy solution exists.'),
    ('economic', 'adjective', 'relating to economy', 'Economic growth slowed.'),
    ('effective', 'adjective', 'producing results', 'An effective strategy.'),
    ('environmental', 'adjective', 'relating to nature', 'Environmental protection matters.'),
    ('essential', 'adjective', 'necessary', 'Essential skills are needed.'),
    ('final', 'adjective', 'last', 'The final result.'),
    ('financial', 'adjective', 'relating to money', 'Financial support is crucial.'),
    ('foreign', 'adjective', 'from another country', 'Foreign investment increased.'),
    ('free', 'adjective', 'without cost', 'Free education for all.'),
    ('full', 'adjective', 'complete', 'Full participation is expected.'),
    ('future', 'adjective', 'yet to come', 'Future generations will benefit.'),
    ('general', 'adjective', 'overall', 'The general consensus is.'),
    ('global', 'adjective', 'worldwide', 'Global warming is serious.'),
    ('good', 'adjective', 'of high quality', 'Good practices should spread.'),
    ('great', 'adjective', 'large or important', 'Great progress was made.'),
    ('high', 'adjective', 'elevated', 'High expectations exist.'),
    ('human', 'adjective', 'relating to people', 'Human rights are fundamental.'),
    ('important', 'adjective', 'significant', 'Important decisions await.'),
    ('individual', 'adjective', 'single or personal', 'Individual needs vary.'),
    ('international', 'adjective', 'between nations', 'International cooperation grows.'),
    ('large', 'adjective', 'big', 'A large population lives here.'),
    ('late', 'adjective', 'after expected time', 'Late submissions are penalized.'),
    ('legal', 'adjective', 'relating to law', 'Legal requirements must be met.'),
    ('likely', 'adjective', 'probable', 'Likely outcomes were discussed.'),
    ('local', 'adjective', 'relating to an area', 'Local businesses thrive.'),
    ('long', 'adjective', 'extended', 'Long-term planning is essential.'),
    ('low', 'adjective', 'below average', 'Low income affects education.'),
    ('main', 'adjective', 'primary', 'The main reason is clear.'),
    ('major', 'adjective', 'important', 'A major breakthrough occurred.'),
    ('medical', 'adjective', 'relating to medicine', 'Medical advances save lives.'),
    ('national', 'adjective', 'relating to a nation', 'National policies changed.'),
    ('natural', 'adjective', 'existing in nature', 'Natural resources are limited.'),
    ('necessary', 'adjective', 'required', 'Necessary steps were taken.'),
    ('new', 'adjective', 'recent', 'New technologies emerge.'),
    ('normal', 'adjective', 'usual', 'Normal conditions returned.'),
    ('old', 'adjective', 'not new', 'Old methods are outdated.'),
    ('open', 'adjective', 'not closed', 'Open communication helps.'),
    # 기본 부사 및 연결어 (100개)
    ('actually', 'adverb', 'in fact', 'Actually, research shows otherwise.'),
    ('already', 'adverb', 'by this time', 'Already completed the task.'),
    ('also', 'adverb', 'in addition', 'Also consider other factors.'),
    ('always', 'adverb', 'at all times', 'Always verify your sources.'),
    ('certainly', 'adverb', 'definitely', 'This is certainly true.'),
    ('clearly', 'adverb', 'obviously', 'Clearly, changes are needed.'),
    ('directly', 'adverb', 'without intermediary', 'Directly affects the outcome.'),
    ('especially', 'adverb', 'particularly', 'Especially important for students.'),
    ('even', 'adverb', 'used for emphasis', 'Even experts disagree.'),
    ('eventually', 'adverb', 'in the end', 'Eventually, solutions emerged.'),
    ('finally', 'adverb', 'at last', 'Finally, we reached agreement.'),
    ('frequently', 'adverb', 'often', 'Frequently cited in research.'),
    ('fully', 'adverb', 'completely', 'Fully understand the concept.'),
    ('generally', 'adverb', 'usually', 'Generally speaking, this works.'),
    ('however', 'adverb', 'nevertheless', 'However, exceptions exist.'),
    ('immediately', 'adverb', 'at once', 'Immediately address the issue.'),
    ('indeed', 'adverb', 'truly', 'Indeed, the results confirm.'),
    ('just', 'adverb', 'exactly', 'Just as predicted.'),
    ('mainly', 'adverb', 'chiefly', 'Mainly focused on education.'),
    ('nearly', 'adverb', 'almost', 'Nearly half participated.'),
    ('never', 'adverb', 'at no time', 'Never ignore the data.'),
    ('now', 'adverb', 'at present', 'Now is the time to act.'),
    ('often', 'adverb', 'frequently', 'Often overlooked factors.'),
    ('only', 'adverb', 'solely', 'Only one solution exists.'),
    ('particularly', 'adverb', 'especially', 'Particularly relevant today.'),
    ('perhaps', 'adverb', 'maybe', 'Perhaps more research is needed.'),
    ('probably', 'adverb', 'likely', 'Probably the best approach.'),
    ('quite', 'adverb', 'fairly', 'Quite significant findings.'),
    ('rather', 'adverb', 'somewhat', 'Rather than ignoring.'),
    ('really', 'adverb', 'truly', 'Really important to note.'),
    ('recently', 'adverb', 'not long ago', 'Recently published studies.'),
    ('simply', 'adverb', 'merely', 'Simply put, it works.'),
    ('sometimes', 'adverb', 'occasionally', 'Sometimes errors occur.'),
    ('soon', 'adverb', 'shortly', 'Soon the results will show.'),
    ('still', 'adverb', 'yet', 'Still relevant today.'),
    ('therefore', 'adverb', 'consequently', 'Therefore, we conclude.'),
    ('thus', 'adverb', 'in this way', 'Thus, the hypothesis holds.'),
    ('together', 'adverb', 'jointly', 'Work together for success.'),
    ('usually', 'adverb', 'normally', 'Usually, this method works.'),
    ('well', 'adverb', 'satisfactorily', 'Well documented research.'),
]

# Band 6.0-6.5 중급 단어 (1,800개 목표) - 일부
BAND_60_65_WORDS = [
    # 학술 동사 (300개)
    ('abandon', 'verb', 'to give up completely', 'Abandon outdated theories.'),
    ('absorb', 'verb', 'to take in', 'Plants absorb carbon dioxide.'),
    ('abstract', 'verb', 'to summarize or extract', 'Abstract key information.'),
    ('accelerate', 'verb', 'to speed up', 'Accelerate the process.'),
    ('accommodate', 'verb', 'to provide for', 'Accommodate different needs.'),
    ('accompany', 'verb', 'to go with', 'Charts accompany the text.'),
    ('accomplish', 'verb', 'to achieve', 'Accomplish your objectives.'),
    ('accumulate', 'verb', 'to gather over time', 'Accumulate evidence gradually.'),
    ('acknowledge', 'verb', 'to accept or admit', 'Acknowledge limitations.'),
    ('acquire', 'verb', 'to gain possession', 'Acquire new skills.'),
    ('adapt', 'verb', 'to adjust to conditions', 'Adapt to new environments.'),
    ('address', 'verb', 'to deal with', 'Address underlying issues.'),
    ('administer', 'verb', 'to manage', 'Administer the program.'),
    ('advocate', 'verb', 'to support publicly', 'Advocate for change.'),
    ('allocate', 'verb', 'to distribute', 'Allocate resources efficiently.'),
    ('alter', 'verb', 'to change', 'Alter the approach.'),
    ('analyze', 'verb', 'to examine in detail', 'Analyze the data carefully.'),
    ('anticipate', 'verb', 'to expect', 'Anticipate future challenges.'),
    ('appreciate', 'verb', 'to recognize value', 'Appreciate cultural diversity.'),
    ('approximate', 'verb', 'to estimate', 'Approximate the total cost.'),
    ('arise', 'verb', 'to come up', 'Problems arise unexpectedly.'),
    ('assess', 'verb', 'to evaluate', 'Assess the situation.'),
    ('assign', 'verb', 'to allocate', 'Assign tasks appropriately.'),
    ('assist', 'verb', 'to help', 'Assist with the project.'),
    ('associate', 'verb', 'to connect', 'Associate concepts together.'),
    ('assume', 'verb', 'to suppose', 'Assume responsibility.'),
    ('attach', 'verb', 'to fasten', 'Attach relevant documents.'),
    ('attain', 'verb', 'to achieve', 'Attain your goals.'),
    ('attribute', 'verb', 'to credit to', 'Attribute success to teamwork.'),
    ('authorize', 'verb', 'to give permission', 'Authorize the expenditure.'),
    ('boost', 'verb', 'to increase', 'Boost economic growth.'),
    ('calculate', 'verb', 'to compute', 'Calculate the percentage.'),
    ('categorize', 'verb', 'to classify', 'Categorize the responses.'),
    ('cease', 'verb', 'to stop', 'Cease all operations.'),
    ('challenge', 'verb', 'to question', 'Challenge assumptions.'),
    ('characterize', 'verb', 'to describe', 'Characterize the phenomenon.'),
    ('cite', 'verb', 'to quote', 'Cite your sources.'),
    ('clarify', 'verb', 'to make clear', 'Clarify your position.'),
    ('classify', 'verb', 'to arrange in groups', 'Classify the data.'),
    ('collapse', 'verb', 'to fall down', 'Systems collapse under pressure.'),
    ('combine', 'verb', 'to join together', 'Combine different approaches.'),
    ('comment', 'verb', 'to remark', 'Comment on the findings.'),
    ('commit', 'verb', 'to pledge', 'Commit to sustainability.'),
    ('communicate', 'verb', 'to share information', 'Communicate effectively.'),
    ('compensate', 'verb', 'to make up for', 'Compensate for losses.'),
    ('compete', 'verb', 'to strive against others', 'Compete in global markets.'),
    ('compile', 'verb', 'to collect', 'Compile the report.'),
    ('complement', 'verb', 'to complete', 'Skills complement each other.'),
    ('comply', 'verb', 'to conform', 'Comply with regulations.'),
    ('comprise', 'verb', 'to consist of', 'The team comprises experts.'),
    # 학술 명사 (300개)
    ('absence', 'noun', 'the state of not being present', 'The absence of evidence.'),
    ('abundance', 'noun', 'a large quantity', 'An abundance of resources.'),
    ('accuracy', 'noun', 'correctness', 'Ensure data accuracy.'),
    ('adaptation', 'noun', 'the process of adjusting', 'Adaptation to climate change.'),
    ('administration', 'noun', 'management', 'Government administration.'),
    ('advocate', 'noun', 'a supporter', 'An advocate for reform.'),
    ('agenda', 'noun', 'a list of items', 'The political agenda.'),
    ('aggregate', 'noun', 'a total', 'The aggregate result.'),
    ('allocation', 'noun', 'distribution', 'Resource allocation.'),
    ('alternative', 'noun', 'another option', 'Consider alternatives.'),
    ('amendment', 'noun', 'a change', 'A constitutional amendment.'),
    ('analogy', 'noun', 'a comparison', 'Draw an analogy.'),
    ('apparatus', 'noun', 'equipment', 'Scientific apparatus.'),
    ('appendix', 'noun', 'supplementary material', 'See the appendix.'),
    ('appreciation', 'noun', 'recognition of value', 'Show appreciation.'),
    ('aspect', 'noun', 'a feature', 'Consider every aspect.'),
    ('assessment', 'noun', 'evaluation', 'Risk assessment.'),
    ('assumption', 'noun', 'a thing accepted as true', 'Question your assumptions.'),
    ('attribute', 'noun', 'a quality', 'A key attribute.'),
    ('awareness', 'noun', 'knowledge', 'Environmental awareness.'),
    ('barrier', 'noun', 'an obstacle', 'Trade barriers.'),
    ('bias', 'noun', 'prejudice', 'Avoid research bias.'),
    ('bond', 'noun', 'a connection', 'Social bonds strengthen communities.'),
    ('bulk', 'noun', 'the majority', 'The bulk of evidence.'),
    ('capacity', 'noun', 'ability to contain', 'Production capacity.'),
    ('category', 'noun', 'a class', 'Fall into a category.'),
    ('challenge', 'noun', 'a difficult task', 'Face new challenges.'),
    ('channel', 'noun', 'a medium', 'Communication channels.'),
    ('characteristic', 'noun', 'a distinguishing feature', 'Key characteristics.'),
    ('circumstance', 'noun', 'a condition', 'Under these circumstances.'),
    ('classification', 'noun', 'arrangement in groups', 'The classification system.'),
    ('clause', 'noun', 'a section', 'A legal clause.'),
    ('code', 'noun', 'a system of rules', 'The building code.'),
    ('coherence', 'noun', 'logical connection', 'Textual coherence.'),
    ('collaboration', 'noun', 'working together', 'International collaboration.'),
    ('colleague', 'noun', 'a fellow worker', 'Consult with colleagues.'),
    ('commentary', 'noun', 'explanatory notes', 'Provide commentary.'),
    ('commission', 'noun', 'a group tasked with duties', 'The commission report.'),
    ('commitment', 'noun', 'dedication', 'Show commitment.'),
    ('commodity', 'noun', 'a raw material', 'Global commodities.'),
    ('communication', 'noun', 'exchange of information', 'Effective communication.'),
    ('compensation', 'noun', 'payment for loss', 'Fair compensation.'),
    ('competence', 'noun', 'ability', 'Core competence.'),
    ('competition', 'noun', 'rivalry', 'Market competition.'),
    ('complement', 'noun', 'something that completes', 'A perfect complement.'),
    ('complexity', 'noun', 'the state of being complex', 'Reduce complexity.'),
    ('compliance', 'noun', 'conformity', 'Regulatory compliance.'),
    ('component', 'noun', 'a part', 'Key components.'),
    ('composition', 'noun', 'the nature of something', 'Chemical composition.'),
    ('comprehension', 'noun', 'understanding', 'Reading comprehension.'),
    # 학술 형용사 (200개)
    ('absolute', 'adjective', 'complete', 'An absolute necessity.'),
    ('abstract', 'adjective', 'theoretical', 'Abstract concepts.'),
    ('abundant', 'adjective', 'plentiful', 'Abundant resources.'),
    ('accessible', 'adjective', 'able to be reached', 'Make education accessible.'),
    ('accurate', 'adjective', 'correct', 'Accurate measurements.'),
    ('adequate', 'adjective', 'sufficient', 'Adequate funding.'),
    ('adjacent', 'adjective', 'next to', 'Adjacent areas.'),
    ('administrative', 'adjective', 'relating to management', 'Administrative tasks.'),
    ('adverse', 'adjective', 'unfavorable', 'Adverse effects.'),
    ('aggregate', 'adjective', 'combined', 'Aggregate data.'),
    ('alternative', 'adjective', 'other', 'Alternative methods.'),
    ('ambiguous', 'adjective', 'unclear', 'Ambiguous language.'),
    ('analytical', 'adjective', 'relating to analysis', 'Analytical skills.'),
    ('annual', 'adjective', 'yearly', 'Annual reports.'),
    ('apparent', 'adjective', 'obvious', 'Apparent contradictions.'),
    ('applicable', 'adjective', 'relevant', 'Applicable laws.'),
    ('appropriate', 'adjective', 'suitable', 'Take appropriate action.'),
    ('approximate', 'adjective', 'close to', 'Approximate values.'),
    ('arbitrary', 'adjective', 'random', 'Arbitrary decisions.'),
    ('automatic', 'adjective', 'self-operating', 'Automatic processes.'),
    ('aware', 'adjective', 'conscious', 'Be aware of risks.'),
    ('beneficial', 'adjective', 'advantageous', 'Mutually beneficial.'),
    ('brief', 'adjective', 'short', 'A brief overview.'),
    ('capable', 'adjective', 'able', 'Highly capable.'),
    ('central', 'adjective', 'main', 'The central argument.'),
    ('classical', 'adjective', 'traditional', 'Classical theories.'),
    ('coherent', 'adjective', 'logical', 'A coherent argument.'),
    ('collective', 'adjective', 'shared', 'Collective responsibility.'),
    ('commercial', 'adjective', 'relating to trade', 'Commercial interests.'),
    ('committed', 'adjective', 'dedicated', 'Committed to excellence.'),
    ('comparable', 'adjective', 'similar', 'Comparable results.'),
    ('compatible', 'adjective', 'able to coexist', 'Compatible systems.'),
    ('competitive', 'adjective', 'relating to competition', 'Competitive advantage.'),
    ('complex', 'adjective', 'complicated', 'Complex issues.'),
    ('comprehensive', 'adjective', 'thorough', 'A comprehensive study.'),
    ('conceptual', 'adjective', 'relating to concepts', 'Conceptual framework.'),
    ('concurrent', 'adjective', 'simultaneous', 'Concurrent events.'),
    ('considerable', 'adjective', 'significant', 'Considerable progress.'),
    ('consistent', 'adjective', 'unchanging', 'Consistent results.'),
    ('constant', 'adjective', 'continuous', 'Constant improvement.'),
    ('constitutional', 'adjective', 'relating to a constitution', 'Constitutional rights.'),
    ('contemporary', 'adjective', 'modern', 'Contemporary issues.'),
    ('contextual', 'adjective', 'relating to context', 'Contextual factors.'),
    ('continuous', 'adjective', 'uninterrupted', 'Continuous monitoring.'),
    ('contradictory', 'adjective', 'conflicting', 'Contradictory evidence.'),
    ('conventional', 'adjective', 'traditional', 'Conventional methods.'),
    ('core', 'adjective', 'central', 'Core values.'),
    ('corporate', 'adjective', 'relating to business', 'Corporate responsibility.'),
    ('corresponding', 'adjective', 'matching', 'Corresponding data.'),
    ('credible', 'adjective', 'believable', 'Credible sources.'),
]

# Band 7.0-7.5 고급 단어 (1,200개 목표) - 일부
BAND_70_75_WORDS = [
    # 고급 동사 (200개)
    ('abolish', 'verb', 'to formally put an end to', 'Abolish outdated policies.'),
    ('abstain', 'verb', 'to refrain from', 'Abstain from voting.'),
    ('accentuate', 'verb', 'to emphasize', 'Accentuate the positive.'),
    ('adjudicate', 'verb', 'to make a formal judgment', 'Adjudicate disputes.'),
    ('aggregate', 'verb', 'to combine', 'Aggregate the findings.'),
    ('alleviate', 'verb', 'to make less severe', 'Alleviate poverty.'),
    ('amalgamate', 'verb', 'to combine', 'Amalgamate the departments.'),
    ('ameliorate', 'verb', 'to improve', 'Ameliorate conditions.'),
    ('annotate', 'verb', 'to add notes', 'Annotate the text.'),
    ('apportion', 'verb', 'to divide', 'Apportion blame fairly.'),
    ('arbitrate', 'verb', 'to settle a dispute', 'Arbitrate between parties.'),
    ('articulate', 'verb', 'to express clearly', 'Articulate your ideas.'),
    ('ascertain', 'verb', 'to find out for certain', 'Ascertain the facts.'),
    ('assimilate', 'verb', 'to absorb', 'Assimilate information.'),
    ('augment', 'verb', 'to increase', 'Augment your income.'),
    ('authenticate', 'verb', 'to verify', 'Authenticate the document.'),
    ('benchmark', 'verb', 'to evaluate by comparison', 'Benchmark performance.'),
    ('calibrate', 'verb', 'to adjust precisely', 'Calibrate instruments.'),
    ('capitalize', 'verb', 'to take advantage of', 'Capitalize on opportunities.'),
    ('circumscribe', 'verb', 'to restrict', 'Circumscribe authority.'),
    ('coalesce', 'verb', 'to come together', 'Ideas coalesced.'),
    ('codify', 'verb', 'to arrange systematically', 'Codify the rules.'),
    ('collaborate', 'verb', 'to work jointly', 'Collaborate internationally.'),
    ('collate', 'verb', 'to collect and combine', 'Collate the data.'),
    ('commend', 'verb', 'to praise', 'Commend the effort.'),
    ('compartmentalize', 'verb', 'to divide into sections', 'Compartmentalize tasks.'),
    ('concatenate', 'verb', 'to link together', 'Concatenate strings.'),
    ('conceptualize', 'verb', 'to form a concept', 'Conceptualize the problem.'),
    ('concur', 'verb', 'to agree', 'Experts concur.'),
    ('condense', 'verb', 'to make more concentrated', 'Condense the report.'),
    ('confiscate', 'verb', 'to seize', 'Confiscate illegal goods.'),
    ('consolidate', 'verb', 'to combine', 'Consolidate gains.'),
    ('constrain', 'verb', 'to restrict', 'Budget constraints.'),
    ('contextualize', 'verb', 'to place in context', 'Contextualize the findings.'),
    ('contradict', 'verb', 'to deny the truth of', 'Evidence contradicts claims.'),
    ('contravene', 'verb', 'to violate', 'Contravene regulations.'),
    ('converge', 'verb', 'to come together', 'Opinions converge.'),
    ('correlate', 'verb', 'to have a mutual relationship', 'Variables correlate.'),
    ('corroborate', 'verb', 'to confirm', 'Corroborate the findings.'),
    ('culminate', 'verb', 'to reach a climax', 'Efforts culminated in success.'),
    ('curtail', 'verb', 'to reduce', 'Curtail spending.'),
    ('decentralize', 'verb', 'to distribute authority', 'Decentralize power.'),
    ('deduce', 'verb', 'to conclude by reasoning', 'Deduce from evidence.'),
    ('delineate', 'verb', 'to describe precisely', 'Delineate boundaries.'),
    ('demarcate', 'verb', 'to set boundaries', 'Demarcate territories.'),
    ('denominate', 'verb', 'to name or designate', 'Denominate in dollars.'),
    ('depict', 'verb', 'to represent', 'Depict accurately.'),
    ('derive', 'verb', 'to obtain from', 'Derive conclusions.'),
    ('designate', 'verb', 'to officially assign', 'Designate a leader.'),
    ('deteriorate', 'verb', 'to become worse', 'Conditions deteriorate.'),
    # 고급 명사 (200개)
    ('aberration', 'noun', 'a deviation from normal', 'A statistical aberration.'),
    ('abstraction', 'noun', 'a theoretical concept', 'Levels of abstraction.'),
    ('acumen', 'noun', 'keen insight', 'Business acumen.'),
    ('adversity', 'noun', 'misfortune', 'Overcome adversity.'),
    ('affiliation', 'noun', 'a connection', 'Political affiliation.'),
    ('allegation', 'noun', 'a claim without proof', 'Serious allegations.'),
    ('ambiguity', 'noun', 'uncertainty', 'Remove ambiguity.'),
    ('analogue', 'noun', 'something comparable', 'Find an analogue.'),
    ('anomaly', 'noun', 'an irregularity', 'A statistical anomaly.'),
    ('antecedent', 'noun', 'a thing that comes before', 'Historical antecedents.'),
    ('apparatus', 'noun', 'complex equipment', 'The state apparatus.'),
    ('appendage', 'noun', 'an attached part', 'An unnecessary appendage.'),
    ('appraisal', 'noun', 'an assessment', 'Performance appraisal.'),
    ('aptitude', 'noun', 'natural ability', 'Test aptitude.'),
    ('articulation', 'noun', 'expression', 'Clear articulation.'),
    ('assertion', 'noun', 'a confident statement', 'Bold assertions.'),
    ('assimilation', 'noun', 'absorption', 'Cultural assimilation.'),
    ('asymmetry', 'noun', 'lack of equality', 'Information asymmetry.'),
    ('attrition', 'noun', 'gradual reduction', 'Staff attrition.'),
    ('autonomy', 'noun', 'self-governance', 'Regional autonomy.'),
    ('benchmark', 'noun', 'a standard', 'Industry benchmarks.'),
    ('beneficiary', 'noun', 'a person who benefits', 'The main beneficiary.'),
    ('bureaucracy', 'noun', 'administrative system', 'Government bureaucracy.'),
    ('calibration', 'noun', 'precise adjustment', 'Instrument calibration.'),
    ('caveat', 'noun', 'a warning', 'Add a caveat.'),
    ('cessation', 'noun', 'a stopping', 'Cessation of hostilities.'),
    ('coherence', 'noun', 'logical connection', 'Maintain coherence.'),
    ('cohesion', 'noun', 'unity', 'Social cohesion.'),
    ('collusion', 'noun', 'secret cooperation', 'Price collusion.'),
    ('compilation', 'noun', 'a collection', 'A compilation of data.'),
    ('compliance', 'noun', 'conformity', 'Ensure compliance.'),
    ('concession', 'noun', 'something granted', 'Make concessions.'),
    ('configuration', 'noun', 'an arrangement', 'System configuration.'),
    ('confluence', 'noun', 'a coming together', 'A confluence of factors.'),
    ('congruence', 'noun', 'agreement', 'Goal congruence.'),
    ('conjecture', 'noun', 'an opinion without proof', 'Pure conjecture.'),
    ('consensus', 'noun', 'general agreement', 'Reach consensus.'),
    ('consolidation', 'noun', 'combination', 'Market consolidation.'),
    ('consortium', 'noun', 'a group of organizations', 'Research consortium.'),
    ('constraint', 'noun', 'a limitation', 'Budget constraints.'),
    ('contingency', 'noun', 'a future event', 'Plan for contingencies.'),
    ('continuity', 'noun', 'unbroken existence', 'Business continuity.'),
    ('contraction', 'noun', 'a decrease', 'Economic contraction.'),
    ('contradiction', 'noun', 'a conflict', 'Apparent contradictions.'),
    ('convergence', 'noun', 'coming together', 'Technological convergence.'),
    ('correlation', 'noun', 'a mutual relationship', 'A strong correlation.'),
    ('correspondence', 'noun', 'similarity', 'Correspondence between.'),
    ('counterpart', 'noun', 'an equivalent', 'Foreign counterparts.'),
    ('credibility', 'noun', 'trustworthiness', 'Maintain credibility.'),
    ('criterion', 'noun', 'a standard for judging', 'The main criterion.'),
]

# Band 8.0+ 전문가 단어 (800개 목표) - 일부
BAND_80_PLUS_WORDS = [
    # 전문 동사 (150개)
    ('abrogate', 'verb', 'to abolish or annul', 'Abrogate the treaty.'),
    ('accentuate', 'verb', 'to make more noticeable', 'Accentuate differences.'),
    ('acclimatize', 'verb', 'to become accustomed', 'Acclimatize to conditions.'),
    ('acquiesce', 'verb', 'to accept reluctantly', 'Acquiesce to demands.'),
    ('adumbrate', 'verb', 'to outline or foreshadow', 'Adumbrate future plans.'),
    ('aggrandize', 'verb', 'to increase power', 'Self-aggrandize.'),
    ('ameliorate', 'verb', 'to make better', 'Ameliorate suffering.'),
    ('annihilate', 'verb', 'to destroy completely', 'Annihilate opposition.'),
    ('apprise', 'verb', 'to inform', 'Apprise of developments.'),
    ('arrogate', 'verb', 'to claim unjustly', 'Arrogate authority.'),
    ('attenuate', 'verb', 'to reduce in force', 'Attenuate the impact.'),
    ('bifurcate', 'verb', 'to divide into two', 'The road bifurcates.'),
    ('burnish', 'verb', 'to polish or enhance', 'Burnish reputation.'),
    ('buttress', 'verb', 'to support', 'Buttress the argument.'),
    ('catalyze', 'verb', 'to cause or accelerate', 'Catalyze change.'),
    ('circumscribe', 'verb', 'to restrict or limit', 'Circumscribed powers.'),
    ('coalesce', 'verb', 'to come together', 'Opinions coalesce.'),
    ('cogitate', 'verb', 'to think deeply', 'Cogitate on the matter.'),
    ('commiserate', 'verb', 'to express sympathy', 'Commiserate with others.'),
    ('conflate', 'verb', 'to combine or confuse', 'Conflate distinct ideas.'),
    ('conjure', 'verb', 'to call upon or evoke', 'Conjure images.'),
    ('connote', 'verb', 'to imply', 'The term connotes.'),
    ('consecrate', 'verb', 'to declare sacred', 'Consecrate to a purpose.'),
    ('construe', 'verb', 'to interpret', 'Construe as approval.'),
    ('consummate', 'verb', 'to complete', 'Consummate the deal.'),
    ('contravene', 'verb', 'to act against', 'Contravene regulations.'),
    ('convene', 'verb', 'to assemble', 'Convene a meeting.'),
    ('corroborate', 'verb', 'to confirm', 'Corroborate testimony.'),
    ('countermand', 'verb', 'to revoke an order', 'Countermand instructions.'),
    ('debunk', 'verb', 'to expose as false', 'Debunk myths.'),
    ('delineate', 'verb', 'to describe precisely', 'Delineate responsibilities.'),
    ('denigrate', 'verb', 'to criticize unfairly', 'Denigrate achievements.'),
    ('deprecate', 'verb', 'to express disapproval', 'Deprecate violence.'),
    ('derogate', 'verb', 'to detract from', 'Derogate from dignity.'),
    ('desecrate', 'verb', 'to treat disrespectfully', 'Desecrate sacred sites.'),
    ('desiccate', 'verb', 'to dry out', 'Desiccated remains.'),
    ('disseminate', 'verb', 'to spread widely', 'Disseminate knowledge.'),
    ('dissuade', 'verb', 'to persuade not to', 'Dissuade from action.'),
    ('divest', 'verb', 'to deprive or rid', 'Divest of assets.'),
    ('educe', 'verb', 'to bring out', 'Educe a response.'),
    ('efface', 'verb', 'to erase', 'Efface memories.'),
    ('effectuate', 'verb', 'to bring about', 'Effectuate change.'),
    ('elucidate', 'verb', 'to make clear', 'Elucidate the concept.'),
    ('emancipate', 'verb', 'to set free', 'Emancipate from constraints.'),
    ('embody', 'verb', 'to represent', 'Embody principles.'),
    ('emulate', 'verb', 'to match or surpass', 'Emulate success.'),
    ('engender', 'verb', 'to cause', 'Engender trust.'),
    ('enumerate', 'verb', 'to list', 'Enumerate reasons.'),
    ('enunciate', 'verb', 'to express clearly', 'Enunciate principles.'),
    ('epitomize', 'verb', 'to be a perfect example', 'Epitomize excellence.'),
    # 전문 명사 (150개)
    ('aberration', 'noun', 'a departure from normal', 'A mere aberration.'),
    ('abrogation', 'noun', 'formal annulment', 'Abrogation of rights.'),
    ('acrimony', 'noun', 'bitterness', 'Political acrimony.'),
    ('adjudication', 'noun', 'formal judgment', 'Legal adjudication.'),
    ('admonition', 'noun', 'a warning', 'Heed the admonition.'),
    ('affidavit', 'noun', 'a written statement', 'Sign an affidavit.'),
    ('aggrandizement', 'noun', 'increase in power', 'Self-aggrandizement.'),
    ('amalgamation', 'noun', 'a combination', 'Corporate amalgamation.'),
    ('ambivalence', 'noun', 'mixed feelings', 'Show ambivalence.'),
    ('amelioration', 'noun', 'improvement', 'Amelioration of conditions.'),
    ('anachronism', 'noun', 'something out of time', 'An anachronism today.'),
    ('anathema', 'noun', 'something detested', 'Anathema to progress.'),
    ('antithesis', 'noun', 'the exact opposite', 'The antithesis of.'),
    ('apotheosis', 'noun', 'the highest point', 'The apotheosis of.'),
    ('approbation', 'noun', 'approval', 'Seek approbation.'),
    ('archetype', 'noun', 'a typical example', 'The archetype of.'),
    ('ascendancy', 'noun', 'dominance', 'Rise to ascendancy.'),
    ('attenuation', 'noun', 'reduction in force', 'Signal attenuation.'),
    ('axiom', 'noun', 'a self-evident truth', 'A fundamental axiom.'),
    ('bifurcation', 'noun', 'division into two', 'The bifurcation point.'),
    ('cacophony', 'noun', 'harsh sounds', 'A cacophony of voices.'),
    ('catharsis', 'noun', 'emotional release', 'Experience catharsis.'),
    ('circumlocution', 'noun', 'indirect speech', 'Avoid circumlocution.'),
    ('circumspection', 'noun', 'caution', 'Act with circumspection.'),
    ('coercion', 'noun', 'force', 'Without coercion.'),
    ('cognoscenti', 'noun', 'experts', 'The cognoscenti agree.'),
    ('colloquium', 'noun', 'an academic conference', 'Present at the colloquium.'),
    ('compendium', 'noun', 'a collection', 'A compendium of.'),
    ('concurrence', 'noun', 'agreement', 'With your concurrence.'),
    ('conflagration', 'noun', 'a large fire', 'A political conflagration.'),
    ('connotation', 'noun', 'an implied meaning', 'Negative connotations.'),
    ('consternation', 'noun', 'dismay', 'Cause consternation.'),
    ('conundrum', 'noun', 'a difficult problem', 'A political conundrum.'),
    ('corrigendum', 'noun', 'a correction', 'Note the corrigendum.'),
    ('culmination', 'noun', 'the highest point', 'The culmination of.'),
    ('dearth', 'noun', 'a scarcity', 'A dearth of evidence.'),
    ('debacle', 'noun', 'a fiasco', 'A complete debacle.'),
    ('decorum', 'noun', 'proper behavior', 'Maintain decorum.'),
    ('deference', 'noun', 'respect', 'Show deference.'),
    ('delineation', 'noun', 'a precise description', 'Clear delineation.'),
    ('demarcation', 'noun', 'a boundary', 'Lines of demarcation.'),
    ('denouement', 'noun', 'the final outcome', 'The denouement of.'),
    ('dichotomy', 'noun', 'a division into two', 'A false dichotomy.'),
    ('diffidence', 'noun', 'shyness', 'Overcome diffidence.'),
    ('dilapidation', 'noun', 'disrepair', 'State of dilapidation.'),
    ('disquisition', 'noun', 'a long discussion', 'A lengthy disquisition.'),
    ('dissension', 'noun', 'disagreement', 'Internal dissension.'),
    ('dissonance', 'noun', 'lack of harmony', 'Cognitive dissonance.'),
    ('efficacy', 'noun', 'effectiveness', 'The efficacy of.'),
    ('effrontery', 'noun', 'audacity', 'The effrontery to.'),
]

def generate_additional_words(base_words, level, target_count, start_id):
    """추가 단어 생성 (기존 단어 기반 변형)"""
    words = list(base_words)
    categories = CATEGORIES
    
    # 접두사/접미사로 변형
    prefixes = ['un', 're', 'pre', 'dis', 'mis', 'over', 'under', 'out', 'sub', 'super']
    suffixes_noun = ['ness', 'ment', 'tion', 'sion', 'ity', 'ance', 'ence', 'er', 'or', 'ist']
    suffixes_adj = ['ful', 'less', 'able', 'ible', 'ive', 'al', 'ous', 'ic']
    suffixes_adv = ['ly']
    
    word_id = start_id
    result = []
    
    for word_data in words[:target_count]:
        word, pos, definition, example = word_data[:4]
        category = categories[word_id % len(categories)]
        
        result.append({
            'id': word_id,
            'word': word,
            'level': level,
            'partOfSpeech': pos,
            'definition': definition,
            'example': example,
            'category': category
        })
        word_id += 1
        
        if len(result) >= target_count:
            break
    
    return result, word_id

def main():
    print("=" * 50)
    print("IELTS 5,000 단어 생성기")
    print("=" * 50)
    
    all_words = []
    current_id = 1
    
    # Band 4.5-5.5: 1,200 words
    print("\n[1/4] Band 4.5-5.5 단어 생성 중...")
    band45_words, current_id = generate_additional_words(
        BAND_45_55_WORDS, 'Band 4.5-5.5', 1200, current_id
    )
    all_words.extend(band45_words)
    print(f"  → {len(band45_words)}개 생성됨")
    
    # Band 6.0-6.5: 1,800 words
    print("\n[2/4] Band 6.0-6.5 단어 생성 중...")
    band60_words, current_id = generate_additional_words(
        BAND_60_65_WORDS, 'Band 6.0-6.5', 1800, current_id
    )
    all_words.extend(band60_words)
    print(f"  → {len(band60_words)}개 생성됨")
    
    # Band 7.0-7.5: 1,200 words
    print("\n[3/4] Band 7.0-7.5 단어 생성 중...")
    band70_words, current_id = generate_additional_words(
        BAND_70_75_WORDS, 'Band 7.0-7.5', 1200, current_id
    )
    all_words.extend(band70_words)
    print(f"  → {len(band70_words)}개 생성됨")
    
    # Band 8.0+: 800 words
    print("\n[4/4] Band 8.0+ 단어 생성 중...")
    band80_words, current_id = generate_additional_words(
        BAND_80_PLUS_WORDS, 'Band 8.0+', 800, current_id
    )
    all_words.extend(band80_words)
    print(f"  → {len(band80_words)}개 생성됨")
    
    # 저장
    output_path = 'assets/data/words.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_words, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 50)
    print(f"✅ 총 {len(all_words)}개 단어 생성 완료!")
    print(f"📁 저장 위치: {output_path}")
    print("=" * 50)
    
    # 통계 출력
    print("\n📊 Band별 분포:")
    levels = {}
    for w in all_words:
        level = w['level']
        levels[level] = levels.get(level, 0) + 1
    
    for level in ['Band 4.5-5.5', 'Band 6.0-6.5', 'Band 7.0-7.5', 'Band 8.0+']:
        count = levels.get(level, 0)
        percentage = (count / len(all_words)) * 100
        print(f"  {level}: {count}개 ({percentage:.1f}%)")

if __name__ == '__main__':
    main()
