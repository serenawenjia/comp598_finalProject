import pandas as pd
import os
import json
import sys
import math
from constants import cats

def calc_tfidf(IFILE, NUM):
    tfidf = {cat: {} for cat in cats}

    usage_mp = {} # word -> how many categories used this word
    res = {}
    with open(IFILE) as ifile:
        mp = json.load(ifile)
        for cat in cats:
            for w, cnt in mp[cat].items():
                if w not in usage_mp:
                    usage_mp[w] = 0
                usage_mp[w] += 1

        for cat in cats:
            for w, cnt in mp[cat].items():
                tfidf[cat][w] = cnt * math.log10(len(cats) / usage_mp[w])

        for cat in cats:
            sorted_pairs = sorted(tfidf[cat].items(), key=lambda kv: kv[1], reverse=True)[:NUM]
            # res[cat] = [pair[0] for pair in sorted_pairs]
            res[cat] = sorted_pairs

    return res

def main():
    print(f'Usage: python3 {__file__} word_counts_json_path')

    NUM = 10
    IFILE = sys.argv[1]
    OFILE = os.getcwd() + '/' + IFILE[:IFILE.find('_')] + '_tfidf.json'

    mp = calc_tfidf(IFILE, NUM)
    os.makedirs(os.path.dirname(OFILE) or '.', exist_ok=True)
    with open(OFILE, 'w') as ofile:
        json.dump(mp, ofile, indent=4)

if __name__ == '__main__':
    main()
