#!/usr/bin/env python3
"""IELTS 5000개 목표 - 최종 대량 생성"""
import json
import os

# Band 4.5-5.5: 목표 1,200개 (현재 ~1,100개, 100개 추가 필요)
FINAL_BAND45 = [
    # 추가 필수 단어
    ('amount', 'verb', 'to total', 'Costs amount to millions.'),
    ('amuse', 'verb', 'to entertain', 'Data amuses researchers.'),
    ('analyze', 'verb', 'to examine', 'Analyze the results.'),
    ('announce', 'verb', 'to declare', 'Announce findings.'),
    ('annoy', 'verb', 'to irritate', 'Errors annoy.'),
    ('anticipate', 'verb', 'to expect', 'Anticipate problems.'),
    ('apologize', 'verb', 'to express regret', 'Apologize for error.'),
    ('appeal', 'verb', 'to attract', 'Results appeal.'),
    ('appear', 'verb', 'to seem', 'Appear significant.'),
    ('applaud', 'verb', 'to praise', 'Applaud efforts.'),
    ('apply', 'verb', 'to use', 'Apply methods.'),
    ('appoint', 'verb', 'to assign', 'Appoint committee.'),
    ('appreciate', 'verb', 'to value', 'Appreciate support.'),
    ('approve', 'verb', 'to accept', 'Approve proposal.'),
    ('argue', 'verb', 'to debate', 'Argue for change.'),
    ('arise', 'verb', 'to occur', 'Problems arise.'),
    ('arrange', 'verb', 'to organize', 'Arrange meeting.'),
    ('arrest', 'verb', 'to stop', 'Arrest decline.'),
    ('arrive', 'verb', 'to reach', 'Arrive at conclusion.'),
    ('articulate', 'verb', 'to express', 'Articulate clearly.'),
    # 추가 명사
    ('accomplishment', 'noun', 'achievement', 'Major accomplishment.'),
    ('accordance', 'noun', 'agreement', 'In accordance with.'),
    ('accountability', 'noun', 'responsibility', 'Ensure accountability.'),
    ('accumulation', 'noun', 'collection', 'Data accumulation.'),
    ('achievement', 'noun', 'success', 'Major achievement.'),
    ('acknowledgement', 'noun', 'recognition', 'Acknowledgement of.'),
    ('acquisition', 'noun', 'obtaining', 'Data acquisition.'),
    ('activation', 'noun', 'starting', 'Process activation.'),
    ('adaptation', 'noun', 'adjustment', 'Climate adaptation.'),
    ('addition', 'noun', 'extra', 'In addition to.'),
    ('adjustment', 'noun', 'modification', 'Minor adjustment.'),
    ('administration', 'noun', 'management', 'Public administration.'),
    ('admission', 'noun', 'entrance', 'University admission.'),
    ('adoption', 'noun', 'acceptance', 'Policy adoption.'),
    ('advancement', 'noun', 'progress', 'Career advancement.'),
    ('advantage', 'noun', 'benefit', 'Competitive advantage.'),
    ('adventure', 'noun', 'exciting experience', 'Research adventure.'),
    ('advertisement', 'noun', 'promotion', 'Job advertisement.'),
    ('advice', 'noun', 'recommendation', 'Expert advice.'),
    ('affair', 'noun', 'matter', 'Current affairs.'),
    # 추가 형용사
    ('calm', 'adjective', 'peaceful', 'Calm approach.'),
    ('capable', 'adjective', 'able', 'Capable researcher.'),
    ('capital', 'adjective', 'main', 'Capital importance.'),
    ('careful', 'adjective', 'cautious', 'Careful analysis.'),
    ('casual', 'adjective', 'informal', 'Casual observation.'),
    ('central', 'adjective', 'main', 'Central theme.'),
    ('certain', 'adjective', 'sure', 'Certain outcome.'),
    ('challenging', 'adjective', 'difficult', 'Challenging task.'),
    ('cheap', 'adjective', 'inexpensive', 'Cheap solution.'),
    ('chief', 'adjective', 'main', 'Chief concern.'),
    ('civil', 'adjective', 'of citizens', 'Civil rights.'),
    ('classic', 'adjective', 'traditional', 'Classic example.'),
    ('clean', 'adjective', 'pure', 'Clean data.'),
    ('clear', 'adjective', 'obvious', 'Clear evidence.'),
    ('clever', 'adjective', 'intelligent', 'Clever solution.'),
    ('clinical', 'adjective', 'medical', 'Clinical trial.'),
    ('close', 'adjective', 'near', 'Close relationship.'),
    ('closed', 'adjective', 'not open', 'Closed system.'),
    ('coastal', 'adjective', 'near coast', 'Coastal regions.'),
    ('cognitive', 'adjective', 'of thinking', 'Cognitive development.'),
]

