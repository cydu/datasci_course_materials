import sys
import traceback
import re
import json

def get_state(tweet):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    try: 
        for k, v in states.iteritems():
            lv = v.lower()
            if lv in tweet['place']['full_name'].lower():
                return k
            if lv in tweet['user']['location'].lower():
                return k
    except:
        pass
    return None

def process(sent_file, tweet_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    
    states = {'CA': 0}
    
    for line in tweet_file:
        score = 0
        try:
            tweet = json.loads(line)
            state = get_state(tweet)
            if state == None:
                continue
            words = re.findall(r"[a-zA-Z]+",tweet['text'])
            score = sum([scores.get(w.lower(), 0) for w in words])

            if state not in states:
                states[state] = 0
            states[state] += 1 and score > 0 or -1
        except:
            #print traceback.print_exc()
            pass

    for s in [k for k, v in sorted(states.iteritems(), key=lambda x: x[1], reverse=True)][0:1]:
        print s

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    process(sent_file, tweet_file)

if __name__ == '__main__':
    main()
