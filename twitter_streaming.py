from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1133205265187131392-4h9hV3hdCIIBHJXsce2umHWdgNKnxR"
access_token_secret = "cZgta6nL6pz5IVCdBf2oGvuYQrh5JRqrEpdeNGEbNxK9b"
consumer_key = "Il4y1yMLiJAuO9ouqcXSZESYJ"
consumer_secret = "ITJTqFApceDy2FfYz0vong4UK3ve4YbPBSTmwKpkp79Tqj2pkt"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['INC', 'BJP', 'BSP','NCP','CPI'])