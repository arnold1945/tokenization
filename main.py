# 🧠 Your Task: Tokenize the story from 'story.txt' using NLTK's sent_tokenize and word_tokenize functions

# Make sure required NLTK resources are available
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import nltk
nltk.download('punkt')      # Tokenizer models returns True
nltk.download('stopwords')  # List of common stopwords returns True
nltk.download('wordnet')    # For lemmatization returns True
nltk.download('averaged_perceptron_tagger')  # For POS tagging returns True
# 1. Open and read the story text

file = open('story.txt')
text_from_file = file.read()
file.close()




# 2. (Optional) Remove any unwanted characters using re.sub
# For example: remove extra whitespace or punctuation symbols
# clean_story = None  # Keep common sentence characters
clean_story = re.sub(r'[#|*|-|_]', '', text_from_file)
# print(clean_story)


# 3. Tokenize the story into sentences
# TODO: Replace the line below with a call to sent_tokenize
sentences = sent_tokenize(clean_story)



# 4. Tokenize the story into words
# TODO: Replace the line below with a call to word_tokenize


words = word_tokenize(clean_story)

# 5. Print results
print("=== Sentences ===")
print(sentences)
print("\n=== Words ===")
print(words)
