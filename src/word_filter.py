import src.blocked_words as blocked





def isBadWord(tweet):
    bad_words = blocked.blockedWordList()
    test = False



    for word in bad_words:
        tweet = tweet.lower()
        if word in tweet:
            test = True
    return test