# Band 6.0-6.5: 목표 1,800개 (현재 ~500개, 1,300개 추가 필요) - 대량 추가
FINAL_BAND60 = [
    # 대량 학술 동사
    ('excel', 'verb', 'to surpass', 'Excel in research.'),
    ('exchange', 'verb', 'to trade', 'Exchange ideas.'),
    ('excite', 'verb', 'to stimulate', 'Findings excite.'),
    ('exclude', 'verb', 'to leave out', 'Exclude outliers.'),
    ('excuse', 'verb', 'to forgive', 'Excuse errors.'),
    ('execute', 'verb', 'to carry out', 'Execute plan.'),
    ('exemplify', 'verb', 'to illustrate', 'Exemplify concept.'),
    ('exempt', 'verb', 'to free from', 'Exempt from rules.'),
    ('exercise', 'verb', 'to use', 'Exercise caution.'),
    ('exhaust', 'verb', 'to use up', 'Exhaust options.'),
    ('exhibit', 'verb', 'to show', 'Exhibit patterns.'),
    ('exist', 'verb', 'to be', 'Problems exist.'),
    ('expand', 'verb', 'to grow', 'Expand scope.'),
    ('expect', 'verb', 'to anticipate', 'Expect results.'),
    ('expedite', 'verb', 'to speed up', 'Expedite process.'),
    ('expel', 'verb', 'to force out', 'Expel members.'),
    ('experience', 'verb', 'to undergo', 'Experience change.'),
    ('experiment', 'verb', 'to test', 'Experiment with methods.'),
    ('explain', 'verb', 'to clarify', 'Explain findings.'),
    ('explode', 'verb', 'to burst', 'Theory explodes.'),
    ('exploit', 'verb', 'to use', 'Exploit resources.'),
    ('explore', 'verb', 'to investigate', 'Explore options.'),
    ('export', 'verb', 'to send abroad', 'Export goods.'),
    ('expose', 'verb', 'to reveal', 'Expose flaws.'),
    ('express', 'verb', 'to state', 'Express concern.'),
    ('extend', 'verb', 'to lengthen', 'Extend deadline.'),
    ('extract', 'verb', 'to remove', 'Extract data.'),
    ('extrapolate', 'verb', 'to infer', 'Extrapolate trends.'),
    ('fabricate', 'verb', 'to make up', 'Fabricate data.'),
    ('face', 'verb', 'to confront', 'Face challenges.'),
    # 대량 학술 명사
    ('deficit', 'noun', 'shortage', 'Budget deficit.'),
    ('definition', 'noun', 'meaning', 'Clear definition.'),
    ('degree', 'noun', 'level', 'High degree.'),
    ('delay', 'noun', 'postponement', 'Long delay.'),
    ('delegation', 'noun', 'group', 'Official delegation.'),
    ('deliberation', 'noun', 'consideration', 'Careful deliberation.'),
    ('delivery', 'noun', 'provision', 'Service delivery.'),
    ('demand', 'noun', 'requirement', 'High demand.'),
    ('democracy', 'noun', 'government type', 'Liberal democracy.'),
    ('demonstration', 'noun', 'showing', 'Clear demonstration.'),
    ('denial', 'noun', 'refusal', 'In denial.'),
    ('density', 'noun', 'compactness', 'Population density.'),
    ('departure', 'noun', 'leaving', 'Major departure.'),
    ('dependence', 'noun', 'reliance', 'Economic dependence.'),
    ('deployment', 'noun', 'use', 'Resource deployment.'),
    ('depression', 'noun', 'downturn', 'Economic depression.'),
    ('deprivation', 'noun', 'lack', 'Sleep deprivation.'),
    ('depth', 'noun', 'deepness', 'In depth.'),
    ('deputy', 'noun', 'assistant', 'Deputy director.'),
    ('derivation', 'noun', 'origin', 'Word derivation.'),
    # 대량 형용사
    ('fuzzy', 'adjective', 'unclear', 'Fuzzy boundaries.'),
    ('general', 'adjective', 'overall', 'General trend.'),
    ('generous', 'adjective', 'giving', 'Generous funding.'),
    ('genetic', 'adjective', 'hereditary', 'Genetic factors.'),
    ('genuine', 'adjective', 'real', 'Genuine concern.'),
    ('geographic', 'adjective', 'of geography', 'Geographic distribution.'),
    ('geological', 'adjective', 'of geology', 'Geological survey.'),
    ('giant', 'adjective', 'huge', 'Giant leap.'),
    ('given', 'adjective', 'specified', 'Given conditions.'),
    ('glad', 'adjective', 'happy', 'Glad to report.'),
    ('global', 'adjective', 'worldwide', 'Global impact.'),
    ('golden', 'adjective', 'excellent', 'Golden opportunity.'),
    ('good', 'adjective', 'positive', 'Good results.'),
    ('governmental', 'adjective', 'of government', 'Governmental policy.'),
    ('gradual', 'adjective', 'slow', 'Gradual change.'),
    ('grand', 'adjective', 'impressive', 'Grand theory.'),
    ('graphic', 'adjective', 'visual', 'Graphic representation.'),
    ('grateful', 'adjective', 'thankful', 'Grateful for support.'),
    ('grave', 'adjective', 'serious', 'Grave concern.'),
    ('great', 'adjective', 'large', 'Great impact.'),
]

