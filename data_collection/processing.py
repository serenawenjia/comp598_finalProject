import os
import sys
import json

print("Usage: python3 processing.py input_json_path [number_to_keep]")
IFILE = sys.argv[1]
NUM = None
if len(sys.argv) == 3:
    NUM = int(sys.argv[2])

res = []
with open(IFILE) as ifile:
    data = json.load(ifile)
    print('Processing', len(data), 'tweets')
    
    if NUM is None:
        NUM = len(data)
    
    print('Keeping', NUM, 'tweets')

    for index, post in enumerate(data):
        if index >= NUM:
            break
        if post['place']['country_code'] != 'CA':
            print(post['id'], 'is not in Canada')
            continue
        if post['lang'] != 'en':
            print(post['id'], 'is not in English')
            continue
        res.append({
            'id' : post['id'],
            'created_at' : post['created_at'],
            'full_text' : post['full_text'],
            'category' : '',
            'sentiment' : ''
        })

with open(IFILE[:-5] + "_processed_" + str(NUM) + ".json", 'w') as ofile:
    json.dump(res, ofile, indent=4)