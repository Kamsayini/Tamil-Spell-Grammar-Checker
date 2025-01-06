import sys
import os
from sklearn.metrics import precision_score, recall_score, f1_score

# Ensure the current directory is in the Python path
sys.path.append(os.getcwd())

from SpellCheckerTamil import SpellChecker

def evaluate_spell_checker(test_sentences, expected_corrections, corrected_sentence):
    TP = 0  # True positive - mispelled words that were recognized as mispelled
    FP = 0  # False positive - valid words that were recognized as mispelled
    FN = 0  # False negative - mispelled words that were recognized as correct
    TN = 0  # True negative - valid words that were recognized as correct
    total_words = 0

    for i, sentence in enumerate(test_sentences):
        expected_sentence = expected_corrections[i]

        corrected_words = corrected_sentence.split()
        expected_words = expected_sentence.split()
        test_words = sentence.split()

        for corrected_word, expected_word, test_word in zip(corrected_words, expected_words, test_words):
            total_words += 1
            if test_word == expected_word:  # If the input word is correct
                if test_word == corrected_word:  # Predict as correct word
                    TN += 1
                else:  # Predict as mispelled word
                    FP += 1
            elif test_word != expected_word:  # If the input word is mispelled
                if test_word == corrected_word:  # Predict as correct word
                    FN += 1
                else:  # Predict as mispelled word
                    TP += 1

    # Metrics calculations
    accuracy = (TP + TN) / (TP + FP + FN + TN)
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    specificity = TN / (TN + FP) if (TN + FP) != 0 else 0
    f1_score_val = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Specificity: {specificity}")
    print(f"F1-Score: {f1_score_val}")


# Correct words file path
correct_words_file = r"C:\Users\HP\Desktop\GrammerSpellCheckBasic\spellCheckerTamil\extracted_words.txt"

test_paragraphs_list = [
    "ஏற்றுமதயை நம்பியுள்ள நாடுகளுகுத்தான் இதனால் பாதிப்பு. உள்நாட்டிலேயே தேவை அதிகமக உள்ள இந்தியா போன்ற மக்கள் தொகை அதிகம் கொண்ட வளரும் பொருளதர நாட்டில் பிரச்சனை ஏற்படது என்று அவர் திடவட்டமாகக் கூறினார்.",
    "இந்த நாளில், வடலர் வள்ளலர் கோயிலில், லட்சக்ணக்கான பக்தர்கள் தரிசனம் செய்வார்கள். அருட்பருஞ் ஜோதி தனப்பெருங்கருணை என்று கோஷங்ள் முழங்க, வள்ளலரை வணங்குவார்கள். வருவோருக்கெல்லாம் அன்னதானம் தடையின்றி நடந்து கெண்டே இருக்கும்.",
    "வர்த்தக அமைசசகத்தின் கீழ செயல்படும் சரக்கு போக்கவரத்து துறயை ஏற்கெனவ வாகன உற்பத்தியாளர் சங்க பிரதிநிதிகள் அணுகி இந்த பிரச்சனை குறித்து விவாதித்துள்லனர். பன்முக வரி விதப்பு முறை குலப்பமாக உள்ளதையும் குறிப்பிட்டுள்ளனர்.",
    "இநதப் பேரலகியடன் ஒப்பந்தம் செய்யபட்டுள்ள படம் விரைவில் படப்பிடிப்பு தொடங்கவிருக்கிறது. இந்தப் படம் பெரும் பொருட்செலவில் தயாரிக்கவிருக்கறது. இப்படத்தின் நயகன் எனக்கு மகவும் பிடித்த நடிகர், அவர் சமயலின் சிறப்புக்கு எடுத்துக்காட்டாக விளங்குகிறார். படம் பற்றிய எதிர்பர்ப்புகள் அதிகமாக உள்ளன. படம் படப்பிடிப்பு முடிந்த பன்னர், அத மக்களுக்கு மிகவும் வரவேற்கப்படும் என நம்புறேன்.",
    "சூரபதமன் என்ற அரக்ன் சிறந்த சிவ பக்தன். அவன மிகப் பெரிய யகங்கள், தவங்கள் செய்து சிவபருமானின் நன்மதிப்பைப் பெற்றான். அவனுக்கு வரமலிக்க விரும்பினார் சிவன். ஈசன் உட்பட யாருக்கும் தன்னக் கெல்ல வல்லமை இருக்கக் கூடாது என்று வேண்டினன் சூரன்."
]

