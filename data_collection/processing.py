import tweepy
import json
import os
from dotenv import load_dotenv
import sys

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth) # API for V1.1

print("Usage: python3 processing.py input_json_path [start_row end_row]")
IFILE = sys.argv[1]
START = None
END = None
if len(sys.argv) == 4:
    START = int(sys.argv[2])
    END = int(sys.argv[3])

res = []
with open(IFILE) as ifile:
    data = json.load(ifile)
    print('Processing', len(data), 'tweets')
    
    if START is None:
        START = 1
    if END is None:
        END = len(data)

    print('Keeping tweets from row', START, 'to row', END)

    for index, post in enumerate(data):
        if index + 1 < START or index + 1 > END:
            continue
        if post['lang'] != 'en':
            print(post['id'], 'is not in English')
            continue
        
        full_text = post['full_text']
        if post['is_quote_status']:
            full_text += '\n' + post['quoted_status']['full_text']

        try:
            if post['in_reply_to_status_id']:
                original = api.get_status(post['in_reply_to_status_id'])._json
                full_text += '\n' + original['text']
        except Exception as e:
            print(f"Failed to retrieve original for row {index} (tweet id {post['id']}). Only keeping reply text. Error message:\n{str(e)}")

        res.append({
            'row' : index + 1,
            'id' : post['id'],
            'created_at' : post['created_at'],
            'full_text' : full_text,
            'category' : '',
            'sentiment' : ''
        })

with open(f"{IFILE[:-5]}_processed_{START}_{END}.json", 'w') as ofile:
    json.dump(res, ofile, indent=4)