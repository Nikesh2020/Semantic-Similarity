"""
T38 Compulsory Task 1:
------------------
File name: garden.py
Author: Nikesh Chavda
Student ID: NC22110005394
Notes:
Assumptions:
Dependencies: please install spaCy:
Type the following commands in command line: -

pip3 install spacy
python3 -m spacy download en_core_web_sm
----------------OR----------------------
pip install spacy
python -m spacy download en_core_web_sm
"""

import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# similarity with spacy
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Results are as follows with en_core_web_md: -
'''
word1.similarity(word2) = 0.5929930274321619        (cat and monkey)
word3.similarity(word2) = 0.40415016164997786       (banana and monkey)
word3.similarity(word1) = 0.22358827466989753       (banana and cat)
'''
# Note, what is interesting about the results is that: -
# cat and monkey are the most similar which they are as they are both animals
# the 2nd most similar are monkey and banana because monkeys eat bananas
# and least similar are banana and cats as cats are not really associated with bananas

# Results are as follows with en_core_web_sm: -
'''
word1.similarity(word2) = 0.6770567131180597        (cat and monkey)
word3.similarity(word2) = 0.7276310914874259      (banana and monkey)
word3.similarity(word1) = 0.6806929608512433       (banana and cat)
'''

# loop through and compare each token in the sentence with each other token in the sentence for similarity
# apply the nlp model to the sentence first
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# sentence to compare
sentence_to_compare = "Why is my cat on the car"

# list of sentences to compare the above sentence with
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

# apply nlp model to the sentence before perform comparison on
model_sentence = nlp(sentence_to_compare)

# for every sentence in the sentences list compare it in terms of similarity with the sentence to compare with, and
# print results of the similarity comparison to the output console
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
