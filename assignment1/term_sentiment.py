import sys
import json

def get_sent_dict_from_file(fname):
    scores = {}
    with open(fname) as sent_file:
        for line in sent_file:
            term, score = line.split('\t')
            scores[term] = int(score)
    return scores

def get_english_tweet_texts(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            j = json.loads(line)
            if "lang" in j and j["lang"] == "en":
                try:
                    yield json.loads(line)['text']
                except KeyError:
                    pass

def get_english_tweet_texts_not_from_json(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            yield line.strip()

def get_sent_of_tweet(sent_dict, tweet):
    return sum(sent_dict.get(word.lower(), 0) for word in tweet.split())

def main():
    sent_dict = get_sent_dict_from_file(sys.argv[1])
    tweet_texts = get_english_tweet_texts(sys.argv[2])

    new_sents = {}

    for tweet in tweet_texts:
        sent = get_sent_of_tweet(sent_dict, tweet)
        for term in tweet.split():
            if term in sent_dict:
                continue
            elif term in new_sents:
                new_sents[term].append(sent)
            else:
                new_sents[term] = [sent]

    for term, sents in new_sents.iteritems():
        print term, sum(sents) / float(len(sents))

if __name__ == '__main__':
    main()
