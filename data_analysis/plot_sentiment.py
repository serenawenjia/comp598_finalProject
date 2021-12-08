import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import json
from constants import cats

def plot_sentiment(IFILE):
    OFILE = os.getcwd() + '/' + IFILE[:-5] + '_plot.png'

    df = pd.read_json(IFILE)
    print(df)

    df = df / df.sum()
    print(df)
    
    df = df.transpose()
    print(df)

    df = df.sort_values('positive', ascending=False)
    print(df)
    
    df.plot.bar(
        xlabel='Category',
        ylabel='Percentage',
        title = 'Sentiments Percentage by Category',
        stacked = True)
    
    plt.tight_layout() # Bottom margin
    plt.savefig(OFILE)

def main():
    print(f'Usage: python3 {__file__} sentiment_count_json_path')
    
    IFILE = sys.argv[1]
    plot_sentiment(IFILE)


if __name__ == '__main__':
    main()