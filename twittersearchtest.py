from TwitterSearch import *
import config
try:
    tso = TwitterSearchOrder()
    #set list of keywords to search for 
    tso.set_keywords(['Sandy Hook'])
    #specify tweet language as english
    tso.set_language('en')
    #do not include entity info
    tso.set_include_entities(False)
    #set number of tweets to get
    tso.set_count(20)

    # create a TwitterSearch object with tokens
    ts = TwitterSearch(
        consumer_key = config.consumer_key,
        consumer_secret = config.consumer_secret,
        access_token = config.access_token,
        access_token_secret = config.access_token_secret
     )

    tweetcount = 0
    
     # get tweets
    for tweet in ts.search_tweets_iterable(tso):
        #filter retweets
        if(tweet['in_reply_to_status_id'] != None):
            #filter replies
            #if(not '@' in tweet['text']):
            #print( '@%s tweeted: %s [at time : %s]' % ( tweet['user']['screen_name'], tweet['text'], tweet['created_at'] ) )
            tweetcount += 1
    
    print(tweetcount)

#handle errors if they exist
except TwitterSearchException as e:
    print(e)
