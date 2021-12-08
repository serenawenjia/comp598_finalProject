# Data Collection for COMP598 Final Project

## Setup

1. Create environment: `python3 -m venv env`
1. Activate environment: `source env/bin/activate`
1. Install dependencies: `pip3 install -r requirements.txt`

## How to Run

1. Activate environment: `source env/bin/activate`
1. To produce word counts: `python3 count_words.py annotated_json_path`
1. To produce tf-idf: `python3 compute_tfidf.py word_counts_json_path`
1. To produce sentiments counts: `python3 count_sentiments.py annotated_json_path`
1. To plot tf-idf: `python3 plot_tfidf.py tfidf_json_path`
1. To plot sentiments: `python3 plot_sentiment.py sentiment_counts_json_path` 
