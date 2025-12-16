#!/usr/bin/env python3
"""Band 6.0-6.5 추가 단어 (Part 3) - 대량 추가"""
import json

WORDS_PART3 = [
    # 중급 학술 동사 (200개)
    ('consult', 'verb', 'to seek advice', 'Consult with experts.'),
    ('consume', 'verb', 'to use up', 'Resources are consumed rapidly.'),
    ('contact', 'verb', 'to communicate with', 'Contact participants.'),
    ('contain', 'verb', 'to include', 'The report contains data.'),
    ('contemplate', 'verb', 'to consider', 'Contemplate alternatives.'),
    ('contest', 'verb', 'to challenge', 'Contest the findings.'),
    ('continue', 'verb', 'to carry on', 'Continue the research.'),
    ('contract', 'verb', 'to make smaller', 'Markets contract.'),
    ('contradict', 'verb', 'to deny', 'Results contradict assumptions.'),
    ('contrast', 'verb', 'to compare differences', 'Contrast the approaches.'),
    ('contribute', 'verb', 'to give', 'Contribute to knowledge.'),
    ('control', 'verb', 'to regulate', 'Control variables.'),
    ('convert', 'verb', 'to change', 'Convert data formats.'),
    ('convey', 'verb', 'to communicate', 'Convey meaning clearly.'),
    ('convince', 'verb', 'to persuade', 'Convince the audience.'),
    ('cooperate', 'verb', 'to work together', 'Cooperate with teams.'),
    ('coordinate', 'verb', 'to organize', 'Coordinate efforts.'),
    ('cope', 'verb', 'to deal with', 'Cope with challenges.'),
    ('copy', 'verb', 'to duplicate', 'Copy the method.'),
    ('correct', 'verb', 'to make right', 'Correct errors.'),
    ('correlate', 'verb', 'to show connection', 'Variables correlate.'),
    ('correspond', 'verb', 'to match', 'Results correspond.'),
    ('cost', 'verb', 'to require payment', 'Errors cost time.'),
    ('count', 'verb', 'to calculate', 'Count occurrences.'),
    ('couple', 'verb', 'to join', 'Couple with analysis.'),
    ('cover', 'verb', 'to include', 'Cover all topics.'),
    ('crash', 'verb', 'to collapse', 'Markets crash.'),
    ('create', 'verb', 'to make', 'Create opportunities.'),
    ('credit', 'verb', 'to acknowledge', 'Credit the source.'),
    ('criticize', 'verb', 'to evaluate negatively', 'Criticize methodology.'),
    ('cultivate', 'verb', 'to develop', 'Cultivate skills.'),
    ('damage', 'verb', 'to harm', 'Damage reputation.'),
    ('date', 'verb', 'to assign time', 'Date the findings.'),
    ('deal', 'verb', 'to handle', 'Deal with issues.'),
    ('debate', 'verb', 'to discuss', 'Debate the topic.'),
    ('decide', 'verb', 'to make choice', 'Decide on approach.'),
    ('declare', 'verb', 'to announce', 'Declare results.'),
    ('decline', 'verb', 'to decrease', 'Numbers decline.'),
    ('dedicate', 'verb', 'to commit', 'Dedicate resources.'),
    ('deduce', 'verb', 'to conclude', 'Deduce from evidence.'),
    ('deem', 'verb', 'to consider', 'Deem appropriate.'),
    ('defeat', 'verb', 'to overcome', 'Defeat challenges.'),
    ('defend', 'verb', 'to protect', 'Defend the thesis.'),
    ('defer', 'verb', 'to postpone', 'Defer judgment.'),
    ('define', 'verb', 'to explain meaning', 'Define key terms.'),
    ('delay', 'verb', 'to postpone', 'Delay implementation.'),
    ('delegate', 'verb', 'to assign', 'Delegate tasks.'),
    ('delete', 'verb', 'to remove', 'Delete irrelevant data.'),
    ('deliver', 'verb', 'to provide', 'Deliver results.'),
    ('demand', 'verb', 'to require', 'Situations demand action.'),
    # 중급 학술 명사 (200개)
    ('collaboration', 'noun', 'working together', 'Academic collaboration.'),
    ('collection', 'noun', 'gathering', 'Data collection.'),
    ('combination', 'noun', 'mixture', 'Combination of factors.'),
    ('comment', 'noun', 'remark', 'Critical comment.'),
    ('commission', 'noun', 'group given task', 'Research commission.'),
    ('commitment', 'noun', 'dedication', 'Strong commitment.'),
    ('commodity', 'noun', 'product', 'Valuable commodity.'),
    ('communication', 'noun', 'exchange of information', 'Clear communication.'),
    ('community', 'noun', 'group of people', 'Scientific community.'),
    ('comparison', 'noun', 'evaluation', 'Make comparisons.'),
    ('compensation', 'noun', 'payment', 'Fair compensation.'),
    ('competition', 'noun', 'rivalry', 'Market competition.'),
    ('complaint', 'noun', 'expression of dissatisfaction', 'Common complaint.'),
    ('complexity', 'noun', 'complication', 'Increased complexity.'),
    ('compliance', 'noun', 'conformity', 'Regulatory compliance.'),
    ('component', 'noun', 'part', 'Key component.'),
    ('composition', 'noun', 'makeup', 'Chemical composition.'),
    ('compromise', 'noun', 'agreement', 'Reach compromise.'),
    ('computation', 'noun', 'calculation', 'Complex computation.'),
    ('concentration', 'noun', 'focus', 'High concentration.'),
    ('concept', 'noun', 'idea', 'Abstract concept.'),
    ('concern', 'noun', 'worry', 'Main concern.'),
    ('conclusion', 'noun', 'end result', 'Draw conclusions.'),
    ('condition', 'noun', 'state', 'Under conditions.'),
    ('conference', 'noun', 'meeting', 'Academic conference.'),
    ('confidence', 'noun', 'certainty', 'High confidence.'),
    ('configuration', 'noun', 'arrangement', 'System configuration.'),
    ('confirmation', 'noun', 'verification', 'Seek confirmation.'),
    ('conflict', 'noun', 'disagreement', 'Resolve conflict.'),
    ('confusion', 'noun', 'bewilderment', 'Avoid confusion.'),
    ('connection', 'noun', 'link', 'Make connections.'),
    ('consciousness', 'noun', 'awareness', 'Raise consciousness.'),
    ('consensus', 'noun', 'agreement', 'Reach consensus.'),
    ('consent', 'noun', 'permission', 'Informed consent.'),
    ('consequence', 'noun', 'result', 'Face consequences.'),
    ('conservation', 'noun', 'preservation', 'Environmental conservation.'),
    ('consideration', 'noun', 'thought', 'Careful consideration.'),
    ('consistency', 'noun', 'uniformity', 'Maintain consistency.'),
    ('consolidation', 'noun', 'strengthening', 'Market consolidation.'),
    ('constant', 'noun', 'fixed value', 'Mathematical constant.'),
    ('constitution', 'noun', 'fundamental law', 'National constitution.'),
    ('constraint', 'noun', 'limitation', 'Budget constraints.'),
    ('construction', 'noun', 'building', 'Theory construction.'),
    ('consultation', 'noun', 'discussion', 'Expert consultation.'),
    ('consumer', 'noun', 'buyer', 'Consumer behavior.'),
    ('consumption', 'noun', 'use', 'Energy consumption.'),
    ('contact', 'noun', 'connection', 'Make contact.'),
    ('container', 'noun', 'receptacle', 'Data container.'),
    ('content', 'noun', 'material', 'Content analysis.'),
    ('context', 'noun', 'circumstances', 'Historical context.'),
    # 중급 형용사 (100개)
    ('economic', 'adjective', 'of economy', 'Economic impact.'),
    ('editorial', 'adjective', 'of editing', 'Editorial decision.'),
    ('educational', 'adjective', 'of education', 'Educational reform.'),
    ('effective', 'adjective', 'producing result', 'Effective solution.'),
    ('efficient', 'adjective', 'working well', 'Efficient process.'),
    ('elaborate', 'adjective', 'detailed', 'Elaborate explanation.'),
    ('electronic', 'adjective', 'of electronics', 'Electronic data.'),
    ('elementary', 'adjective', 'basic', 'Elementary level.'),
    ('eligible', 'adjective', 'qualified', 'Eligible participants.'),
    ('emerging', 'adjective', 'developing', 'Emerging trends.'),
    ('emotional', 'adjective', 'of feelings', 'Emotional response.'),
    ('empirical', 'adjective', 'based on observation', 'Empirical evidence.'),
    ('empty', 'adjective', 'containing nothing', 'Empty rhetoric.'),
    ('enabling', 'adjective', 'making possible', 'Enabling factor.'),
    ('endless', 'adjective', 'infinite', 'Endless possibilities.'),
    ('enormous', 'adjective', 'huge', 'Enormous impact.'),
    ('entire', 'adjective', 'whole', 'Entire population.'),
    ('environmental', 'adjective', 'of environment', 'Environmental impact.'),
    ('equal', 'adjective', 'same', 'Equal opportunity.'),
    ('equivalent', 'adjective', 'equal in value', 'Equivalent results.'),
    ('essential', 'adjective', 'necessary', 'Essential component.'),
    ('established', 'adjective', 'accepted', 'Established practice.'),
    ('ethical', 'adjective', 'moral', 'Ethical considerations.'),
    ('ethnic', 'adjective', 'of race', 'Ethnic diversity.'),
    ('eventual', 'adjective', 'final', 'Eventual outcome.'),
    ('evident', 'adjective', 'obvious', 'Evident from data.'),
    ('evolutionary', 'adjective', 'of evolution', 'Evolutionary process.'),
    ('exact', 'adjective', 'precise', 'Exact measurement.'),
    ('excellent', 'adjective', 'very good', 'Excellent results.'),
    ('exceptional', 'adjective', 'unusual', 'Exceptional case.'),
    ('excessive', 'adjective', 'too much', 'Excessive use.'),
    ('exclusive', 'adjective', 'sole', 'Exclusive rights.'),
    ('executive', 'adjective', 'managerial', 'Executive decision.'),
    ('exhaustive', 'adjective', 'thorough', 'Exhaustive analysis.'),
    ('existing', 'adjective', 'current', 'Existing research.'),
    ('experimental', 'adjective', 'of experiment', 'Experimental design.'),
    ('expert', 'adjective', 'skilled', 'Expert opinion.'),
    ('explicit', 'adjective', 'clear', 'Explicit statement.'),
    ('extensive', 'adjective', 'wide', 'Extensive research.'),
    ('external', 'adjective', 'outside', 'External factors.'),
]

CATEGORIES = ['Academic', 'Research', 'Science', 'Analysis', 'Writing', 
              'Critical Thinking', 'Education', 'Professional', 'Data', 'Theory']

def main():
    try:
        with open('assets/data/band60_words.json', 'r', encoding='utf-8') as f:
            existing = json.load(f)
    except:
        existing = []
    
    existing_words = {w['word'] for w in existing}
    start_id = len(existing) + 1
    added = 0
    
    for i, (word, pos, definition, example) in enumerate(WORDS_PART3):
        if word not in existing_words:
            existing.append({
                'id': start_id + added,
                'word': word,
                'level': 'Band 6.0-6.5',
                'partOfSpeech': pos,
                'definition': definition,
                'example': example,
                'category': CATEGORIES[(start_id + added) % len(CATEGORIES)]
            })
            existing_words.add(word)
            added += 1
    
    with open('assets/data/band60_words.json', 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f'✅ Band 6.0-6.5 업데이트: {len(existing)}개 (추가: {added}개)')

if __name__ == '__main__':
    main()
