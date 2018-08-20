import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"
 

#Create OAuth object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Build API object with OAuth
api = tweepy.API(auth)

#Counter for actual number of tweets from query
count = 0
#Set a result tweets limit
tweetLimit = 1000

#Search tweets by "keyword" between specific date, around specific location
cricTweet = tweepy.Cursor(api.search, q='keyword', since = '2015-12-29', until = '2015-12-30', geocode = "25.75869,-80.37388,10000mi").items(tweetLimit)
for tweet in cricTweet:
	count += 1
	#Print tweet content
	print(tweet.created_at)
	print(tweet.text.encode('unicode-escape'))
	print(tweet.location if hasattr(tweet, 'location') else "Undefined location")
	print("\n")
#Print actual tweets number
print(count)
