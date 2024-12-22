# Tamil Spelling and Grammar Checker

## Overview

This project focuses on developing a Tamil spelling and grammar checker designed to assist users in identifying and correcting spelling errors and few basic grammatical mistakes in Tamil text. The primary goal is to enhance the quality and accuracy of Tamil language content for both casual users and professionals.


## Datasets

1. **Tamil Words Dataset**: 
   - [Tamil Loan Words Classification](https://www.kaggle.com/datasets/muthua/tamil-loan-words-classification)
   - Contains strictly Tamil words.

2. **Tamil News Dataset**: 
   - [Tamil News Dataset](https://www.kaggle.com/datasets/disisbig/tamil-news-dataset?select=train.csv)
   - Contains ~6500 news articles collected from Tamil news websites.

3. **Error Annotated Tamil Corpus**: 
   - [Error Annotated Tamil Corpus](https://www.kaggle.com/datasets/neechalkaran/error-annotated-tamil-corpus)
   - Used for grammar checking.


## Features

- **Spell Checking**: 
  - Uses prefix and suffix matching along with Levenshtein distance to suggest corrections for misspelled Tamil words.
  
- **Grammar Checking**: 
  - Implements rules for checking sentence structure, adjective-noun order, and plural agreement.

- **Machine Learning Approach**: 
  - Attempts to improve spell checking through logistic regression and LSTM networks.
    

## Installation

1. Clone the repository:
   git clone https://github.com/Kamsayini/Tamil-Spell-Grammar-Checker.git