expected_paragraph = [
    "ஏற்றுமதியை நம்பியுள்ள நாடுகளுக்குத்தான் இதனால் பாதிப்பு. உள்நாட்டிலேயே தேவை அதிகமாக உள்ள இந்தியா போன்ற மக்கள் தொகை அதிகம் கொண்ட வளரும் பொருளாதார நாட்டில் பிரச்சனை ஏற்படாது என்று அவர் திட்டவட்டமாகக் கூறினார்.",
    "இந்த நாளில், வடலூர் வள்ளலார் கோயிலில், லட்சக்கணக்கான பக்தர்கள் தரிசனம் செய்வார்கள். அருட்பெருஞ் ஜோதி தனிப்பெருங்கருணை என்று கோஷங்கள் முழங்க, வள்ளலாரை வணங்குவார்கள். வருவோருக்கெல்லாம் அன்னதானம் தடையின்றி நடந்து கொண்டே இருக்கும்.",
    "வர்த்தக அமைச்சகத்தின் கீழ் செயல்படும் சரக்கு போக்குவரத்து துறையை ஏற்கெனவே வாகன உற்பத்தியாளர் சங்க பிரதிநிதிகள் அணுகி இந்த பிரச்சனை குறித்து விவாதித்துள்ளனர். பன்முக வரி விதிப்பு முறை குழப்பமாக உள்ளதையும் குறிப்பிட்டுள்ளனர்.",
    "இந்தப் பேரழகியுடன் ஒப்பந்தம் செய்யப்பட்டுள்ள படம் விரைவில் படப்பிடிப்பு தொடங்கவிருக்கிறது. இந்தப் படம் பெரும் பொருட்செலவில் தயாரிக்கவிருக்கிறது. இப்படத்தின் நாயகன் எனக்கு மிகவும் பிடித்த நடிகர், அவர் சமையலின் சிறப்புக்கு எடுத்துக்காட்டாக விளங்குகிறார். படம் பற்றிய எதிர்பார்ப்புகள் அதிகமாக உள்ளன. படம் படப்பிடிப்பு முடிந்த பின்னர், அது மக்களுக்கு மிகவும் வரவேற்கப்படும் என நம்புகிறேன்.",
    "சூரபதுமன் என்ற அரக்கன் சிறந்த சிவ பக்தன். அவன் மிகப் பெரிய யாகங்கள், தவங்கள் செய்து சிவபெருமானின் நன்மதிப்பைப் பெற்றான். அவனுக்கு வரமளிக்க விரும்பினார் சிவன். ஈசன் உட்பட யாருக்கும் தன்னைக் கொல்ல வல்லமை இருக்கக் கூடாது என்று வேண்டினான் சூரன்."
]

# Split the text into sentences for checking
test_sentences = [para.rstrip(".").split(".") for para in test_paragraphs_list]
expected_sentences = [para.rstrip(".").split(".") for para in expected_paragraph]

# Loop through test paragraphs and perform spell/grammar correction
for idx, test_sentences_group in enumerate(test_sentences):
    print(f"\n\n--- Testing Paragraph {idx+1} ---")

    for i, sentence in enumerate(test_sentences_group):
        print(f"\nTest Sentence {i+1}: {sentence.strip()}")

        # Initialize the SpellChecker object
        spell_checker = SpellChecker(correct_words_file, sentence)
        corrected_text = spell_checker.correct()

        # Output the corrected text
        print(f"Corrected Text: {corrected_text.strip()}")
        print(f"Expected Text: {expected_sentences[idx][i].strip()}")

        # Evaluate the spell checker against the expected result
        print("--- Evaluation Results ---")
        evaluate_spell_checker([sentence.strip()], [expected_sentences[idx][i].strip()], corrected_text.strip())

