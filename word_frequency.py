# Importing the required libraries
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from collections import Counter

# Download required NLTK data (only needs to be run once)
nltk.download('punkt')
nltk.download('stopwords')

# Reading the text file
try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: texto.txt file not found")
    exit()

# Tokenize the text into words
words = word_tokenize(content)

# Remove punctuation
words = [word for word in words if word.isalnum()]

# Remove stop words
stop_words = set(stopwords.words('english'))
words = [word for word in words if word.lower() not in stop_words]

# Remove numbers
words = [word for word in words if not word.isdigit()]

# Get the 20 most common words
word_freq = Counter(words)
common_words = word_freq.most_common(20)

# Print the results
print("The 20 most common words are:")
for word, freq in common_words:
    print(f"{word}: {freq}")
