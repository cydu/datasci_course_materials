import sys
import re
import json

def process(tweet_file):
    words = {}
    for line in tweet_file:
        try:
            tweet = json.loads(line)
            twords = re.findall(r"[a-zA-Z]+",tweet['text'])
            for w in [w.lower() for w in twords]:
                if w not in words:
                    words[w] = 0
                words[w] += 1
        except:
            pass

    total = sum([v for k, v in words.iteritems()])
    for k, v in words.iteritems():
        print k, v * 1.0 / total

def main():
    tweet_file = open(sys.argv[1])
    process(tweet_file)

if __name__ == '__main__':
    main()
