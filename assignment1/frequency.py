import sys
import json
import operator

def get_english_tweet_texts(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            j = json.loads(line)
            if "lang" in j and j["lang"] == "en":
                try:
                    yield json.loads(line)['text']
                except KeyError:
                    pass

def get_tweet_texts(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            try:
                yield json.loads(line)['text']
            except KeyError:
                pass

def main():
    tweet_txts = get_english_tweet_texts(sys.argv[1])

    term_freqs = {}
    total_terms = 0
    for tweet in tweet_txts:
        splt = tweet.split()
        total_terms += len(splt)
        for term in splt:
            term_freqs[term] = term_freqs.get(term, 0) + 1

    s = sorted(term_freqs.iteritems(), key=operator.itemgetter(1), reverse=True)

    for i in range(10):
        print s[i][0], s[i][1] / float(total_terms)

if __name__ == '__main__':
    main()