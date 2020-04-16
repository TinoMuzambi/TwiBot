import tweepy

FILE_NAME="last_seen_id.txt"

CONSUMER_KEY = 'fQYLc7fQMBewZC6Z4tc56VTaJ'
CONSUMER_SECRET = '4cqzZ5gMgfnbb10iBSWuNT0QlpVyCmat3Zuz3RR8YpdT6qvs3W'
ACCESS_KEY = '1244637342293544961-XcmPATJWFvYZaNlBPKr157elAiD1Pk'
ACCESS_SECRET = 'fOQUmWcD0iHswTyrD4wXDATvW16rXBOTkqq0mDnqGIqIo'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode = "extended") 

for mention in reversed(mentions):
    print(str(mention.id) + " - " + mention.text)
    if "#testing" in mention.text.lower():
        print("Found #testing responding back")