# Band 7.0-7.5: 목표 1,200개 (현재 ~350개, 850개 추가 필요)
FINAL_BAND70 = [
    # 고급 동사
    ('converse', 'verb', 'to talk', 'Converse with experts.'),
    ('convert', 'verb', 'to change', 'Convert data format.'),
    ('convey', 'verb', 'to communicate', 'Convey meaning.'),
    ('convince', 'verb', 'to persuade', 'Convince audience.'),
    ('cooperate', 'verb', 'to work together', 'Cooperate on project.'),
    ('coordinate', 'verb', 'to organize', 'Coordinate efforts.'),
    ('cope', 'verb', 'to deal with', 'Cope with challenges.'),
    ('copy', 'verb', 'to duplicate', 'Copy method.'),
    ('correct', 'verb', 'to fix', 'Correct errors.'),
    ('correlate', 'verb', 'to connect', 'Variables correlate.'),
    ('correspond', 'verb', 'to match', 'Results correspond.'),
    ('corroborate', 'verb', 'to confirm', 'Corroborate findings.'),
    ('corrupt', 'verb', 'to damage', 'Corrupt data.'),
    ('cost', 'verb', 'to require payment', 'Errors cost time.'),
    ('counsel', 'verb', 'to advise', 'Counsel participants.'),
    ('count', 'verb', 'to calculate', 'Count occurrences.'),
    ('counter', 'verb', 'to oppose', 'Counter argument.'),
    ('couple', 'verb', 'to join', 'Couple with analysis.'),
    ('cover', 'verb', 'to include', 'Cover all aspects.'),
    ('craft', 'verb', 'to make', 'Craft argument.'),
    # 고급 명사
    ('competence', 'noun', 'ability', 'Professional competence.'),
    ('competition', 'noun', 'rivalry', 'Fierce competition.'),
    ('compilation', 'noun', 'collection', 'Data compilation.'),
    ('complaint', 'noun', 'grievance', 'File complaint.'),
    ('complement', 'noun', 'addition', 'Perfect complement.'),
    ('completion', 'noun', 'finishing', 'Project completion.'),
    ('complexity', 'noun', 'complication', 'Increased complexity.'),
    ('compliance', 'noun', 'conformity', 'Regulatory compliance.'),
    ('complication', 'noun', 'difficulty', 'Unexpected complication.'),
    ('compliment', 'noun', 'praise', 'Pay compliment.'),
    ('component', 'noun', 'part', 'Key component.'),
    ('composition', 'noun', 'makeup', 'Chemical composition.'),
    ('compound', 'noun', 'mixture', 'Chemical compound.'),
    ('comprehension', 'noun', 'understanding', 'Reading comprehension.'),
    ('compromise', 'noun', 'agreement', 'Reach compromise.'),
    ('compulsion', 'noun', 'urge', 'Strong compulsion.'),
    ('computation', 'noun', 'calculation', 'Complex computation.'),
    ('concealment', 'noun', 'hiding', 'Data concealment.'),
    ('concentration', 'noun', 'focus', 'High concentration.'),
    ('conception', 'noun', 'idea', 'Original conception.'),
    # 고급 형용사
    ('comparable', 'adjective', 'similar', 'Comparable results.'),
    ('comparative', 'adjective', 'relative', 'Comparative study.'),
    ('compatible', 'adjective', 'consistent', 'Compatible systems.'),
    ('compelling', 'adjective', 'convincing', 'Compelling evidence.'),
    ('compensatory', 'adjective', 'making up for', 'Compensatory measures.'),
    ('competent', 'adjective', 'capable', 'Competent researcher.'),
    ('competitive', 'adjective', 'rivalry-based', 'Competitive advantage.'),
    ('complementary', 'adjective', 'completing', 'Complementary approach.'),
    ('complete', 'adjective', 'whole', 'Complete analysis.'),
    ('complex', 'adjective', 'complicated', 'Complex problem.'),
    ('compliant', 'adjective', 'conforming', 'Compliant behavior.'),
    ('complimentary', 'adjective', 'praising', 'Complimentary review.'),
    ('composite', 'adjective', 'combined', 'Composite score.'),
    ('comprehensive', 'adjective', 'thorough', 'Comprehensive study.'),
    ('compulsory', 'adjective', 'mandatory', 'Compulsory education.'),
    ('computational', 'adjective', 'of computing', 'Computational method.'),
    ('conceivable', 'adjective', 'possible', 'Conceivable outcome.'),
    ('concentrated', 'adjective', 'focused', 'Concentrated effort.'),
    ('conceptual', 'adjective', 'abstract', 'Conceptual framework.'),
    ('concerned', 'adjective', 'worried', 'Deeply concerned.'),
]

