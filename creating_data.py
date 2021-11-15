# Step 1: Get the data
import torch
from torchtext.datasets import AG_NEWS


train_iter = AG_NEWS(split= 'train') # gets the training split

from torchtext.data.utils import get_tokenizer # gets the tokenizer
from torchtext.vocab import build_vocab_from_iterator # builds the vocabulary from the training data

tokenizer = get_tokenizer("basic_english") # gets the basic english tokenizer
train_iter = AG_NEWS(split= 'train') # gets the training split

def yield_tokens(data_iter): # a generator that yields tokens from the data
    for _, text in data_iter:
        yield tokenizer(text)

vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<unk>"]) # builds the vocabulary from the training data
vocab.set_default_index(vocab["<unk>"]) # sets the default index to the unknown token



# These create a pipeline to make it easy to process the data
text_pipeline = lambda x: vocab(tokenizer(x))
label_pipeline = lambda x: int(x) - 1
print(text_pipeline('A test of the vocab'))