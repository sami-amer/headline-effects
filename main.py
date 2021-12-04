"""
add docs
"""

from helpers import glove_semantic_similarity, sentinet_scorer, plotter
from concrete.util import CommunicationReader
from pathlib import Path


def import_data(input_file):
    for (comm, filename) in CommunicationReader(input_file):
        name = comm.id
        all_text = comm.text.split('\n')
        headline_text = all_text[0] # make sure to grab headline as well
        article_text = (' ').join(all_text[1:]) # get article text
    
    return headline_text, article_text, name

def main(files):
    text = [] # make this a list of tuples
    for file in files:
        pass

if __name__ == "__main__":
    # main()
    p_2003 = Path("data/200305/")
    p_2006 = Path("data/20060/")
    
    files_2003 = p_2003.glob("*")
    files_2006 = p_2006.glob("*")

    # import_data(files_2003[0])

    # with open("chosen_2003.txt","w+") as f:
    #     for file in files_2003:
    #         headline, article, name = import_data(file)
    #         if len(article) > 300:
    #             f.write(name+"\n")

    names = []
    
    with open("chosen_2003.txt", "r") as f:
        for line in f:
            names.append(line.strip('\n'))
    names.sort()
    print(names)