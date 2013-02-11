"""
The lines below are meant to be edited. Please edit them. They're for editing.
"""

# gotten from the twitter app page
TWITTER_CONSUMER_KEY = ""
TWITTER_CONSUMER_SECRET = ""
TWITTER_ACCESS_TOKEN = ""
TWITTER_ACCESS_SECRET = ""

# command used for speech - uncomment the one you need
#SPEAK_CMD = ["say"] # osx
SPEAK_CMD = ["espeak"] # linux - will need to install it first

# minutes between poll attempts
# twitter rate-limits the call here to 15 times per hour - so at most every 4 mins. set faster at your own risk!
POLL_INTERVAL = 5

# announce power-on?
ANNOUNCE_ENABLED = True
ANNOUNCE_MESSAGE = "Twitter reader ready"

# message template
MESSAGE = "%s tweeted: %s"
