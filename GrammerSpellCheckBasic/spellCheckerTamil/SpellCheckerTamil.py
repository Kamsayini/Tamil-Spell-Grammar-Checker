def prefix_match(string1, string2): 
    common_length = 0
    min_len = min(len(string1), len(string2))
    for i in range(min_len):
        if string1[i] == string2[i]:
            common_length += 1
        else:
            break
    return common_length

def suffix_match(string1, string2):
    common_length = 0
    min_len = min(len(string1), len(string2))
    for i in range(1, min_len + 1):
        if string1[-i] == string2[-i]:
            common_length += 1
        else:
            break
    return common_length

def prefilter_candidates(user_input, correct_words, length_threshold=2):
    return [
        word for word in correct_words
        if abs(len(word) - len(user_input)) <= length_threshold
    ]

def suggestions(user_input, correct_words):
    suggestions = []
    filtered_correct_words = prefilter_candidates(user_input, correct_words, 2)

    for word in filtered_correct_words:
        prefix_score = prefix_match(user_input, word)
        suffix_score = suffix_match(user_input, word)
        score = prefix_score + suffix_score

        if score > 0:
            suggestions.append((word, score))
        
    suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)
    return suggestions

def levenshtein_distance(string1, string2):
    n, m = len(string1), len(string2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insertion = 1 + dp[i][j-1]
                deletion = 1 + dp[i-1][j]
                replacement = 1 + dp[i-1][j-1]
                dp[i][j] = min(insertion, deletion, replacement)
    
    return dp[n][m]

def find_closest_levenshtein(user_input, correct_words):
    return min(correct_words, key=lambda word: levenshtein_distance(user_input, word))

class SpellChecker:
    def __init__(self, correct_words_file, user_input):
        self.user_input_words = user_input.split()
        with open(correct_words_file, 'r', encoding='utf-8') as file:
            data = file.readlines()
        self.correct_words = [word.strip() for word in data]
    
    def correct(self):
        corrected_words = []
        for word_to_check in self.user_input_words:
            suggested_words = suggestions(word_to_check, self.correct_words)

            print(f"Number of Suggested words for {word_to_check} -> {len(suggested_words)}")

            if suggested_words:
                best_match = find_closest_levenshtein(word_to_check, [s[0] for s in suggested_words])
                corrected_word = best_match.strip()
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word_to_check)

        return " ".join(corrected_words)
