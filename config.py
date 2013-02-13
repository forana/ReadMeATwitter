# gotten from the twitter app page
TWITTER_CONSUMER_KEY = ""
TWITTER_CONSUMER_SECRET = ""
TWITTER_ACCESS_TOKEN = ""
TWITTER_ACCESS_SECRET = ""

# minutes between poll attempts
# twitter rate-limits the call here to 15 times per hour - so at most every 4 mins. set faster at your own risk!
POLL_INTERVAL = 5

# announce power-on?
ANNOUNCE_ENABLED = True
ANNOUNCE_MESSAGE = "Twitter reader ready"

# message template
MESSAGE = "%s tweeted: %s"
