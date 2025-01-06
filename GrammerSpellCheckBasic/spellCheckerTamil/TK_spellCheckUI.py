import tkinter as tk
from tkinter import messagebox
from SpellCheckerTamil import SpellChecker, suggestions  # Use the provided SpellChecker class

# Function to handle user input and show suggestions
def check_spelling():
    user_input = input_text.get("1.0", "end-1c")  # Get the text from the input field
    
    if not user_input.strip():
        messagebox.showerror("Input Error", "Please enter some text to check.")
        return

    # Initialize the spell checker
    spell_checker = SpellChecker("wordsFinal.txt", user_input)
    
    # Get the corrected text
    corrected_text = spell_checker.correct()
    
    # Show the corrected text in the output field
    output_text.delete("1.0", "end")
    output_text.insert("1.0", corrected_text)
    
    # Show suggestions
    suggestions_text.delete("1.0", "end")
    for word in user_input.split():
        suggested_words = suggestions(word, spell_checker.correct_words)  # Using suggestions from the class
        if suggested_words:
            suggestions_text.insert("end", f"Suggestions for '{word}':\n")
            for suggested_word, score in suggested_words:
                suggestions_text.insert("end", f" - {suggested_word} (score: {score})\n")
            suggestions_text.insert("end", "\n")

# Set up the main window
window = tk.Tk()
window.title("Tamil Spell Checker")
window.geometry("600x500")

# Input Field
input_label = tk.Label(window, text="Enter your text:")
input_label.pack(pady=5)
input_text = tk.Text(window, height=5, width=70)
input_text.pack(pady=10)

# Check button
check_button = tk.Button(window, text="Check Spelling", command=check_spelling)
check_button.pack(pady=10)

# Output Field
output_label = tk.Label(window, text="Corrected Text:")
output_label.pack(pady=5)
output_text = tk.Text(window, height=5, width=70)
output_text.pack(pady=10)

# Suggestions Field
suggestions_label = tk.Label(window, text="Suggestions:")
suggestions_label.pack(pady=5)
suggestions_text = tk.Text(window, height=10, width=70)
suggestions_text.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
