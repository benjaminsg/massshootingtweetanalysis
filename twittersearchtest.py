from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['mass shooting']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    tso.set_count(20)

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'REDACTED',
        consumer_secret = 'REDACTED',
        access_token = 'REDACTED',
        access_token_secret = 'REDACTED'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        #filter retweets
        if(tweet['in_reply_to_status_id'] != None):
            #filter replies
            if(not '@' in tweet['text']):
                print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
