import pandas as pd

df = pd.DataFrame([
    ['my name is Jack', 'Y'],
    ['Hi I am Jack', 'Y'],
    ['Hello There!', 'Y'],
    ['Hi I am cooking', 'N'],
    ['Hello are you there?', 'N'],
    ['There is a bird there', 'N'],
], columns=['text', 'label'])

from torchtext.legacy.data import Field
from torchtext.vocab import GloVe
embedding_glove = GloVe(name='6B', dim=100)
text_field = Field(
    tokenize = 'basic_english',
    lower = True
)

label_fields = Field(sequential = False, use_vocab = False)

preprocessed_text = df['text'].apply(lambda x: text_field.preprocess(x))
text_field.build_vocab(
    preprocessed_text, 
    vectors='glove.6B.300d'
)
vocab = text_field.vocab

# vocab.vectors
print(vocab['are']) # unknown tokens are 0, padding tokens are 1