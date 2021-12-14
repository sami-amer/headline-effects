"""
Calculates the overall positivity, negativity, and objectivity of a piece of text.
The scorer uses sentiword net, which calculates sentiment per word. We then add the sentiment scores up to get total score
"""

# native
import re
import string

# lib
import nltk

from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet
from nltk.corpus import stopwords

from nltk.tag import pos_tag

from nltk.tokenize import word_tokenize

from nltk.tree import bracket_parse

from nltk.stem.wordnet import WordNetLemmatizer

# nltk.download('sentiwordnet')
# nltk.download('stopwords')

## ------------------------------------------------------------------------------------------------
##
## The following code is borrowed from 
## 
## Jackson, Holly (2021). The New York Times Distorts the Palestinian Struggle:
## A Case Study of Anti-Palestinian Bias in American News Coverage of the First
## and Second Palestinian Intifadas. Pre-print: http://web.mit.edu/hjackson/www/The_NYT_Distorts_the_Palestinian_Struggle.pdf.
##
## in the following file
##
## https://github.com/hollyjackson/NYT_Content_Analysis/blob/main/generate_training_set.py
##

def clean_text(text):
    # will replace the html characters with " "
    text = re.sub('<.*?>', ' ', text)  
    # to remove the punctuations
    text = text.translate(str.maketrans(' ',' ',string.punctuation))
    # will consider only alphabets and numerics
    text = re.sub('[^a-zA-Z]',' ',text)  
    # will replace newline with space
    text = re.sub("\n"," ",text)
    # will convert to lower case
    text = text.lower()
    return text

def preprocess(text):
    stop_words = set(stopwords.words('english')) 
    lemmatizer = WordNetLemmatizer()
    # split into words
    text = clean_text(text)
    # separate into words and remove stop words
    word_tokens = word_tokenize(text) 
    output_text = [w for w in word_tokens if not w in stop_words] 
    # lemmatize words
    lemmatized_text = [lemmatizer.lemmatize(w) for w in output_text]
    return lemmatized_text

##
##
## ------------------------------------------------------------------------------------------------

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''


def sentinet_scorer(text):
    tokens = preprocess(text)
    tagged = pos_tag(tokens)

    pos_score = 0 
    neg_score = 0
    obj_score = 0
    num_words = 0

    for tup in tagged:
        new_tag = get_wordnet_pos(tup[1])

        words = swn.senti_synsets(tup[0], new_tag)
        list_words = list(words)
        if len(list_words) != 0:
            word = list_words[0]

            pos_score += word.pos_score()
            neg_score -= word.neg_score()
            obj_score += word.obj_score()
            num_words += 1

    if num_words == 0:
        return None
    avg_pos_score = pos_score / num_words
    avg_neg_score = neg_score / num_words
    avg_obj_score = obj_score / num_words
    
    return avg_pos_score, avg_neg_score, avg_obj_score
   