#!/usr/bin/env python3
"""Band 8.0+ 추가 단어 (Part 2)"""
import json

WORDS_PART2 = [
    # 최상급 학술 동사 (80개)
    ('abnegate', 'verb', 'to renounce or reject', 'Abnegate traditional approaches.'),
    ('abjure', 'verb', 'to solemnly renounce', 'Abjure outdated methods.'),
    ('ablate', 'verb', 'to remove by erosion', 'Ablate excess material.'),
    ('adumbrate', 'verb', 'to outline or foreshadow', 'Adumbrate future trends.'),
    ('aggrandize', 'verb', 'to increase power or reputation', 'Aggrandize the theory.'),
    ('anathematize', 'verb', 'to curse or condemn', 'Anathematize opposing views.'),
    ('animadvert', 'verb', 'to criticize', 'Animadvert upon methodology.'),
    ('apostatize', 'verb', 'to abandon beliefs', 'Apostatize from tradition.'),
    ('arrogate', 'verb', 'to claim without justification', 'Arrogate authority.'),
    ('asseverate', 'verb', 'to declare solemnly', 'Asseverate the findings.'),
    ('attenuate', 'verb', 'to weaken or reduce', 'Attenuate the effects.'),
    ('bowdlerize', 'verb', 'to censor', 'Bowdlerize the report.'),
    ('calumniate', 'verb', 'to slander', 'Calumniate colleagues.'),
    ('canalize', 'verb', 'to direct into channels', 'Canalize research efforts.'),
    ('castigate', 'verb', 'to criticize severely', 'Castigate poor methodology.'),
    ('cavil', 'verb', 'to make petty objections', 'Cavil at minor details.'),
    ('cognoscente', 'verb', 'to recognize as expert', 'Cognoscente in the field.'),
    ('collogue', 'verb', 'to confer secretly', 'Collogue with experts.'),
    ('comminate', 'verb', 'to threaten divine punishment', 'Comminate against error.'),
    ('concatenate', 'verb', 'to link together', 'Concatenate data sets.'),
    ('confabulate', 'verb', 'to talk informally', 'Confabulate theories.'),
    ('conflate', 'verb', 'to merge', 'Conflate distinct concepts.'),
    ('congeal', 'verb', 'to solidify', 'Ideas congeal into theory.'),
    ('conjoin', 'verb', 'to join together', 'Conjoin methodologies.'),
    ('connote', 'verb', 'to imply', 'Words connote meaning.'),
    ('contravene', 'verb', 'to violate', 'Contravene established norms.'),
    ('controvert', 'verb', 'to dispute', 'Controvert the hypothesis.'),
    ('corroborate', 'verb', 'to confirm', 'Corroborate findings.'),
    ('countermand', 'verb', 'to revoke', 'Countermand previous orders.'),
    ('countervail', 'verb', 'to counterbalance', 'Benefits countervail risks.'),
    ('decimate', 'verb', 'to destroy large part', 'Decimate the population.'),
    ('deconstruct', 'verb', 'to analyze critically', 'Deconstruct the argument.'),
    ('denigrate', 'verb', 'to criticize unfairly', 'Denigrate research.'),
    ('deprecate', 'verb', 'to express disapproval', 'Deprecate simplistic views.'),
    ('derogate', 'verb', 'to disparage', 'Derogate from standards.'),
    ('desiderate', 'verb', 'to feel lack of', 'Desiderate more evidence.'),
    ('disseminate', 'verb', 'to spread widely', 'Disseminate findings.'),
    ('dissimulate', 'verb', 'to conceal', 'Dissimulate true intentions.'),
    ('efface', 'verb', 'to erase', 'Efface previous errors.'),
    ('effectuate', 'verb', 'to bring about', 'Effectuate change.'),
    # 최상급 학술 명사 (80개)
    ('abeyance', 'noun', 'state of suspension', 'Hold in abeyance.'),
    ('abnegation', 'noun', 'self-denial', 'Abnegation of responsibility.'),
    ('absolution', 'noun', 'formal release', 'Absolution from blame.'),
    ('abstinence', 'noun', 'restraint', 'Abstinence from judgment.'),
    ('accolade', 'noun', 'award of praise', 'Academic accolade.'),
    ('accoutrement', 'noun', 'equipment', 'Scholarly accoutrements.'),
    ('acme', 'noun', 'highest point', 'Acme of achievement.'),
    ('addendum', 'noun', 'addition', 'Include an addendum.'),
    ('adjuration', 'noun', 'solemn urging', 'Adjuration to comply.'),
    ('aegis', 'noun', 'protection', 'Under the aegis of.'),
    ('affidavit', 'noun', 'sworn statement', 'Submit an affidavit.'),
    ('afflatus', 'noun', 'divine inspiration', 'Creative afflatus.'),
    ('aggrandizement', 'noun', 'increase in power', 'Self-aggrandizement.'),
    ('alchemy', 'noun', 'mysterious transformation', 'Intellectual alchemy.'),
    ('algorithm', 'noun', 'step-by-step procedure', 'Complex algorithm.'),
    ('allocution', 'noun', 'formal speech', 'Judicial allocution.'),
    ('allotrope', 'noun', 'different form', 'Chemical allotrope.'),
    ('amalgam', 'noun', 'mixture', 'Amalgam of theories.'),
    ('anathema', 'noun', 'thing detested', 'Anathema to researchers.'),
    ('anchorite', 'noun', 'religious recluse', 'Academic anchorite.'),
    ('animadversion', 'noun', 'criticism', 'Scholarly animadversion.'),
    ('annuity', 'noun', 'yearly payment', 'Research annuity.'),
    ('antechamber', 'noun', 'waiting room', 'Antechamber of discovery.'),
    ('antinomy', 'noun', 'contradiction', 'Logical antinomy.'),
    ('antithesis', 'noun', 'direct opposite', 'Thesis and antithesis.'),
    ('aphorism', 'noun', 'short wise saying', 'Scientific aphorism.'),
    ('apogee', 'noun', 'highest point', 'Apogee of career.'),
    ('apotheosis', 'noun', 'glorification', 'Apotheosis of reason.'),
    ('apparatchik', 'noun', 'official', 'Academic apparatchik.'),
    ('appellation', 'noun', 'name', 'Technical appellation.'),
    ('approbation', 'noun', 'approval', 'Official approbation.'),
    ('archon', 'noun', 'ruler', 'Archon of discipline.'),
    ('argot', 'noun', 'specialized language', 'Academic argot.'),
    ('armature', 'noun', 'framework', 'Theoretical armature.'),
    ('arrant', 'noun', 'complete', 'Arrant nonsense.'),
    ('asseveration', 'noun', 'solemn declaration', 'Emphatic asseveration.'),
    ('assiduity', 'noun', 'persistent effort', 'Scholarly assiduity.'),
    ('atavism', 'noun', 'reversion to ancestral', 'Intellectual atavism.'),
    ('attainder', 'noun', 'loss of rights', 'Academic attainder.'),
    ('avatar', 'noun', 'embodiment', 'Avatar of progress.'),
    # 최상급 학술 형용사 (40개)
    ('abstruse', 'adjective', 'obscure and difficult', 'Abstruse theoretical framework.'),
    ('acerbic', 'adjective', 'sharp and critical', 'Acerbic commentary.'),
    ('acquisitive', 'adjective', 'eager to acquire', 'Acquisitive approach to data.'),
    ('adroit', 'adjective', 'clever and skillful', 'Adroit manipulation of variables.'),
    ('adulatory', 'adjective', 'excessively praising', 'Adulatory review.'),
    ('anachronistic', 'adjective', 'belonging to another time', 'Anachronistic methodology.'),
    ('anodyne', 'adjective', 'unlikely to offend', 'Anodyne conclusion.'),
    ('antipodal', 'adjective', 'diametrically opposite', 'Antipodal positions.'),
    ('apocryphal', 'adjective', 'of doubtful authenticity', 'Apocryphal evidence.'),
    ('apposite', 'adjective', 'apt and appropriate', 'Apposite reference.'),
    ('architectonic', 'adjective', 'relating to structure', 'Architectonic framework.'),
    ('artless', 'adjective', 'without guile', 'Artless presentation.'),
    ('ascetic', 'adjective', 'severely self-disciplined', 'Ascetic research approach.'),
    ('asinine', 'adjective', 'extremely foolish', 'Asinine argument.'),
    ('assiduous', 'adjective', 'showing great care', 'Assiduous attention to detail.'),
    ('atavistic', 'adjective', 'reverting to ancestral', 'Atavistic tendencies.'),
    ('attenuated', 'adjective', 'weakened', 'Attenuated argument.'),
    ('august', 'adjective', 'inspiring reverence', 'August institution.'),
    ('avaricious', 'adjective', 'greedy', 'Avaricious pursuit.'),
    ('axiomatic', 'adjective', 'self-evidently true', 'Axiomatic principles.'),
    ('baleful', 'adjective', 'threatening', 'Baleful implications.'),
    ('beatific', 'adjective', 'blissfully happy', 'Beatific discovery.'),
    ('bellicose', 'adjective', 'warlike', 'Bellicose rhetoric.'),
    ('benighted', 'adjective', 'in state of ignorance', 'Benighted view.'),
    ('bifurcated', 'adjective', 'divided into two', 'Bifurcated approach.'),
    ('boorish', 'adjective', 'rough and bad-mannered', 'Boorish dismissal.'),
    ('byzantine', 'adjective', 'excessively complicated', 'Byzantine regulations.'),
    ('caducous', 'adjective', 'tending to fall', 'Caducous assumptions.'),
    ('calumniatory', 'adjective', 'slanderous', 'Calumniatory assertions.'),
    ('capacious', 'adjective', 'spacious', 'Capacious theoretical framework.'),
]

CATEGORIES = ['Advanced Academic Writing', 'Sophisticated Argumentation', 
              'Expert Level Research', 'High-Level Critical Analysis',
              'Scholarly Excellence', 'Professional Mastery',
              'Distinguished Discourse', 'Elite Academia']

def main():
    try:
        with open('assets/data/band80_words.json', 'r', encoding='utf-8') as f:
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
                'level': 'Band 8.0+',
                'partOfSpeech': pos,
                'definition': definition,
                'example': example,
                'category': CATEGORIES[(start_id + added) % len(CATEGORIES)]
            })
            existing_words.add(word)
            added += 1
    
    with open('assets/data/band80_words.json', 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f'✅ Band 8.0+ 업데이트: {len(existing)}개 (추가: {added}개)')

if __name__ == '__main__':
    main()
