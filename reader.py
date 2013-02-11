from client import Client
import speaker
import config

from Queue import Queue
from time import sleep
from threading import Thread

client = Client()

queue = Queue()
quit = False

if config.ANNOUNCE_ENABLED:
	speaker.speak(config.ANNOUNCE_MESSAGE)

def gather():
	global queue, quit
	lastId = client.getLatestTweetId()
	print "Last tweet = "+lastId

	while not quit:
		sleep(60 * config.POLL_INTERVAL)
		tweets = client.getTweets(lastId)
		if len(tweets)>0:
			lastId = tweets[0].id
			for tweet in reversed(tweets):
				print "Queueing "+str(tweet)
				queue.put(tweet)
		else:
			print "No tweets - I checked"

def read():
	global queue, quit
	while not quit:
		sleep(1)
		if not queue.empty():
			tweet = queue.get()
			message = config.MESSAGE % (tweet.user, tweet.tweet)
			print "Saying: "+message
			speaker.speak(message)

gatherThread = Thread(target=gather)
gatherThread.daemon = True
readThread = Thread(target=read)
readThread.daemon = True

try:
	gatherThread.start()
	readThread.start()
except Exception as e:
	quit = True
	print e
	speaker.speak(e)

while not quit:
	try:
		gatherThread.join(1)
		readThread.join(1)
	except KeyboardInterrupt:
		quit = True
