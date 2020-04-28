import requests
import json
import config

endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/testing.json" 

headers = {"Authorization":"Bearer " + config.bearer_token, "Content-Type": "application/json"}  

data = '{"query":"fear mass shooting", "fromDate": "201212020000", "toDate": "201301240000"}'

response = requests.post(endpoint,data=data,headers=headers).json()

results = response['results']

#print(results[1].keys())

for tweet in results:
    if(tweet['in_reply_to_status_id'] != None):
        #filter replies
        #if(not '@' in tweet['text']):
        print( '@%s tweeted: %s [at time : %s]' % ( tweet['user']['screen_name'], tweet['text'], tweet['created_at'] ) )

#print(jso.dumps(response, indent = 2))