# Band 8.0+: 목표 800개 (현재 ~320개, 480개 추가 필요)
FINAL_BAND80 = [
    # 최고급 동사
    ('excise', 'verb', 'to remove', 'Excise irrelevant data.'),
    ('excoriate', 'verb', 'to criticize severely', 'Excoriate methodology.'),
    ('exculpate', 'verb', 'to free from blame', 'Exculpate researchers.'),
    ('execrate', 'verb', 'to detest', 'Execrate dishonesty.'),
    ('exempt', 'verb', 'to free from', 'Exempt from rules.'),
    ('exert', 'verb', 'to apply', 'Exert influence.'),
    ('exhort', 'verb', 'to urge', 'Exhort to action.'),
    ('exhume', 'verb', 'to dig up', 'Exhume evidence.'),
    ('exonerate', 'verb', 'to absolve', 'Exonerate from blame.'),
    ('expatiate', 'verb', 'to elaborate', 'Expatiate on theory.'),
    ('expedite', 'verb', 'to speed up', 'Expedite review.'),
    ('expiate', 'verb', 'to atone', 'Expiate errors.'),
    ('explicate', 'verb', 'to explain', 'Explicate meaning.'),
    ('expound', 'verb', 'to explain', 'Expound theory.'),
    ('expropriate', 'verb', 'to take away', 'Expropriate ideas.'),
    ('expunge', 'verb', 'to erase', 'Expunge from record.'),
    ('extemporize', 'verb', 'to improvise', 'Extemporize response.'),
    ('extenuate', 'verb', 'to lessen', 'Extenuate circumstances.'),
    ('extirpate', 'verb', 'to destroy', 'Extirpate errors.'),
    ('extol', 'verb', 'to praise', 'Extol virtues.'),
    # 최고급 명사
    ('claptrap', 'noun', 'nonsense', 'Academic claptrap.'),
    ('clarity', 'noun', 'clearness', 'Crystal clarity.'),
    ('clash', 'noun', 'conflict', 'Intellectual clash.'),
    ('classification', 'noun', 'categorization', 'Classification system.'),
    ('clemency', 'noun', 'mercy', 'Show clemency.'),
    ('cliche', 'noun', 'overused phrase', 'Avoid cliches.'),
    ('clientele', 'noun', 'customers', 'Research clientele.'),
    ('climax', 'noun', 'peak', 'Reach climax.'),
    ('clique', 'noun', 'exclusive group', 'Academic clique.'),
    ('closure', 'noun', 'conclusion', 'Bring closure.'),
    ('coalition', 'noun', 'alliance', 'Form coalition.'),
    ('codification', 'noun', 'systematization', 'Legal codification.'),
    ('coercion', 'noun', 'force', 'Without coercion.'),
    ('cognizance', 'noun', 'awareness', 'Take cognizance.'),
    ('coherence', 'noun', 'consistency', 'Internal coherence.'),
    ('cohesion', 'noun', 'unity', 'Social cohesion.'),
    ('coincidence', 'noun', 'chance occurrence', 'Mere coincidence.'),
    ('collaboration', 'noun', 'cooperation', 'Research collaboration.'),
    ('collation', 'noun', 'comparison', 'Data collation.'),
    ('colloquialism', 'noun', 'informal expression', 'Avoid colloquialisms.'),
    # 최고급 형용사
    ('circumspect', 'adjective', 'cautious', 'Circumspect approach.'),
    ('circumstantial', 'adjective', 'incidental', 'Circumstantial evidence.'),
    ('civic', 'adjective', 'of city', 'Civic duty.'),
    ('clairvoyant', 'adjective', 'psychic', 'Clairvoyant prediction.'),
    ('clamorous', 'adjective', 'noisy', 'Clamorous debate.'),
    ('clandestine', 'adjective', 'secret', 'Clandestine operation.'),
    ('clarion', 'adjective', 'clear', 'Clarion call.'),
    ('classical', 'adjective', 'traditional', 'Classical approach.'),
    ('classifiable', 'adjective', 'can be classified', 'Classifiable data.'),
    ('claustrophobic', 'adjective', 'confined', 'Claustrophobic atmosphere.'),
    ('clean-cut', 'adjective', 'clear', 'Clean-cut distinction.'),
    ('clearheaded', 'adjective', 'rational', 'Clearheaded analysis.'),
    ('clerical', 'adjective', 'administrative', 'Clerical error.'),
    ('climactic', 'adjective', 'of climax', 'Climactic conclusion.'),
    ('clinical', 'adjective', 'detached', 'Clinical objectivity.'),
    ('cloistered', 'adjective', 'secluded', 'Cloistered academia.'),
    ('close-knit', 'adjective', 'tightly bound', 'Close-knit community.'),
    ('clouded', 'adjective', 'obscured', 'Clouded judgment.'),
    ('coalesced', 'adjective', 'combined', 'Coalesced theories.'),
    ('coarse', 'adjective', 'rough', 'Coarse analysis.'),
]

