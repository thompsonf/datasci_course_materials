import sys
import json

def get_tweet_texts(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            try:
                yield json.loads(line)['text']
            except KeyError:
                pass

def main():
    tweet_txts = get_tweet_texts(sys.argv[1])

    term_freqs = {}
    total_terms = 0
    for tweet in tweet_txts:
        splt = tweet.split()
        total_terms += len(splt)
        for term in splt:
            term_freqs[term] = term_freqs.get(term, 0) + 1

    for term, freq in term_freqs.iteritems():
        print term, float(freq) / total_terms

if __name__ == '__main__':
    main()