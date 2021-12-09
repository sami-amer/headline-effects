"""
add docs
"""

from tarfile import REGULAR_TYPES
from typing import List
from numpy.lib.npyio import save
from helpers import glove_semantic_similarity, sentinet_scorer, plotter
from concrete.util import CommunicationReader
from pathlib import Path
import numpy as np
from tqdm import tqdm

def import_data(input_file):
    
    for (comm, filename) in CommunicationReader(input_file):
        name = comm.id
        all_text = comm.text.split('\n')
        headline_text = all_text[0] # make sure to grab headline as well
        article_text = (' ').join(all_text[1:]) # get article text
    
    return headline_text, article_text, name, len(headline_text), len(article_text)

def score(files, save_name):
    
    # scores = ["name", "headline", "headline_score", "article_score", "similarity score", "full_lengths", "cleaned_lengths"]
    scores = []
    
    for file in tqdm(files):
        input_data = import_data(file)
        if len(sentinet_scorer.preprocess(input_data[0])) < 2 or len(sentinet_scorer.preprocess(input_data[1])) < 2:
            continue 
        headline_text = input_data[0]
        article_text = input_data[1]
        # print(headline_text)
        # print(article_text)

        swn_scores = (sentinet_scorer.sentinet_scorer(headline_text),sentinet_scorer.sentinet_scorer(article_text))
        if not swn_scores[0] or not swn_scores[1]:
            continue
        similarity_score, new_lengths = glove_semantic_similarity.compute_semantic_similarity(headline_text, article_text)

        
        # scores.append([input_data[2],headline_text,swn_scores[0],swn_scores[1],similarity_score,(input_data[3], input_data[4]),(len(headline_text),len(article_text))])
        scores.append({
            "name" : input_data[2],
            "headline" : headline_text,
            "headline_score": swn_scores[0],
            "article_score": swn_scores[1],
            "similarity_score": similarity_score,
            "full_lengths": (input_data[3], input_data[4]),
            "cleaned_lengths":(new_lengths[0],new_lengths[1])
        })

    # print(scores)
    
    scores_array = np.array(scores)
    # print(scores_array)

    np.save(save_name,scores_array)

def filter_files(path_to_data: Path, target_count: int, target_length_min: int):
    
    files = path_to_data.glob("*")
    filtered_files = []

    counter = 0
    target = target_count

    for file in tqdm(files):
        headline_text, article_text, name, len_headline, len_article = import_data(file)
        if len_article > target_length_min:
            counter += 1
            files.append(file)
        if counter >= target:
            break

    return filtered_files





if __name__ == "__main__":
    # main()
    p_2003 = Path("data/200305/")
    p_2006 = Path("data/20060/")
    
    # files_2003 = p_2003.glob("*")
    # files_2006 = p_2006.glob("*")

    # import_data(files_2003[0])
    # files = []
    
    # with open("chosen_2003.txt","w+") as f:
    #     counter  = 0
    #     target = 15000
    #     for file in tqdm(files_2003):
    #         headline_text, article_text, name, len_headline, len_article = import_data(file)
    #         if len_article > 1000:
    #             f.write(name+"\n")
    #             counter += 1
    #             files.append(file)
    #         if counter >= target:
    #             break
    files = filter_files(p_2003)
    score(files,"run_2_15000.npy")
    # print(files)
    # print(import_data(files[0]))
    
    # names.sort()
    # print(names)