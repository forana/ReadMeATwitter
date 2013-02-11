import oauth2
import config
from contextlib import closing
import simplejson

class Client:
	FIRST_REQUEST_URL = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=1"
	HOME_REQUEST_URL = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=100&since_id=%s"

	def __init__(self):
		consumer = oauth2.Consumer(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
		token = oauth2.Token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_SECRET)
		self.client = oauth2.Client(consumer, token)

	def getRawJSON(self, sinceId = 0):
		url = Client.FIRST_REQUEST_URL if sinceId == 0 else (Client.HOME_REQUEST_URL % (sinceId,))
		resp, content = self.client.request(url, "GET")
		return simplejson.loads(content)
		#with closing(open("sample.json",'r')) as file:
		#	return simplejson.loads(file.read())

	def getLatestTweetId(self):
		return Tweet(self.getRawJSON()[0]).id

	def getTweets(self, sinceId): 
		return map(Tweet, self.getRawJSON(sinceId))

class Tweet:
	def __init__(self, obj):
		self.id = obj["id_str"]
		self.tweet = obj["text"].encode('ascii', 'ignore')
		self.user = obj["user"]["name"].encode('ascii', 'ignore')

	def __str__(self):
		return "#%s: %s: %s" % (self.id, self.user, self.tweet)
