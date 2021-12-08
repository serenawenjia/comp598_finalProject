import pandas as pd
import os
import sys
import json
from constants import cats, sents

def count_sentiments(IFILE):
    mp = {cat: {sent: 0 for sent in sents} for cat in cats}
    
    df = pd.read_json(IFILE)

    for index, row in df.iterrows():
        # if index > 100: # DEBUG
        #     break
        cat = row['category'].lower()
        if cat not in cats: 
            print('unknown category', cat, 'in row', index + 1)
            continue

        sent = row['sentiment'].lower()
        if sent not in sents: 
            print('unknown sentiment', sent, 'in row', index + 1)
            continue

        mp[cat][sent] += 1

    return mp

def main():
    print(f'Usage: python3 {__file__} annotated_tweets_json_path')
    
    IFILE = sys.argv[1]
    OFILE = os.getcwd() + '/' + IFILE[:-5] + '_sentiment_counts.json'

    mp = count_sentiments(IFILE)

    os.makedirs(os.path.dirname(OFILE) or '.', exist_ok=True)
    with open(OFILE, 'w') as ofile:
        json.dump(mp, ofile, indent=4)

if __name__ == '__main__':
    main()