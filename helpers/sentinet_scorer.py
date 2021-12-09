"""
    sentinet_scorer.py calculates the overall positivity, negativity, and objectivity of a piece of text.
    the scorer uses sentiword net, which calculates sentiment per word. we then add the sentiment scores up to get total score

    the program processes text in these steps:
        clean and preprocess text
            clean (strip)
            remove filler words
            lemmatize
        assign part of speech tag
            convert to swn format
        calculate sentiment per word
        computer acg scores ann return
        ? To do: maybe get importance?
        input raw string of words (either headline or article)
        output avg objextvity score of text (total obj score / words) along with avg pos and avg neg

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
## and Second Palestinian Intifadas. Pre-print: http://web.mit.edu/hjackson/www/
## The_NYT_Distorts_the_Palestinian_Struggle.pdf.
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

    pos_score = 0 # make this smaller
    neg_score = 0
    obj_score = 0
    num_words = 0

    for tup in tagged:
        new_tag = get_wordnet_pos(tup[1])

        words = swn.senti_synsets(tup[0], new_tag)
        list_words = list(words)
        if len(list_words) != 0:
            # print(tup[0], list_words)
            word = list_words[0]

            pos_score += word.pos_score()
            neg_score -= word.neg_score()
            obj_score += word.obj_score()
            num_words += 1

    # print(pos_score,neg_score,obj_score)
    # print('Average article objectivity rating:',obj_score/num_words)
    if num_words == 0:
        return None
    avg_pos_score = pos_score / num_words
    avg_neg_score = neg_score / num_words
    avg_obj_score = obj_score / num_words
    
    return avg_pos_score, avg_neg_score, avg_obj_score



if __name__ == "__main__":
    raw = """RIO DE JANEIRO — Brazil, a global climate leader turned environmental villain under President Jair Bolsonaro, approached the United Nations climate conference in Glasgow ready to prove it was changing course, with commitments to create a green jobs program, cut carbon emissions and curb deforestation. 
    But even as John Kerry, the U.S. climate envoy, said on Twitter that those steps added “crucial momentum” to combating climate change, environmentalists argued that the plans lacked ambition and the details that would make them credible.

    And Mr. Bolsonaro’s conspicuous absence from the summit raised questions about his commitment to the reversal.

    A week before the conference started, Mr. Bolsonaro said in an interview that he would not attend for “strategic” reasons, without clarifying. Days later, Vice President Hamilton Mourão suggested Mr. Bolsonaro wanted to shield himself from exposure.

    Mr. Bolsonaro, who took office in 2019, has overseen a surge in deforestation of the Amazon and widespread neglect of environmental regulations, which have made him the target of condemnation at home and abroad.

    If the president attends the summit, “everyone will throw rocks at him,” Mr. Mourão told reporters. Instead, he said, “there will be a robust team there with the ability to, let’s say, carry out the negotiation strategy.”

    Days before the conference, Brazil’s government announced a policy to create green jobs while preserving the country’s vast forests. Then, on Monday, Brazil committed to cutting emissions in half by 2030, achieving carbon neutrality by 2050 and ending illegal deforestation by 2028, a step up from its pledge last year.
    Climate Fwd  A new administration, an ongoing climate emergency — and a ton of news. Our newsletter will help you stay on top of it. Get it sent to your inbox.

    In a video shared in one of the summit’s side events, Mr. Bolsonaro called Brazil “a green power” and declared that “in the fight against climate change, we have always been part of the solution, not the problem.”

    On Tuesday, Brazil joined more than 100 other countries in pledging to reduce methane emissions by 30 percent by 2030. It has historically resisted making such a commitment because most of its methane is discharged by the farming sector, a major driver of the Brazilian economy.
    Editors’ Picks
    The Manhattan ‘Madam’ Who Hobnobbed With the City’s Elite
    Can’t. Stop. Self-Swabbing.
    Should I Tell a Facebook Friend I Had an Affair With Her Partner?
    Continue reading the main story

    Still, Mr. Bolsonaro’s absence goes against the argument that Brazil is reversing course, said Natalie Unterstell, the president of the Institute Talanoa, a climate policy think tank.

    “It’s a big contradiction,” she said. “At the moment when he should be confirming that he wants to be more ambitious about climate issues, he isn’t present.”"""
    print(sentinet_scorer(raw))