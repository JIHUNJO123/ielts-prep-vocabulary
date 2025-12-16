#!/usr/bin/env python3
"""Band 4.5-5.5 추가 단어 (Part 4) - 대량 추가"""
import json

WORDS_PART4 = [
    # 필수 일상 동사 (200개)
    ('remove', 'verb', 'to take away', 'Remove obstacles to success.'),
    ('repeat', 'verb', 'to do again', 'Repeat the experiment.'),
    ('replace', 'verb', 'to put in place of', 'Replace old methods.'),
    ('report', 'verb', 'to give account of', 'Report findings clearly.'),
    ('represent', 'verb', 'to stand for', 'Data represents trends.'),
    ('require', 'verb', 'to need', 'Studies require funding.'),
    ('research', 'verb', 'to investigate', 'Research the topic thoroughly.'),
    ('reserve', 'verb', 'to keep back', 'Reserve judgment.'),
    ('resolve', 'verb', 'to solve', 'Resolve the issue.'),
    ('respond', 'verb', 'to answer', 'Respond to feedback.'),
    ('rest', 'verb', 'to relax', 'Let the matter rest.'),
    ('restore', 'verb', 'to bring back', 'Restore confidence.'),
    ('restrict', 'verb', 'to limit', 'Restrict access.'),
    ('result', 'verb', 'to occur as consequence', 'This results in change.'),
    ('retain', 'verb', 'to keep', 'Retain information.'),
    ('return', 'verb', 'to come back', 'Return to the topic.'),
    ('reveal', 'verb', 'to show', 'Studies reveal patterns.'),
    ('review', 'verb', 'to examine', 'Review the literature.'),
    ('rise', 'verb', 'to go up', 'Prices rise steadily.'),
    ('run', 'verb', 'to operate', 'Run the analysis.'),
    ('satisfy', 'verb', 'to meet requirements', 'Satisfy criteria.'),
    ('save', 'verb', 'to keep safe', 'Save resources.'),
    ('say', 'verb', 'to speak', 'Studies say differently.'),
    ('search', 'verb', 'to look for', 'Search for solutions.'),
    ('see', 'verb', 'to perceive', 'See the results.'),
    ('seek', 'verb', 'to look for', 'Seek answers.'),
    ('seem', 'verb', 'to appear', 'Results seem promising.'),
    ('select', 'verb', 'to choose', 'Select participants.'),
    ('sell', 'verb', 'to exchange for money', 'Sell products globally.'),
    ('send', 'verb', 'to cause to go', 'Send information.'),
    ('separate', 'verb', 'to divide', 'Separate variables.'),
    ('serve', 'verb', 'to work for', 'Serve a purpose.'),
    ('set', 'verb', 'to put', 'Set standards.'),
    ('settle', 'verb', 'to resolve', 'Settle disputes.'),
    ('shape', 'verb', 'to form', 'Shape the future.'),
    ('share', 'verb', 'to have in common', 'Share findings.'),
    ('shift', 'verb', 'to move', 'Shift focus.'),
    ('shoot', 'verb', 'to move quickly', 'Prices shoot up.'),
    ('show', 'verb', 'to display', 'Data shows trends.'),
    ('shut', 'verb', 'to close', 'Shut down operations.'),
    ('signal', 'verb', 'to indicate', 'Signal a change.'),
    ('sit', 'verb', 'to be seated', 'Sit on committees.'),
    ('solve', 'verb', 'to find answer', 'Solve problems.'),
    ('sort', 'verb', 'to arrange', 'Sort data.'),
    ('sound', 'verb', 'to seem', 'Arguments sound valid.'),
    ('speak', 'verb', 'to talk', 'Speak clearly.'),
    ('specify', 'verb', 'to state clearly', 'Specify requirements.'),
    ('spend', 'verb', 'to use up', 'Spend time wisely.'),
    ('spread', 'verb', 'to extend', 'Information spreads quickly.'),
    ('stand', 'verb', 'to be upright', 'Stand by findings.'),
    # 필수 일상 명사 (200개)
    ('section', 'noun', 'part', 'Next section covers.'),
    ('sector', 'noun', 'area of economy', 'Private sector growth.'),
    ('security', 'noun', 'safety', 'National security.'),
    ('selection', 'noun', 'choice', 'Random selection.'),
    ('sense', 'noun', 'meaning', 'In this sense.'),
    ('sentence', 'noun', 'group of words', 'Complete sentence.'),
    ('series', 'noun', 'sequence', 'Series of events.'),
    ('service', 'noun', 'helpful activity', 'Customer service.'),
    ('setting', 'noun', 'environment', 'Educational setting.'),
    ('share', 'noun', 'portion', 'Market share.'),
    ('side', 'noun', 'surface', 'Both sides argue.'),
    ('sign', 'noun', 'indication', 'Sign of progress.'),
    ('significance', 'noun', 'importance', 'Statistical significance.'),
    ('site', 'noun', 'location', 'Research site.'),
    ('situation', 'noun', 'circumstance', 'Current situation.'),
    ('size', 'noun', 'extent', 'Sample size matters.'),
    ('skill', 'noun', 'ability', 'Critical skills.'),
    ('society', 'noun', 'community', 'Modern society.'),
    ('software', 'noun', 'computer programs', 'Analysis software.'),
    ('solution', 'noun', 'answer', 'Find solutions.'),
    ('sort', 'noun', 'type', 'Sort of problem.'),
    ('sound', 'noun', 'noise', 'Sound reasoning.'),
    ('source', 'noun', 'origin', 'Primary source.'),
    ('space', 'noun', 'area', 'Office space.'),
    ('species', 'noun', 'biological group', 'Endangered species.'),
    ('speech', 'noun', 'spoken words', 'Speech patterns.'),
    ('speed', 'noun', 'rate of motion', 'Processing speed.'),
    ('staff', 'noun', 'employees', 'Staff members.'),
    ('stage', 'noun', 'phase', 'Development stage.'),
    ('standard', 'noun', 'level of quality', 'Meet standards.'),
    ('star', 'noun', 'celebrity', 'Rising star.'),
    ('start', 'noun', 'beginning', 'Good start.'),
    ('state', 'noun', 'condition', 'Current state.'),
    ('statement', 'noun', 'declaration', 'Clear statement.'),
    ('station', 'noun', 'place', 'Research station.'),
    ('status', 'noun', 'position', 'Social status.'),
    ('step', 'noun', 'measure', 'Next step.'),
    ('stock', 'noun', 'supply', 'Stock market.'),
    ('story', 'noun', 'account', 'Success story.'),
    ('strategy', 'noun', 'plan', 'Effective strategy.'),
    ('strength', 'noun', 'power', 'Key strength.'),
    ('stress', 'noun', 'pressure', 'Reduce stress.'),
    ('structure', 'noun', 'arrangement', 'Organizational structure.'),
    ('student', 'noun', 'learner', 'Student performance.'),
    ('study', 'noun', 'research', 'Recent study shows.'),
    ('style', 'noun', 'manner', 'Writing style.'),
    ('subject', 'noun', 'topic', 'Change subject.'),
    ('success', 'noun', 'achievement', 'Measure success.'),
    ('suggestion', 'noun', 'proposal', 'Helpful suggestion.'),
    ('summer', 'noun', 'warm season', 'Summer program.'),
    # 필수 형용사 (100개)
    ('strong', 'adjective', 'powerful', 'Strong evidence.'),
    ('structural', 'adjective', 'of structure', 'Structural changes.'),
    ('subsequent', 'adjective', 'following', 'Subsequent analysis.'),
    ('substantial', 'adjective', 'considerable', 'Substantial improvement.'),
    ('successful', 'adjective', 'achieving aim', 'Successful outcome.'),
    ('such', 'adjective', 'of this kind', 'Such findings.'),
    ('sudden', 'adjective', 'unexpected', 'Sudden change.'),
    ('sufficient', 'adjective', 'enough', 'Sufficient evidence.'),
    ('suitable', 'adjective', 'appropriate', 'Suitable method.'),
    ('superior', 'adjective', 'better', 'Superior results.'),
    ('sure', 'adjective', 'certain', 'Sure outcome.'),
    ('surprised', 'adjective', 'shocked', 'Surprised by results.'),
    ('surprising', 'adjective', 'unexpected', 'Surprising findings.'),
    ('sustainable', 'adjective', 'maintainable', 'Sustainable growth.'),
    ('technical', 'adjective', 'of technique', 'Technical skills.'),
    ('technological', 'adjective', 'of technology', 'Technological advance.'),
    ('temporary', 'adjective', 'not permanent', 'Temporary solution.'),
    ('theoretical', 'adjective', 'of theory', 'Theoretical framework.'),
    ('thick', 'adjective', 'not thin', 'Thick layer.'),
    ('thin', 'adjective', 'not thick', 'Thin margin.'),
    ('third', 'adjective', 'after second', 'Third factor.'),
    ('thorough', 'adjective', 'complete', 'Thorough analysis.'),
    ('tight', 'adjective', 'firm', 'Tight deadline.'),
    ('tiny', 'adjective', 'very small', 'Tiny sample.'),
    ('top', 'adjective', 'highest', 'Top priority.'),
    ('total', 'adjective', 'complete', 'Total amount.'),
    ('tough', 'adjective', 'difficult', 'Tough decision.'),
    ('traditional', 'adjective', 'conventional', 'Traditional methods.'),
    ('tremendous', 'adjective', 'very great', 'Tremendous impact.'),
    ('true', 'adjective', 'correct', 'True value.'),
    ('typical', 'adjective', 'representative', 'Typical example.'),
    ('unable', 'adjective', 'not able', 'Unable to confirm.'),
    ('uncertain', 'adjective', 'not sure', 'Uncertain outcome.'),
    ('underlying', 'adjective', 'fundamental', 'Underlying cause.'),
    ('unexpected', 'adjective', 'surprising', 'Unexpected result.'),
    ('unique', 'adjective', 'one of a kind', 'Unique approach.'),
    ('united', 'adjective', 'joined', 'United effort.'),
    ('universal', 'adjective', 'applying to all', 'Universal principle.'),
    ('unlikely', 'adjective', 'improbable', 'Unlikely outcome.'),
    ('unnecessary', 'adjective', 'not needed', 'Unnecessary detail.'),
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
    
    for i, (word, pos, definition, example) in enumerate(WORDS_PART4):
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
