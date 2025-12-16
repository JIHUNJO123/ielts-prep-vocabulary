#!/usr/bin/env python3
"""Band 4.5-5.5 추가 단어 (Part 3)"""
import json

WORDS_PART3 = [
    # 더 많은 동사 (150개)
    ('occur', 'verb', 'to happen', 'Changes occur naturally.'),
    ('offer', 'verb', 'to present for acceptance', 'Offer solutions.'),
    ('open', 'verb', 'to make accessible', 'Open new possibilities.'),
    ('operate', 'verb', 'to function', 'Systems operate efficiently.'),
    ('organize', 'verb', 'to arrange', 'Organize the data.'),
    ('own', 'verb', 'to possess', 'Own a business.'),
    ('participate', 'verb', 'to take part', 'Participate in discussions.'),
    ('pass', 'verb', 'to move by', 'Pass the exam.'),
    ('pay', 'verb', 'to give money', 'Pay attention.'),
    ('perform', 'verb', 'to carry out', 'Perform well.'),
    ('permit', 'verb', 'to allow', 'Permit access.'),
    ('pick', 'verb', 'to choose', 'Pick the best option.'),
    ('plan', 'verb', 'to arrange', 'Plan carefully.'),
    ('play', 'verb', 'to engage in', 'Play a role.'),
    ('please', 'verb', 'to make happy', 'Please the audience.'),
    ('point', 'verb', 'to indicate', 'Point to evidence.'),
    ('possess', 'verb', 'to own', 'Possess skills.'),
    ('practice', 'verb', 'to perform repeatedly', 'Practice regularly.'),
    ('prepare', 'verb', 'to make ready', 'Prepare for exams.'),
    ('present', 'verb', 'to show', 'Present the findings.'),
    ('preserve', 'verb', 'to maintain', 'Preserve the environment.'),
    ('prevent', 'verb', 'to stop', 'Prevent problems.'),
    ('produce', 'verb', 'to make', 'Produce results.'),
    ('promise', 'verb', 'to assure', 'Promise improvement.'),
    ('promote', 'verb', 'to advance', 'Promote education.'),
    ('propose', 'verb', 'to suggest', 'Propose a solution.'),
    ('protect', 'verb', 'to keep safe', 'Protect the environment.'),
    ('prove', 'verb', 'to demonstrate', 'Prove the theory.'),
    ('provide', 'verb', 'to supply', 'Provide support.'),
    ('publish', 'verb', 'to issue', 'Publish research.'),
    ('pull', 'verb', 'to draw toward', 'Pull together resources.'),
    ('push', 'verb', 'to press forward', 'Push for change.'),
    ('put', 'verb', 'to place', 'Put into practice.'),
    ('raise', 'verb', 'to lift up', 'Raise awareness.'),
    ('reach', 'verb', 'to arrive at', 'Reach a conclusion.'),
    ('read', 'verb', 'to interpret written', 'Read the data.'),
    ('realize', 'verb', 'to become aware', 'Realize the potential.'),
    ('receive', 'verb', 'to get', 'Receive feedback.'),
    ('recognize', 'verb', 'to identify', 'Recognize patterns.'),
    ('recommend', 'verb', 'to suggest', 'Recommend changes.'),
    ('record', 'verb', 'to document', 'Record observations.'),
    ('reduce', 'verb', 'to decrease', 'Reduce costs.'),
    ('refer', 'verb', 'to mention', 'Refer to the chart.'),
    ('reflect', 'verb', 'to think about', 'Reflect on progress.'),
    ('regard', 'verb', 'to consider', 'Regard as important.'),
    ('relate', 'verb', 'to connect', 'Relate to the topic.'),
    ('release', 'verb', 'to let go', 'Release information.'),
    ('rely', 'verb', 'to depend on', 'Rely on data.'),
    ('remain', 'verb', 'to stay', 'Remain committed.'),
    ('remember', 'verb', 'to recall', 'Remember key points.'),
    # 더 많은 명사 (150개)
    ('population', 'noun', 'number of people', 'Population growth continues.'),
    ('position', 'noun', 'location', 'Take a position.'),
    ('possibility', 'noun', 'chance', 'Consider possibilities.'),
    ('potential', 'noun', 'capability', 'Unlock potential.'),
    ('power', 'noun', 'ability to act', 'Power of education.'),
    ('practice', 'noun', 'habitual action', 'Best practices apply.'),
    ('pressure', 'noun', 'stress', 'Social pressure affects.'),
    ('price', 'noun', 'cost', 'Price increases impact.'),
    ('principle', 'noun', 'basic truth', 'Guiding principles.'),
    ('problem', 'noun', 'difficulty', 'Solve problems.'),
    ('process', 'noun', 'series of actions', 'Decision process.'),
    ('product', 'noun', 'item made', 'Quality products.'),
    ('production', 'noun', 'making of goods', 'Production increases.'),
    ('professor', 'noun', 'university teacher', 'Professor explains.'),
    ('program', 'noun', 'plan of action', 'Education program.'),
    ('progress', 'noun', 'forward movement', 'Track progress.'),
    ('project', 'noun', 'planned undertaking', 'Research project.'),
    ('property', 'noun', 'possession', 'Property rights.'),
    ('protection', 'noun', 'keeping safe', 'Environmental protection.'),
    ('public', 'noun', 'general population', 'Inform the public.'),
    ('purpose', 'noun', 'reason for', 'Serve a purpose.'),
    ('quality', 'noun', 'degree of excellence', 'Quality matters.'),
    ('question', 'noun', 'query', 'Answer the question.'),
    ('range', 'noun', 'extent', 'Wide range of topics.'),
    ('rate', 'noun', 'measure', 'Growth rate increases.'),
    ('reaction', 'noun', 'response', 'Initial reaction.'),
    ('reader', 'noun', 'one who reads', 'Reader understands.'),
    ('reality', 'noun', 'actual existence', 'Face reality.'),
    ('reason', 'noun', 'cause', 'Good reason to believe.'),
    ('record', 'noun', 'document', 'Keep records.'),
    ('reference', 'noun', 'mention', 'Make reference to.'),
    ('region', 'noun', 'area', 'Different regions.'),
    ('relation', 'noun', 'connection', 'Relation between factors.'),
    ('relationship', 'noun', 'connection', 'Build relationships.'),
    ('report', 'noun', 'account', 'Annual report.'),
    ('research', 'noun', 'investigation', 'Conduct research.'),
    ('resource', 'noun', 'supply', 'Natural resources.'),
    ('response', 'noun', 'answer', 'Positive response.'),
    ('responsibility', 'noun', 'duty', 'Take responsibility.'),
    ('rest', 'noun', 'remainder', 'The rest of the data.'),
    ('result', 'noun', 'outcome', 'Results show.'),
    ('return', 'noun', 'coming back', 'Return on investment.'),
    ('right', 'noun', 'entitlement', 'Human rights.'),
    ('risk', 'noun', 'danger', 'Reduce risk.'),
    ('role', 'noun', 'function', 'Play a key role.'),
    ('room', 'noun', 'space', 'Room for improvement.'),
    ('rule', 'noun', 'regulation', 'Follow rules.'),
    ('sale', 'noun', 'selling', 'Increase sales.'),
    ('school', 'noun', 'educational institution', 'School performance.'),
    ('science', 'noun', 'systematic study', 'Science advances.'),
    # 더 많은 형용사 (100개)
    ('safe', 'adjective', 'not dangerous', 'Safe environment.'),
    ('same', 'adjective', 'identical', 'Same result.'),
    ('scientific', 'adjective', 'of science', 'Scientific method.'),
    ('secondary', 'adjective', 'second in rank', 'Secondary importance.'),
    ('secure', 'adjective', 'safe', 'Secure system.'),
    ('senior', 'adjective', 'higher in rank', 'Senior management.'),
    ('separate', 'adjective', 'distinct', 'Separate issues.'),
    ('serious', 'adjective', 'important', 'Serious concern.'),
    ('severe', 'adjective', 'harsh', 'Severe consequences.'),
    ('short', 'adjective', 'brief', 'Short term.'),
    ('significant', 'adjective', 'important', 'Significant change.'),
    ('similar', 'adjective', 'alike', 'Similar results.'),
    ('simple', 'adjective', 'easy', 'Simple solution.'),
    ('single', 'adjective', 'one only', 'Single cause.'),
    ('slight', 'adjective', 'small', 'Slight increase.'),
    ('slow', 'adjective', 'not fast', 'Slow progress.'),
    ('small', 'adjective', 'little', 'Small sample.'),
    ('smooth', 'adjective', 'even', 'Smooth transition.'),
    ('social', 'adjective', 'of society', 'Social impact.'),
    ('soft', 'adjective', 'not hard', 'Soft skills.'),
    ('solid', 'adjective', 'firm', 'Solid foundation.'),
    ('sorry', 'adjective', 'feeling regret', 'Sorry state of affairs.'),
    ('sound', 'adjective', 'reliable', 'Sound reasoning.'),
    ('special', 'adjective', 'particular', 'Special attention.'),
    ('specific', 'adjective', 'particular', 'Specific examples.'),
    ('standard', 'adjective', 'usual', 'Standard procedure.'),
    ('steady', 'adjective', 'constant', 'Steady growth.'),
    ('still', 'adjective', 'not moving', 'Still relevant.'),
    ('straight', 'adjective', 'direct', 'Straight answer.'),
    ('strange', 'adjective', 'unusual', 'Strange phenomenon.'),
]

CATEGORIES = ['Academic', 'Environment', 'Technology', 'Health', 'Education',
              'Business', 'Society', 'Science', 'Culture', 'Media']

def main():
    try:
        with open('assets/data/band45_words.json', 'r', encoding='utf-8') as f:
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
                'level': 'Band 4.5-5.5',
                'partOfSpeech': pos,
                'definition': definition,
                'example': example,
                'category': CATEGORIES[(start_id + added) % len(CATEGORIES)]
            })
            existing_words.add(word)
            added += 1
    
    with open('assets/data/band45_words.json', 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f'✅ Band 4.5-5.5 업데이트: {len(existing)}개 (추가: {added}개)')

if __name__ == '__main__':
    main()
