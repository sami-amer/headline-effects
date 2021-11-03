import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tree import bracket_parse
# nltk.download('sentiwordnet')
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet

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
tokens = word_tokenize(raw)
tagged = pos_tag(tokens)
# print(tagged)
pos_score = 0
neg_score = 0
obj_score = 0
for tup in tagged:
    new_tag = get_wordnet_pos(tup[1])
    try:
        breakdown = swn.senti_synset(tup[0]+'.'+new_tag+'.'+'01')
        neg_score -= breakdown.neg_score()
        pos_score += breakdown.pos_score()
        obj_score += breakdown.obj_score()
    except nltk.corpus.reader.wordnet.WordNetError:
        # print('error')
        pass
print(pos_score,neg_score,obj_score)

# text = nltk.Text(tokens)
# breakdown = swn.senti_synset(tagged)
# print(breakdown)