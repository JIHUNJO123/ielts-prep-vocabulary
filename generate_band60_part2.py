#!/usr/bin/env python3
"""Band 6.0-6.5 추가 단어 (Part 2)"""
import json

WORDS_PART2 = [
    # 학술 동사 (150개)
    ('accommodate', 'verb', 'to provide for', 'The policy accommodates diverse needs.'),
    ('accumulate', 'verb', 'to gather over time', 'Evidence accumulates rapidly.'),
    ('acknowledge', 'verb', 'to recognize', 'Acknowledge the limitations.'),
    ('acquire', 'verb', 'to obtain', 'Acquire new skills.'),
    ('adapt', 'verb', 'to adjust', 'Adapt to changing conditions.'),
    ('administer', 'verb', 'to manage', 'Administer the program.'),
    ('advocate', 'verb', 'to support publicly', 'Advocate for change.'),
    ('affect', 'verb', 'to influence', 'Climate affects agriculture.'),
    ('aggregate', 'verb', 'to collect into whole', 'Aggregate the data.'),
    ('allocate', 'verb', 'to distribute', 'Allocate resources efficiently.'),
    ('alter', 'verb', 'to change', 'Alter the approach.'),
    ('anticipate', 'verb', 'to expect', 'Anticipate challenges.'),
    ('appreciate', 'verb', 'to value', 'Appreciate the complexity.'),
    ('approach', 'verb', 'to come near', 'Approach the problem.'),
    ('approximate', 'verb', 'to estimate', 'Approximate the value.'),
    ('assess', 'verb', 'to evaluate', 'Assess the impact.'),
    ('assign', 'verb', 'to allocate', 'Assign responsibilities.'),
    ('assume', 'verb', 'to suppose', 'Assume the hypothesis.'),
    ('attach', 'verb', 'to connect', 'Attach importance to.'),
    ('attain', 'verb', 'to achieve', 'Attain goals.'),
    ('attribute', 'verb', 'to credit to', 'Attribute success to.'),
    ('authorize', 'verb', 'to permit officially', 'Authorize the project.'),
    ('bond', 'verb', 'to unite', 'Bond with community.'),
    ('cease', 'verb', 'to stop', 'Cease operations.'),
    ('challenge', 'verb', 'to question', 'Challenge assumptions.'),
    ('channel', 'verb', 'to direct', 'Channel resources.'),
    ('cite', 'verb', 'to quote', 'Cite sources.'),
    ('clarify', 'verb', 'to make clear', 'Clarify the meaning.'),
    ('classify', 'verb', 'to categorize', 'Classify the data.'),
    ('coincide', 'verb', 'to occur together', 'Events coincide.'),
    ('collapse', 'verb', 'to fall down', 'Systems collapse.'),
    ('commence', 'verb', 'to begin', 'Commence the study.'),
    ('comment', 'verb', 'to remark', 'Comment on findings.'),
    ('commit', 'verb', 'to pledge', 'Commit to goals.'),
    ('communicate', 'verb', 'to convey', 'Communicate effectively.'),
    ('compensate', 'verb', 'to make up for', 'Compensate for losses.'),
    ('compile', 'verb', 'to gather together', 'Compile the data.'),
    ('complement', 'verb', 'to complete', 'Findings complement each other.'),
    ('comply', 'verb', 'to conform', 'Comply with regulations.'),
    ('conceive', 'verb', 'to form idea', 'Conceive new approaches.'),
    ('concentrate', 'verb', 'to focus', 'Concentrate on priorities.'),
    ('conclude', 'verb', 'to end', 'Conclude the analysis.'),
    ('conduct', 'verb', 'to carry out', 'Conduct research.'),
    ('confine', 'verb', 'to limit', 'Confine to specific areas.'),
    ('confirm', 'verb', 'to verify', 'Confirm the hypothesis.'),
    ('conform', 'verb', 'to comply', 'Conform to standards.'),
    ('consent', 'verb', 'to agree', 'Participants consent.'),
    ('constitute', 'verb', 'to make up', 'Data constitutes evidence.'),
    ('constrain', 'verb', 'to limit', 'Budgets constrain research.'),
    ('construct', 'verb', 'to build', 'Construct arguments.'),
    # 학술 명사 (200개)
    ('accuracy', 'noun', 'correctness', 'Ensure accuracy of data.'),
    ('acquisition', 'noun', 'obtaining', 'Language acquisition.'),
    ('adaptation', 'noun', 'adjustment', 'Climate adaptation strategies.'),
    ('adjustment', 'noun', 'modification', 'Require adjustment.'),
    ('administration', 'noun', 'management', 'Government administration.'),
    ('advocate', 'noun', 'supporter', 'Environmental advocate.'),
    ('aggregate', 'noun', 'total', 'In the aggregate.'),
    ('allocation', 'noun', 'distribution', 'Resource allocation.'),
    ('alternative', 'noun', 'other option', 'Consider alternatives.'),
    ('ambiguity', 'noun', 'uncertainty', 'Reduce ambiguity.'),
    ('amendment', 'noun', 'change', 'Policy amendment.'),
    ('analogy', 'noun', 'comparison', 'Draw an analogy.'),
    ('annotation', 'noun', 'note', 'Add annotations.'),
    ('appendix', 'noun', 'supplement', 'See the appendix.'),
    ('appreciation', 'noun', 'understanding', 'Appreciation of complexity.'),
    ('approximation', 'noun', 'estimate', 'Rough approximation.'),
    ('arbitrary', 'noun', 'random choice', 'Avoid arbitrary decisions.'),
    ('area', 'noun', 'region', 'Research area.'),
    ('aspect', 'noun', 'feature', 'Important aspect.'),
    ('assembly', 'noun', 'gathering', 'General assembly.'),
    ('assessment', 'noun', 'evaluation', 'Risk assessment.'),
    ('assignment', 'noun', 'task', 'Complete assignment.'),
    ('assistance', 'noun', 'help', 'Provide assistance.'),
    ('assumption', 'noun', 'supposition', 'Basic assumption.'),
    ('assurance', 'noun', 'guarantee', 'Quality assurance.'),
    ('attachment', 'noun', 'connection', 'Emotional attachment.'),
    ('attainment', 'noun', 'achievement', 'Educational attainment.'),
    ('attitude', 'noun', 'opinion', 'Positive attitude.'),
    ('attribute', 'noun', 'characteristic', 'Key attribute.'),
    ('author', 'noun', 'writer', 'The author argues.'),
    ('authority', 'noun', 'power', 'Legal authority.'),
    ('awareness', 'noun', 'knowledge', 'Raise awareness.'),
    ('behalf', 'noun', 'interest', 'On behalf of.'),
    ('benefit', 'noun', 'advantage', 'Long-term benefit.'),
    ('bias', 'noun', 'prejudice', 'Reduce bias.'),
    ('bond', 'noun', 'connection', 'Social bonds.'),
    ('bulk', 'noun', 'majority', 'The bulk of evidence.'),
    ('capacity', 'noun', 'ability', 'Production capacity.'),
    ('category', 'noun', 'class', 'Different categories.'),
    ('chapter', 'noun', 'section', 'Chapter outline.'),
    ('chart', 'noun', 'diagram', 'Bar chart shows.'),
    ('circumstance', 'noun', 'condition', 'Under circumstances.'),
    ('citation', 'noun', 'reference', 'Include citations.'),
    ('civil', 'noun', 'citizen', 'Civil rights.'),
    ('clarity', 'noun', 'clearness', 'Improve clarity.'),
    ('classic', 'noun', 'standard work', 'A classic study.'),
    ('clause', 'noun', 'provision', 'Contract clause.'),
    ('code', 'noun', 'system of rules', 'Code of conduct.'),
    ('coherence', 'noun', 'consistency', 'Logical coherence.'),
    ('colleague', 'noun', 'coworker', 'Consult colleagues.'),
    # 학술 형용사 (100개)
    ('abstract', 'adjective', 'theoretical', 'Abstract concept.'),
    ('accurate', 'adjective', 'correct', 'Accurate measurement.'),
    ('acute', 'adjective', 'severe', 'Acute problem.'),
    ('adequate', 'adjective', 'sufficient', 'Adequate evidence.'),
    ('adjacent', 'adjective', 'next to', 'Adjacent areas.'),
    ('aggregate', 'adjective', 'combined', 'Aggregate data.'),
    ('alternative', 'adjective', 'other', 'Alternative approach.'),
    ('ambiguous', 'adjective', 'unclear', 'Ambiguous results.'),
    ('analogous', 'adjective', 'similar', 'Analogous situation.'),
    ('annual', 'adjective', 'yearly', 'Annual report.'),
    ('apparent', 'adjective', 'obvious', 'Apparent contradiction.'),
    ('appropriate', 'adjective', 'suitable', 'Appropriate method.'),
    ('arbitrary', 'adjective', 'random', 'Arbitrary selection.'),
    ('automatic', 'adjective', 'self-operating', 'Automatic process.'),
    ('beneficial', 'adjective', 'helpful', 'Mutually beneficial.'),
    ('brief', 'adjective', 'short', 'Brief summary.'),
    ('capable', 'adjective', 'able', 'Capable of change.'),
    ('classic', 'adjective', 'typical', 'Classic example.'),
    ('coherent', 'adjective', 'logical', 'Coherent argument.'),
    ('compatible', 'adjective', 'able to exist together', 'Compatible systems.'),
    ('comprehensive', 'adjective', 'thorough', 'Comprehensive study.'),
    ('concurrent', 'adjective', 'simultaneous', 'Concurrent events.'),
    ('considerable', 'adjective', 'significant', 'Considerable impact.'),
    ('consistent', 'adjective', 'unchanging', 'Consistent results.'),
    ('constant', 'adjective', 'continuous', 'Constant rate.'),
    ('contemporary', 'adjective', 'modern', 'Contemporary research.'),
    ('contextual', 'adjective', 'related to context', 'Contextual factors.'),
    ('contrary', 'adjective', 'opposite', 'Contrary evidence.'),
    ('conventional', 'adjective', 'traditional', 'Conventional methods.'),
    ('core', 'adjective', 'central', 'Core concept.'),
    ('corporate', 'adjective', 'of business', 'Corporate responsibility.'),
    ('corresponding', 'adjective', 'matching', 'Corresponding values.'),
    ('crucial', 'adjective', 'critical', 'Crucial factor.'),
    ('cumulative', 'adjective', 'increasing', 'Cumulative effect.'),
    ('definite', 'adjective', 'certain', 'Definite conclusion.'),
    ('discrete', 'adjective', 'separate', 'Discrete categories.'),
    ('distinct', 'adjective', 'different', 'Distinct features.'),
    ('diverse', 'adjective', 'varied', 'Diverse population.'),
    ('dominant', 'adjective', 'main', 'Dominant factor.'),
    ('dynamic', 'adjective', 'changing', 'Dynamic process.'),
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
    
    for i, (word, pos, definition, example) in enumerate(WORDS_PART2):
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
