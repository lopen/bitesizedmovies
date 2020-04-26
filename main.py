import tweepy, time

CONSUMER_KEY = "XXXX"
CONSUMER_SECRET = "XXXX"
ACCESS_KEY = "XXXX"
ACCESS_SECRET = "XXXX"

auth = tweepy.OAuthHandler(CONSUMER_KEY,
                           CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY,
                      ACCESS_SECRET)

api = tweepy.API(auth)

# start index of the tweet
startnum = 0
# end index of the tweet
endnum = 150

# the script that makes the actual tweet string
def make(filename):
    global endnum, startnum
    
    with open("moviescripts/" + filename, "r") as file:
        string = file.read().replace("\n", "")

    # not implmented yet, check trimmer function
    # endnum = trimmer(string, endnum+1)

    tweet = string[startnum:endnum]
    startnum = endnum
    endnum = endnum + 150
    
    return tweet

# function meant to trim the tweets so we don't end up with any half cut words
# will implement this later down the line
def trimmer(string, endnum):
    if string[endnum].isalpha():
        nextSpace = endnum - 1
        trimmer(string, endnum)
    elif not string[endnum].isalpha():
        return endnum
    
# main loop
while True:
    api.update_status(make("bee.txt"))
    time.sleep(24.0 * 60.0 * 60.0)
