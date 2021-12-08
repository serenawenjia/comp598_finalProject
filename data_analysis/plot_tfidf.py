import matplotlib.pyplot as plt
import os
import sys
import json
from constants import cats

def plot_tfidf(IFILE):
    os.makedirs(os.getcwd() + '/' + IFILE[:-5] + '_plots/', exist_ok=True)
    with open(IFILE) as ifile:
        mp = json.load(ifile)
        for index, cat in enumerate(cats):
            # if index > 0:
            #     break
            OFILE = os.getcwd() + '/' + IFILE[:-5] + '_plots/' + cat + '.png'
            # print(mp[cat]) 
            x = [p[0] for p in mp[cat]]
            y = [p[1] for p in mp[cat]]
            print(x)
            print(y)
            plt.bar(x, y)
            plt.xticks(rotation=90)
            plt.xlabel('word')
            plt.ylabel('tf-idf')
            plt.title(f'Top 10 words in category "{cat}" with the highest tf-idf')
            # plt.ylim(0, 25)
            plt.tight_layout() # Bottom margin
            plt.savefig(OFILE)
            plt.clf()
            # plt.show()

def main():
    print(f'Usage: python3 {__file__} tfidf_json_path')
    
    IFILE = sys.argv[1]
    plot_tfidf(IFILE)


if __name__ == '__main__':
    main()