import sys
import json
import operator

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

def get_sent_dict_from_file(fname):
    scores = {}
    with open(fname) as sent_file:
        for line in sent_file:
            term, score = line.split('\t')
            scores[term] = int(score)
    return scores

def get_sent_of_tweet(sent_dict, tweet):
    try:
        return sum(sent_dict.get(word.lower(), 0) for word in tweet['text'].split())
    except KeyError:
        pass

def get_state_from_tweet(tweet):
    try:
        loc = tweet['user']['location']
        loc_words = [word.strip(' ,.\t\n') for word in loc.split()]
        for word in loc_words:
            if word.upper() in states:
                return word.upper()
    except KeyError:
        pass

def get_english_tweets(fname):
    with open(fname) as tweet_file:
        for line in tweet_file:
            j = json.loads(line)
            if "lang" in j and j["lang"] == "en":
                yield j

def get_sent_and_state(sent_dict, tweet):
    sent = get_sent_of_tweet(sent_dict, tweet)
    state = get_state_from_tweet(tweet)
    if sent is not None and state is not None:
        return sent, state

def main():
    state_sents = {}

    sent_dict = get_sent_dict_from_file(sys.argv[1])
    tweets = get_english_tweets(sys.argv[2])
    for tweet in tweets:
        ret = get_sent_and_state(sent_dict, tweet)
        if ret is not None:
            sent, state = ret
            if state in state_sents:
                state_sents[state].append(sent)
            else:
                state_sents[state] = [sent]
    state_happiness = {state: sum(sents) / float(len(sents)) for state, sents in state_sents.iteritems()}
    happiest_state = max(state_happiness.iteritems(), key=operator.itemgetter(1))[0]
    print happiest_state

if __name__ == '__main__':
    main()