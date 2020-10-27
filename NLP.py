#HOW TO REMOVE P - TAGS
import re 

text = "<p>    This is a paragraph</p>" 

result = re.sub(r'<.?p>', '', text)

print(result) 
#    This is a paragraph

#HOW TO REMOVE WHITESPACE AT THE BEGINNING OF PARAGRAPH
import re 

text = "    This is a paragraph" 

result = re.sub(r'\s{4}', '', text)

print(result) 

#HOW TO TOKENIZE (SPLIT INTO INDIVIDUAL WORDS)
from nltk.tokenize import word_tokenize

text = "Tokenize this text"
tokenized = word_tokenize(text)

print(tokenized)
# ["Tokenize", "this", "text"]

#TOKENIZE AT A SENTENCE LEVEL; SENT_TOKENIZE
from nltk.tokenize import sent_tokenize

text = "Tokenize this sentence. Also, tokenize this sentence."
tokenized = sent_tokenize(text)

print(tokenized)
# ['Tokenize this sentence.', 'Also, tokenize this sentence.']