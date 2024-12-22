from SpellCheckerTamil import SpellChecker
import re

# Define the paths to the input files
file1_path = r"words.txt"
file2_path = r"extracted_words.txt"
correct_words_file = r"wordsFinal.txt"

# Read the contents of the two files and combine them into one
with open(file1_path, 'r', encoding='utf-8') as file1:
    file1_contents = file1.readlines()

with open(file2_path, 'r', encoding='utf-8') as file2:
    file2_contents = file2.readlines()

# Combine both files' contents and write them to 'wordsFinal.txt'
with open(correct_words_file, 'w', encoding='utf-8') as final_file:
    # Write content of both files, keeping each word on a new line
    for line in file1_contents:
        final_file.write(line)
    for line in file2_contents:
        final_file.write(line)

# Sample paragraphs with spelling mistakes
paragraphs = [
    "இந்த காலை அவன் மிகவும் சந்தஷமாக இருந்தான். அவன் செலல தயராக இருந்தான். அவன் பெற்றோரகளுடன் உணவு பரிமாறிக கொண்டிருந்தான், மற்றும் செலலும் போது, அவன் புதிய நண்பர்களைச் சந்தக்க ஆவலுடன் இருந்தான்."
    "அவ படிப்பில் மிகவும் கவனம் செலத்துவான், மற்றும் நாளும் அதிகம் கற்றுக்கொள்ள வரும்புவான்."
]

# Function to correct each paragraph and save the results
def correct_paragraphs(paragraphs, correct_words_file):
    corrected_paragraphs = []
    
    # Initialize the spell checker and correct each paragraph
    for paragraph in paragraphs:
        spell_checker = SpellChecker(correct_words_file, paragraph)
        corrected_text = spell_checker.correct()
        
        # Print the corrected paragraph
        print("Corrected Paragraph:")
        print(corrected_text)
        print("\n" + "="*50 + "\n")  # Separator between paragraphs
        
        corrected_paragraphs.append(corrected_text)
        
    # Save the corrected text to a file
    with open("corrected_text.txt", 'w', encoding='utf-8') as output_file:
        for corrected_paragraph in corrected_paragraphs:
            output_file.write(corrected_paragraph + "\n\n")  # Add space between paragraphs

    print("Corrected text has been saved to 'corrected_text.txt'.")

# Call the function to process and save the corrected text
correct_paragraphs(paragraphs, correct_words_file)
