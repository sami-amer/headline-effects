"""
Plots the data
"""

# lib
import matplotlib as plot
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pylab
import numpy as np
from pylab import *


def plot_scores(npy_file, name):
    """
    Takes the .npy file we generate from out data, and plots and saves the figures.  
    There are no switches - you must uncomment whichever plot you want to run
    """
    scores = np.load(npy_file, allow_pickle= True)
    similarity_scores, obj_ratios, headline_obj, article_obj, headline_pos, article_pos, headline_neg, article_neg = ([] for i in range(8))
    
    counter = 0
    for article in scores:
        # if counter == 1250:
        #     break
        headline_obj.append(article['headline_score'][2])
        article_obj.append(article['article_score'][2])
        obj_ratios.append(article['article_score'][2]/article['headline_score'][2])
        
        similarity_scores.append(article['similarity_score'])
        
        headline_pos.append(article['headline_score'][0])
        article_pos.append(article['article_score'][0])

        headline_neg.append(article['headline_score'][1])
        article_neg.append(article['article_score'][1])
        counter +=1
    
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
    colors = []
    cmap = cm.get_cmap('gist_rainbow',100)
    
    print("Tonal Diff: ", np.mean(tonal_difference), np.std(tonal_difference))
    print("Obj Diff: ", np.mean(obj_diff), np.std(obj_diff))
    print("headline_obj: ", np.mean(headline_obj), np.std(headline_obj))

    for od in obj_diff:
        ind = int(od*100)
        rgba = cmap(ind)
        colors.append(matplotlib.colors.rgb2hex(rgba))
    colors = np.array(colors)

    # This code block generates the string to paste into WebPPL
    # ------------------------------------------------------------------------------------------------------------------------------
    # output = []
    # for tDiff,hObj,oDiff,color in zip(tonal_difference, headline_obj, obj_diff,colors):
    #     output.append({"tonal_difference":round(tDiff,4), "headline_obj":round(hObj,4), "obj_diff":round(oDiff,4), "color": color})
    # # print(output)
    # newCounter = 0
    # with open("webppl_data.txt", "w+") as f: # needs this to break every 10000 characters
    #     f.write('[\n')
    #     for item in output:
    #         if newCounter == 1500:
    #             break
    #         f.write(str(item)+",\n")
    #         newCounter +=1
    #     f.write("]")
    # ------------------------------------------------------------------------------------------------------------------------------

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

    # * Plots the tonal difference versus objectivity of articles and headline, with an arrow ponting from headline to article
    # fig, ax = plt.subplots(dpi=300)
    # # ax.quiver(tonal_difference, headline_obj,np.zeros(np.shape(tonal_difference)), article_obj - headline_obj)
    # for i in range(len(tonal_difference)):
    #     ax.plot([tonal_difference[i], tonal_difference[i]],[headline_obj[i], article_obj[i]], color = colors[i], linewidth = 0.25, ls=(0,(5,10)))
    #     # add_arrow(line, position= tonal_difference[i] ,color="black")
    #     # ax.arrow(tonal_difference[i], article_obj[i], 0, 0.01, shape='full', lw=0, length_includes_head=True, head_width=.01)
    # # ax.scatter(tonal_difference, article_obj, s=1)
    # # ax.scatter(tonal_difference, headline_obj, s=1, c='red')
    # ax.set_xlabel("Tonal Difference")
    # ax.set_ylabel("Objectivity")
    # ax.set(ylim=(0, 1.05))
    # fig.savefig(f"{name}.png")

    # * Plots the positivity versus negativity of articles and headlines, with an arrow pointing from headline to article
    # * Colored by distance 
    # import matplotlib.colors as colors
    # fig, ax = plt.subplots()
    # dPos = article_pos - headline_pos
    # dNeg = article_neg - headline_neg
    # M = np.hypot(dPos, dNeg)
    # # print(M.mean(),np.median(M),M.max())
    # Q = ax.quiver(headline_pos, headline_neg, dPos, dNeg,M, cmap='gist_rainbow', norm=colors.LogNorm(vmin=0.1,vmax=M.max()))
    # # Q = ax.quiver(headline_pos, headline_neg, dPos, dNeg,M, cmap='viridis_r')
    # ax.set_xlabel("Positivity")
    # ax.set_ylabel("Negativity")
    # fig.colorbar(Q)
    # # ax.set(ylim=(0, 1.05))
    # # ax.set(ylim=(-.81, 0.01), xlim =(-0.01, .71))
    # ax.set(ylim=(0.01, headline_neg.min() - 0.1), xlim =(-0.01, headline_pos.max()+0.01))
    # fig.savefig(f"{name}.png",dpi = 300)

    # * Plots the positivity versus negativity of articles and headlines, with an arrow pointing from headline to article
    # * Colored by obj_ratio, linearly or Logarithmically
    # fig, ax = plt.subplots()
    # dPos = article_pos - headline_pos
    # dNeg = article_neg - headline_neg
    # M = obj_ratios
    # Q = ax.quiver(headline_pos, headline_neg, dPos, dNeg, M, cmap='viridis_r', norm = colors.LogNorm(vmin=M.min(), vmax = M.max()))
    # # Q = ax.quiver(headline_pos, headline_neg, dPos, dNeg, M, cmap='viridis_r')
    # ax.set_xlabel("Positivity")
    # ax.set_ylabel("Negativity")
    # cbar = fig.colorbar(Q)
    # # cbar.ax.set_yticklabels(['{:.0f}'.format(x) for x in np.arange(M.min(), M.max(), 1)])
    # # cbar.ax.set_yticklabels(["{:.0f}".format(i) for i in cbar.get_ticks()]) # set ticks of your format
    # cbar.set_label('obj. ratio', rotation=270, labelpad= 21)
    # ax.set(ylim=(-.81, 0.01), xlim =(-0.01, .71))
    # ax.set(ylim=(0.01, headline_neg.min() - 0.1), xlim =(-0.01, headline_pos.max()+0.01))
    # fig.savefig(f"{name}.png",dpi = 300)

    # * Plots tonal difference versus objectivity difference
    # fig, ax = plt.subplots()
    # ax.scatter(tonal_difference, obj_diff, s=.75)
    # # ax.set(xlim=(0, 1), ylim=(0, 1))
    # ax.set_xlabel("Tonal Difference")
    # ax.set_ylabel("Objectvity Difference")
    # fig.savefig(f"{name}.png")



if __name__ == "__main__":
    # name convention = plottype_x_y_coloring_extra
    name = "quiver_tonalDiff_headlineObj" # name or path/name
    plot_scores("data/npy_files/run_2_all_200305.npy",f"{name}_some_additional_name")