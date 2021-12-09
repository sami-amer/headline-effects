"""
plots the data
"""


import matplotlib as plot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def plot_scores(npy_file, name):
    
    scores = np.load(npy_file, allow_pickle= True)
    similarity_scores, obj_ratios, headline_obj, article_obj, headline_pos, article_pos, headline_neg, article_neg = ([] for i in range(8))

    for article in scores:
        headline_obj.append(article['headline_score'][2])
        article_obj.append(article['article_score'][2])
        obj_ratios.append(article['article_score'][2]/article['headline_score'][2])
        
        similarity_scores.append(article['similarity_score'])
        
        headline_pos.append(article['headline_score'][0])
        article_pos.append(article['article_score'][0])

        headline_neg.append(article['headline_score'][1])
        article_neg.append(article['article_score'][1])
    
    headline_obj = np.array(headline_obj)
    article_obj = np.array(article_obj)
    obj_ratios = np.array(obj_ratios)
    
    similarity_scores = np.array(similarity_scores)

    headline_pos = np.array(headline_pos)
    article_pos = np.array(article_pos)
    
    headline_neg = np.array(headline_neg)
    article_neg = np.array(article_neg)

    tonal_difference = abs(headline_pos - article_pos) + abs(headline_neg - article_neg)
    obj_diff = abs(headline_obj - article_obj)

    # * Plots similarity versus objectivtiy ratios
    # fig, ax = plt.subplots()
    # ax.scatter(similarity_scores, obj_ratios, s = .75)
    # ax.set_xlabel("Similarity Score")
    # ax.set_ylabel("Objectivity Ratio")
    # fig.savefig(f"{name}_results_obj_ratio.png")

    # * Plots similarity verusus article objectivity
    # fig, ax = plt.subplots()
    # ax.scatter(similarity_scores, article_obj, s = .75)
    # ax.set_xlabel("Similarity Score")
    # ax.set_ylabel("Article Objectivity")
    # fig.savefig(f"{name}_results_article_obj.png")

    # * Plots similarity scores versus headline objectivity 
    # fig, ax = plt.subplots()
    # ax.scatter(similarity_scores, headline_obj, s = .75)
    # ax.set_xlabel("Similarity Score")
    # ax.set_ylabel("Headline Objectivity")
    # fig.savefig(f"{name}results_headline_obj.png")

    # * Plots the similarity versus objectivity of articles and headline, with an arrow ponting from headline to article
    # fig, ax = plt.subplots()
    # ax.quiver(similarity_scores, headline_obj,np.zeros(np.shape(similarity_scores)), article_obj - headline_obj)
    # ax.set_xlabel("Similarity Score")
    # ax.set_ylabel("Objectivity")
    # ax.set(ylim=(0, 1.05))
    # fig.savefig(f"{name}_results_obj_ratio.png")

    # * Plots headline objectivity versus article objectivity
    # fig, ax = plt.subplots()
    # ax.scatter(headline_obj, article_obj, s=.75)
    # ax.set(xlim=(0, 1), ylim=(0, 1))
    # ax.set_xlabel("Headline Obj")
    # ax.set_ylabel("Article Obj")
    # fig.savefig(f"{name}_results_obj_ratio.png")

    # ! important
    # * Plots the tonal difference versus objectivity of articles and headline, with an arrow ponting from headline to article
    # fig, ax = plt.subplots()
    # ax.quiver(tonal_difference, headline_obj,np.zeros(np.shape(tonal_difference)), article_obj - headline_obj)
    # ax.set_xlabel("Tonal Difference")
    # ax.set_ylabel("Objectivity")
    # ax.set(ylim=(0, 1.05))
    # fig.savefig(f"{name}.png")

    # * Plots the positivity versus negativity of articles and headlines, with an arrow pointing from headline to article
    # fig, ax = plt.subplots()
    # ax.quiver(headline_pos, headline_neg, article_pos - headline_pos, article_neg - headline_neg)
    # ax.set_xlabel("Positivity")
    # ax.set_ylabel("Negativity")
    # # ax.set(ylim=(0, 1.05))
    # fig.savefig(f"{name}.png")

    #! Maybe linear regression on this?
    # * Plots tonal difference versus objectivity difference
    fig, ax = plt.subplots()
    ax.scatter(tonal_difference, obj_diff, s=.75)
    # ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.set_xlabel("Tonal Difference")
    ax.set_ylabel("Objectvity Difference")
    fig.savefig(f"{name}.png")


if __name__ == "__main__":
    plot_scores("data/npy_files/run_2_all_200305.npy","tonal_vs_obj")
    # ? Redo similarity score 
    # ?     Compare it on positive and negative sentiment
    # ?     Tone similarity ?