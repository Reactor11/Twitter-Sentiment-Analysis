import json
import pandas as pd
import matplotlib.pyplot as plt

tweet_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweet_path,'r')
print(tweets_file)
for line in tweets_file:
    try:
        line = json.dumps(line)
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
tweets_file.close()
print(len(tweets_data))
print(tweets_data[0])

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)