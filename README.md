# PyTwitter

## Twitter API authentication
To get data from Twitter, firstly need to get Twitter API authentication, powered by OAuth, by following the steps:

1. Create a twitter account if you do not already have one.
2. Go to https://apps.twitter.com/ and log in with your twitter credentials.
3. Click "Create New App"
4. Fill out the form, agree to the terms, and click "Create your Twitter application"
5. In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
6. Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".

Then we can use Twitter API to get information we want, which we can get and set user statuses, send tweet, search tweets by keyword or by geography information etc, get twitter streaming tracks, get friendships information etc...[CHECK the API](https://dev.twitter.com/rest/public)

## Install Tweepy

* The easiest way to install the latest version is by using pip/easy_install to pull it from PyPI:
```bash
pip install tweepy
```
* You may also use Git to clone the repository from Github and install it manually:
```bash
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python setup.py install
```
* You can also [download it as zip file](https://github.com/tweepy/tweepy/archive/master.zip), then unfold it and run python setup.py install in command line.

## Searching from Twitter

### For searching specific time period, add parameters after q="keyword":
```python
results = api.search(q = "keyword", since="yyyy-mm-dd", until="yyyy-mm-dd")
for result in results:
	print(result.text)
```
Twitter API set the search index with a 7-day limit. In other words, no tweets will be found for a date older than one week. ([MENTION IN TWITTER API](https://dev.twitter.com/rest/reference/get/search/tweets#api-param-since_id))
### For searching by geocode, add parameters after q="keyword":
```python
results = api.search(q = "keyword", geocode="37.781157,-122.398720,1mi")
for result in results:
	print(result.text)
```
Returns tweets by users located within a given radius of the given latitude/longitude.
The parameter value is specified by “latitude,longitude,radius”.
Radius units must be specified as either “mi” (miles) or “km” (kilometers). 

Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly. A maximum of 1,000 distinct “sub-regions” will be considered when using the radius modifier.