CATEGORIES_45 = ['Academic', 'Environment', 'Technology', 'Health', 'Education',
                 'Business', 'Society', 'Science', 'Culture', 'Media']
CATEGORIES_60 = ['Academic', 'Research', 'Science', 'Analysis', 'Writing', 
                 'Critical Thinking', 'Education', 'Professional', 'Data', 'Theory']
CATEGORIES_70 = ['Academic Writing', 'Research Methods', 'Critical Analysis', 
                 'Advanced Theory', 'Scholarly Discussion', 'Professional Development']
CATEGORIES_80 = ['Advanced Academic Writing', 'Sophisticated Argumentation', 
                 'Expert Level Research', 'High-Level Critical Analysis']

def add_words(filename, words, level, categories):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    except:
        existing = []
    
    existing_words = {w['word'] for w in existing}
    start_id = len(existing) + 1
    added = 0
    
    for word, pos, definition, example in words:
        if word not in existing_words:
            existing.append({
                'id': start_id + added,
                'word': word,
                'level': level,
                'partOfSpeech': pos,
                'definition': definition,
                'example': example,
                'category': categories[(start_id + added) % len(categories)]
            })
            existing_words.add(word)
            added += 1
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    return len(existing), added

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    total45, added45 = add_words('assets/data/band45_words.json', FINAL_BAND45, 'Band 4.5-5.5', CATEGORIES_45)
    print(f'✅ Band 4.5-5.5: {total45}개 (추가: {added45}개)')
    
    total60, added60 = add_words('assets/data/band60_words.json', FINAL_BAND60, 'Band 6.0-6.5', CATEGORIES_60)
    print(f'✅ Band 6.0-6.5: {total60}개 (추가: {added60}개)')
    
    total70, added70 = add_words('assets/data/band70_words.json', FINAL_BAND70, 'Band 7.0-7.5', CATEGORIES_70)
    print(f'✅ Band 7.0-7.5: {total70}개 (추가: {added70}개)')
    
    total80, added80 = add_words('assets/data/band80_words.json', FINAL_BAND80, 'Band 8.0+', CATEGORIES_80)
    print(f'✅ Band 8.0+: {total80}개 (추가: {added80}개)')

if __name__ == '__main__':
    main()
