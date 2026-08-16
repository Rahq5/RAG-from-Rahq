# here am trying to test 


import spacy

# Load a pre-trained English model
nlp = spacy.load("en_core_web_sm")

text = """
Hello Mr. Rawi this is me writitng some things to test. the mo. del amd trying to, if he gonna split them. cccor. not.
omg it's not working as expected 
"""

doc = nlp(text)

# Iterate over sentences
for sent in doc.sents:
    print(sent.text)


# ----- output ------
# output: 
'''

Hello Mr. Rawi this is me writitng some things to test.
the mo.
del amd trying to, if he gonna split them.
cccor.
not.

omg it's not working as expected 

'''

# conclusion: it has lower level of smartness 