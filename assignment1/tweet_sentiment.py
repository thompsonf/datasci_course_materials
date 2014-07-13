import sys
import json

def get_sent_dict_from_file(fname):
    scores = {}
    with open(fname) as sent_file:
        for line in sent_file:
            term, score = line.split('\t')
            scores[term] = int(score)
    return scores

def get_sent_of_tweet(sent_dict, tweet):
    return sum(sent_dict.get(word.lower(), 0) for word in tweet.split())

def get_tweet_texts(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            try:
                yield json.loads(line)['text']
            except KeyError:
                pass

def main():
    sent_dict = get_sent_dict_from_file(sys.argv[1])
    tweet_txts = get_tweet_texts(sys.argv[2])
    for tweet in tweet_txts:
        print get_sent_of_tweet(sent_dict, tweet)

if __name__ == '__main__':
    main()
