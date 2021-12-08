import pandas as pd
import os
import sys
import json
from constants import cats

def count_words(IFILE):
    stopwords = ['a','about','above','across','after','again','against','all','almost','alone','along','already','also','although','always','among','an','and','another','any','anybody','anyone','anything','anywhere','are','area','areas','around','as','ask','asked','asking','asks','at','away','b','back','backed','backing','backs','be','became','because','become','becomes','been','before','began','behind','being','beings','best','better','between','big','both','but','by','c','came','can','cannot','case','cases','certain','certainly','clear','clearly','come','could','d','did','differ','different','differently','do','does','done','down','down','downed','downing','downs','during','e','each','early','either','end','ended','ending','ends','enough','even','evenly','ever','every','everybody','everyone','everything','everywhere','f','face','faces','fact','facts','far','felt','few','find','finds','first','for','four','from','full','fully','further','furthered','furthering','furthers','g','gave','general','generally','get','gets','give','given','gives','go','going','good','goods','got','great','greater','greatest','group','grouped','grouping','groups','h','had','has','have','having','he','her','here','herself','high','high','high','higher','highest','him','himself','his','how','however','i','if','important','in','interest','interested','interesting','interests','into','is','it','its','itself','j','just','k','keep','keeps','kind','knew','know','known','knows','l','large','largely','last','later','latest','least','less','let','lets','like','likely','long','longer','longest','m','made','make','making','man','many','may','me','member','members','men','might','more','most','mostly','mr','mrs','much','must','my','myself','n','necessary','need','needed','needing','needs','never','new','new','newer','newest','next','no','nobody','non','noone','not','nothing','now','nowhere','number','numbers','o','of','off','often','old','older','oldest','on','once','one','only','open','opened','opening','opens','or','order','ordered','ordering','orders','other','others','our','out','over','p','part','parted','parting','parts','per','perhaps','place','places','point','pointed','pointing','points','possible','present','presented','presenting','presents','problem','problems','put','puts','q','quite','r','rather','really','right','right','room','rooms','s','said','same','saw','say','says','second','seconds','see','seem','seemed','seeming','seems','sees','several','shall','she','should','show','showed','showing','shows','side','sides','since','small','smaller','smallest','so','some','somebody','someone','something','somewhere','state','states','still','still','such','sure','t','take','taken','than','that','the','their','them','then','there','therefore','these','they','thing','things','think','thinks','this','those','though','thought','thoughts','three','through','thus','to','today','together','too','took','toward','turn','turned','turning','turns','two','u','under','until','up','upon','us','use','used','uses','v','very','w','want','wanted','wanting','wants','was','way','ways','we','well','wells','went','were','what','when','where','whether','which','while','who','whole','whose','why','will','with','within','without','work','worked','working','works','would','x','y','year','years','yet','you','young','younger','youngest','your','yours','z']
    mp = {cat: {} for cat in cats}
    # mp['__ALL__'] = {}

    df = pd.read_json(IFILE)
    to_replace = '()[],-.?!:;#&' # TODO: improve filter
    trans = str.maketrans(to_replace, ' ' * len(to_replace)) 

    for index, row in df.iterrows():
        # if index > 100: # DEBUG
        #     break
        cat = row['category'].lower()
        if cat not in cats: 
            print('unknown category', cat, 'in row', index + 1)
            continue

        # remove http links
        lst = [word for word in row['full_text'].lower().split() if 'http' not in word]

        # split by punctuation
        lst = [word for segment in lst for word in segment.translate(trans).split()]

        # remove non-alphanumerical
        lst = [word for word in lst if word.isalpha()]

        # stopword
        lst = [word for word in lst if word not in stopwords]

        for word in lst:
            if word not in mp[cat]:
                mp[cat][word] = 0
            # if word not in mp['__ALL__']:
            #     mp['__ALL__'][word] = 0

            mp[cat][word] += 1
            # mp['__ALL__'][word] += 1

    return mp

def main():
    print(f'Usage: python3 {__file__} annotated_tweets_json_path')
    
    IFILE = sys.argv[1]
    OFILE = os.getcwd() + '/' + IFILE[:-5] + '_word_counts.json'

    mp = count_words(IFILE)

    os.makedirs(os.path.dirname(OFILE) or '.', exist_ok=True)
    with open(OFILE, 'w') as ofile:
        json.dump(mp, ofile, indent=4)

if __name__ == '__main__':
    main()