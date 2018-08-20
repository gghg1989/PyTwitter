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
 
#Update a tweet
api.update_status(status="This is a tweet sent automatically by a Python script! (Don't worry, friends. I'm just testing my code.)")
 
#Search tweets by "keyword"
results = api.search(q = "keyword")
for result in results:
	print(result.text)
