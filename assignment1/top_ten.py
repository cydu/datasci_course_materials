import sys
import re
import json

def process(tweet_file):
    tags = {}
    for line in tweet_file:
        try:
            tweet = json.loads(line)
            for tag in tweet['entities']['hashtags']:
                if tag['text'] not in tags:
                    tags[tag['text']] = 0
                tags[tag['text']] += 1
        except:
            pass

    for k, v in sorted(tags.iteritems(), key=lambda x:x[1], reverse=True)[0:10]:
        print k, v

def main():
    tweet_file = open(sys.argv[1])
    process(tweet_file)

if __name__ == '__main__':
    main()
