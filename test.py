print 'Hello'
print 'second Hello'

from twitter import *
from twython import *

#this one for pyhton twitter
api = Api(consumer_key='FuKwQ2LurDxvmn9r74KfJghbR',
                  consumer_secret='LbZCi5yWyRolOwgHPFWixU4GBqbUVlH1XvYLFd1G2mogVJZ9Jn',
                  access_token_key='138568005-tTQWxv7OR77TdlSEcwuDMKctXShQoSCs4ZAlKGja',
                  access_token_secret='25WCsQyzoeQVlmrrMDXtR1bbSg7TU5kfLcMJ0KUkakVd3')

#this one for twython
api = Twython('FuKwQ2LurDxvmn9r74KfJghbR',
            app_secret='LbZCi5yWyRolOwgHPFWixU4GBqbUVlH1XvYLFd1G2mogVJZ9Jn',
            oauth_token='138568005-tTQWxv7OR77TdlSEcwuDMKctXShQoSCs4ZAlKGja',
            oauth_token_secret='25WCsQyzoeQVlmrrMDXtR1bbSg7TU5kfLcMJ0KUkakVd3')



print api.VerifyCredentials()

statuses = api.GetUserTimeline(screen_name='lucylucegoose')
print [s.text for s in statuses]

status = api.PostUpdate('Posting this from command line using python-twitter, woop woop!')


print 'done'

#Get test jsons
data = []

search = api.search(q='#govhack', result_type='recent',count=100)
tweets = search['statuses']

for tweet in tweets:
#print tweet['id_str'], '\n', tweet['screen_name'], '\n', tweet['text'], '\n', tweet['coordinates'], '\n\n\n'
                
    info = {"id":  tweet['id_str'], "text": tweet['text']}
    data.append(info)

import json
with open('tweetdata.json', 'w') as outfile:
    json.dump(data, outfile)



tweet_data = []
with open('tweetdata.json', 'rb') as fp:
        tweet_data= json.load(fp)