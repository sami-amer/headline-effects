"""
Computes the semantic similarity between two pieces of text using GLoVe embeddings and 
"""


from re import L
import torch
import torchtext

from helpers.sentinet_scorer import preprocess

glove = torchtext.vocab.GloVe(name="6B", dim=50)   # embedding size = 100


def compute_semantic_similarity(headline_text, article_text):
    """
    Computes the semantic similarity between two pieces of text by averaging their GLoVe eulcidean distance

        Arguments:
            headline_text (str): headline text as a plain cleaned string
            article_text  (str): article text as a plain cleaned string
        
        Returns:
            tuple of (semantic similarity score, lenght of headline and length of article)
    """
    
    headline = preprocess(headline_text)
    article = preprocess(article_text)

    headline_similarity = [0] * len(headline)
    for i in range(len(headline)):
        headline_word = headline[i]
        article_similarity = [0] * len(article)
        for j in range(len(article)):
            article_word = article[j]
            article_similarity[j] = torch.norm(glove[headline_word] - glove[article_word]).item() # euclidean distance
        headline_similarity[i] = sum(article_similarity) / len(article)
    semantic_similartiy = sum(headline_similarity) / len(headline)

    return semantic_similartiy, (len(headline), len(article))
