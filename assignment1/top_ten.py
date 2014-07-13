import sys
import json
import operator

def get_hashtags(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            try:
                j = json.loads(line)
                hashtags = j['entities']['hashtags']
                if hashtags:
                    yield hashtags
            except KeyError:
                pass

def main():
    hashtag_counts = {}
    hashtags = get_hashtags(sys.argv[1])
    for h_list in hashtags:
        for h in h_list:
            h_txt = h['text']
            hashtag_counts[h_txt] = hashtag_counts.get(h_txt, 0) + 1
    top_hts = sorted(hashtag_counts.iteritems(), key=operator.itemgetter(1))[:10]
    for ht, count in top_hts:
        print ht, count

if __name__ == '__main__':
    main()