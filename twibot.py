import tweepy

print("This is my Twitter bot.")

CONSUMER_KEY = 'fQYLc7fQMBewZC6Z4tc56VTaJ'
CONSUMER_SECRET = '4cqzZ5gMgfnbb10iBSWuNT0QlpVyCmat3Zuz3RR8YpdT6qvs3W'
ACCESS_KEY = '1244637342293544961-XcmPATJWFvYZaNlBPKr157elAiD1Pk'
ACCESS_SECRET = 'fOQUmWcD0iHswTyrD4wXDATvW16rXBOTkqq0mDnqGIqIo'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)