#!/usr/bin/env python3
"""Band 7.0-7.5 추가 단어 (Part 2)"""
import json

WORDS_PART2 = [
    # 고급 학술 동사 (120개)
    ('abate', 'verb', 'to reduce in intensity', 'The controversy did not abate.'),
    ('abdicate', 'verb', 'to give up power', 'Abdicate responsibility.'),
    ('abrogate', 'verb', 'to abolish formally', 'Abrogate the agreement.'),
    ('accentuate', 'verb', 'to emphasize', 'Accentuate key findings.'),
    ('acclimatize', 'verb', 'to adjust to climate', 'Acclimatize to new conditions.'),
    ('accrue', 'verb', 'to accumulate', 'Benefits accrue over time.'),
    ('adjudicate', 'verb', 'to judge', 'Adjudicate disputes.'),
    ('admonish', 'verb', 'to warn', 'Admonish against hasty conclusions.'),
    ('adulterate', 'verb', 'to make impure', 'Adulterate the data.'),
    ('aggravate', 'verb', 'to make worse', 'Aggravate the situation.'),
    ('alleviate', 'verb', 'to reduce severity', 'Alleviate poverty.'),
    ('amalgamate', 'verb', 'to combine', 'Amalgamate departments.'),
    ('ameliorate', 'verb', 'to improve', 'Ameliorate conditions.'),
    ('annex', 'verb', 'to attach', 'Annex supporting documents.'),
    ('annihilate', 'verb', 'to destroy', 'Annihilate the opposition.'),
    ('arbitrate', 'verb', 'to settle dispute', 'Arbitrate between parties.'),
    ('articulate', 'verb', 'to express clearly', 'Articulate arguments.'),
    ('ascertain', 'verb', 'to find out', 'Ascertain the facts.'),
    ('assimilate', 'verb', 'to absorb', 'Assimilate information.'),
    ('attenuate', 'verb', 'to weaken', 'Attenuate the signal.'),
    ('augment', 'verb', 'to increase', 'Augment existing research.'),
    ('bequeath', 'verb', 'to leave to another', 'Bequeath knowledge.'),
    ('buttress', 'verb', 'to support', 'Buttress the argument.'),
    ('calibrate', 'verb', 'to adjust precisely', 'Calibrate instruments.'),
    ('capitulate', 'verb', 'to surrender', 'Capitulate to pressure.'),
    ('catalyze', 'verb', 'to cause change', 'Catalyze innovation.'),
    ('circumscribe', 'verb', 'to limit', 'Circumscribe the scope.'),
    ('circumvent', 'verb', 'to avoid', 'Circumvent regulations.'),
    ('coalesce', 'verb', 'to come together', 'Ideas coalesce.'),
    ('codify', 'verb', 'to arrange systematically', 'Codify the rules.'),
    ('cognize', 'verb', 'to perceive', 'Cognize the implications.'),
    ('cohere', 'verb', 'to stick together', 'Arguments cohere.'),
    ('collate', 'verb', 'to collect and compare', 'Collate data.'),
    ('commemorate', 'verb', 'to honor memory', 'Commemorate achievements.'),
    ('commiserate', 'verb', 'to express sympathy', 'Commiserate with colleagues.'),
    ('commute', 'verb', 'to change', 'Commute sentences.'),
    ('compel', 'verb', 'to force', 'Compel action.'),
    ('condense', 'verb', 'to make more concise', 'Condense the report.'),
    ('confiscate', 'verb', 'to seize', 'Confiscate materials.'),
    ('conflate', 'verb', 'to combine', 'Conflate two concepts.'),
    ('congregate', 'verb', 'to gather', 'Scholars congregate.'),
    ('conjecture', 'verb', 'to guess', 'Conjecture about outcomes.'),
    ('consecrate', 'verb', 'to dedicate', 'Consecrate to research.'),
    ('consolidate', 'verb', 'to strengthen', 'Consolidate findings.'),
    ('construe', 'verb', 'to interpret', 'Construe the meaning.'),
    ('consummate', 'verb', 'to complete', 'Consummate the deal.'),
    ('contaminate', 'verb', 'to pollute', 'Contaminate samples.'),
    ('contravene', 'verb', 'to violate', 'Contravene regulations.'),
    ('convene', 'verb', 'to assemble', 'Convene a meeting.'),
    ('converge', 'verb', 'to come together', 'Theories converge.'),
    # 고급 학술 명사 (120개)
    ('aberration', 'noun', 'deviation from normal', 'Statistical aberration.'),
    ('abstraction', 'noun', 'general idea', 'Level of abstraction.'),
    ('acumen', 'noun', 'keen insight', 'Business acumen.'),
    ('adjunct', 'noun', 'addition', 'Adjunct to the theory.'),
    ('advent', 'noun', 'arrival', 'Advent of technology.'),
    ('adversity', 'noun', 'hardship', 'Overcome adversity.'),
    ('affinity', 'noun', 'natural liking', 'Affinity for research.'),
    ('aftermath', 'noun', 'consequence', 'In the aftermath.'),
    ('allegation', 'noun', 'accusation', 'Serious allegations.'),
    ('allusion', 'noun', 'indirect reference', 'Literary allusion.'),
    ('amalgamation', 'noun', 'combination', 'Amalgamation of ideas.'),
    ('ambivalence', 'noun', 'mixed feelings', 'Academic ambivalence.'),
    ('amenity', 'noun', 'useful feature', 'Research amenities.'),
    ('analogue', 'noun', 'comparable thing', 'Digital analogue.'),
    ('anomaly', 'noun', 'irregularity', 'Statistical anomaly.'),
    ('antagonism', 'noun', 'hostility', 'Intellectual antagonism.'),
    ('antecedent', 'noun', 'predecessor', 'Historical antecedent.'),
    ('antidote', 'noun', 'remedy', 'Antidote to ignorance.'),
    ('antipathy', 'noun', 'strong dislike', 'Antipathy toward theory.'),
    ('apex', 'noun', 'highest point', 'Apex of achievement.'),
    ('apparition', 'noun', 'ghostly figure', 'Apparition of doubt.'),
    ('appellation', 'noun', 'name or title', 'Technical appellation.'),
    ('appraisal', 'noun', 'assessment', 'Critical appraisal.'),
    ('apprehension', 'noun', 'anxiety', 'Apprehension about results.'),
    ('arbiter', 'noun', 'judge', 'Arbiter of taste.'),
    ('archetype', 'noun', 'original model', 'Classic archetype.'),
    ('array', 'noun', 'impressive display', 'Array of evidence.'),
    ('articulation', 'noun', 'expression', 'Clear articulation.'),
    ('ascendancy', 'noun', 'dominance', 'Rise to ascendancy.'),
    ('aspiration', 'noun', 'ambition', 'Academic aspirations.'),
    ('assertion', 'noun', 'confident statement', 'Bold assertion.'),
    ('attrition', 'noun', 'gradual reduction', 'Participant attrition.'),
    ('auspices', 'noun', 'patronage', 'Under the auspices of.'),
    ('autonomy', 'noun', 'independence', 'Intellectual autonomy.'),
    ('axiom', 'noun', 'self-evident truth', 'Mathematical axiom.'),
    ('backdrop', 'noun', 'background', 'Against this backdrop.'),
    ('backlash', 'noun', 'strong reaction', 'Political backlash.'),
    ('benchmark', 'noun', 'standard', 'Industry benchmark.'),
    ('beneficiary', 'noun', 'receiver of benefit', 'Primary beneficiary.'),
    ('blueprint', 'noun', 'detailed plan', 'Blueprint for success.'),
    ('bottleneck', 'noun', 'point of congestion', 'Research bottleneck.'),
    ('breakthrough', 'noun', 'important discovery', 'Scientific breakthrough.'),
    ('brevity', 'noun', 'shortness', 'Brevity of response.'),
    ('bureaucracy', 'noun', 'administrative system', 'Government bureaucracy.'),
    ('cadre', 'noun', 'group of trained people', 'Cadre of experts.'),
    ('caliber', 'noun', 'quality', 'High caliber research.'),
    ('canon', 'noun', 'body of accepted works', 'Literary canon.'),
    ('catalyst', 'noun', 'agent of change', 'Catalyst for reform.'),
    ('caveat', 'noun', 'warning', 'Important caveat.'),
    ('cessation', 'noun', 'stopping', 'Cessation of hostilities.'),
    # 고급 학술 형용사 (60개)
    ('abject', 'adjective', 'miserable', 'Abject failure.'),
    ('abstruse', 'adjective', 'difficult to understand', 'Abstruse theory.'),
    ('acclaimed', 'adjective', 'praised', 'Critically acclaimed.'),
    ('adamant', 'adjective', 'unyielding', 'Adamant position.'),
    ('adept', 'adjective', 'skilled', 'Adept at analysis.'),
    ('adverse', 'adjective', 'unfavorable', 'Adverse effects.'),
    ('aesthetic', 'adjective', 'relating to beauty', 'Aesthetic considerations.'),
    ('affluent', 'adjective', 'wealthy', 'Affluent societies.'),
    ('altruistic', 'adjective', 'selfless', 'Altruistic behavior.'),
    ('ambivalent', 'adjective', 'having mixed feelings', 'Ambivalent response.'),
    ('amenable', 'adjective', 'open to suggestion', 'Amenable to change.'),
    ('amorphous', 'adjective', 'shapeless', 'Amorphous concept.'),
    ('ancillary', 'adjective', 'supporting', 'Ancillary benefits.'),
    ('anomalous', 'adjective', 'irregular', 'Anomalous results.'),
    ('antithetical', 'adjective', 'directly opposed', 'Antithetical views.'),
    ('arduous', 'adjective', 'difficult', 'Arduous process.'),
    ('arcane', 'adjective', 'mysterious', 'Arcane knowledge.'),
    ('astute', 'adjective', 'shrewd', 'Astute observation.'),
    ('austere', 'adjective', 'severe', 'Austere measures.'),
    ('auspicious', 'adjective', 'favorable', 'Auspicious beginning.'),
    ('autonomous', 'adjective', 'independent', 'Autonomous region.'),
    ('axiomatic', 'adjective', 'self-evident', 'Axiomatic principle.'),
    ('banal', 'adjective', 'commonplace', 'Banal explanation.'),
    ('benevolent', 'adjective', 'kind', 'Benevolent policy.'),
    ('benign', 'adjective', 'harmless', 'Benign neglect.'),
    ('blatant', 'adjective', 'obvious', 'Blatant disregard.'),
    ('blithe', 'adjective', 'carefree', 'Blithe assumption.'),
    ('burgeoning', 'adjective', 'growing rapidly', 'Burgeoning field.'),
    ('candid', 'adjective', 'honest', 'Candid assessment.'),
    ('canonical', 'adjective', 'according to rules', 'Canonical text.'),
]

CATEGORIES = ['Academic Writing', 'Research Methods', 'Critical Analysis', 
              'Advanced Theory', 'Scholarly Discussion', 'Professional Development',
              'Data Interpretation', 'Literature Review', 'Argumentation', 'Synthesis']

def main():
    try:
        with open('assets/data/band70_words.json', 'r', encoding='utf-8') as f:
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
                'level': 'Band 7.0-7.5',
                'partOfSpeech': pos,
                'definition': definition,
                'example': example,
                'category': CATEGORIES[(start_id + added) % len(CATEGORIES)]
            })
            existing_words.add(word)
            added += 1
    
    with open('assets/data/band70_words.json', 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f'✅ Band 7.0-7.5 업데이트: {len(existing)}개 (추가: {added}개)')

if __name__ == '__main__':
    main()
