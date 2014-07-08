# -*- coding: utf-8 -*-
import sys
import json
import re

def process(sent_file, tweet_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    
    for line in tweet_file:
        score = 0
        try:
            tweet = json.loads(line)
            words = re.findall(r"[a-zA-Z]+",tweet['text'])
            score = sum([scores.get(w.lower(), 0) for w in words])
        except:
            pass
        print score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    process(sent_file, tweet_file)

if __name__ == '__main__':
    main()
