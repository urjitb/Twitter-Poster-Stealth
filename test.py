import random as r

def randomUniqueTweetFetch(profileCounter = 7, tweetCounter = 7):
    tweetsFile = open("tweets",'r')
    tweets = tweetsFile.readlines()
    del tweets[0]
    #print(tweets)
    tweetsFile.close()

    tweet = r.choice(tweets)

    prevtweets = open("PrevTweets.txt",'r')
    prevtweetsList =  [eachtweet.lstrip() for eachtweet in prevtweets.readlines()]
    prevtweets.close()    

    prevtweetsList = list(filter(None, prevtweetsList))

    #print(prevtweetsList)


    while tweet in prevtweetsList:
        tweet = r.choice(tweets)
  
    if len(prevtweetsList) == profileCounter:
        del prevtweetsList[0]

    prevtweetsList.append(tweet)
    #print(prevtweets)
    prevtweets = open("PrevTweets.txt",'w')
    prevtweets.writelines(prevtweetsList)
    prevtweets.close()    


    return tweet.strip()

print(randomUniqueTweetFetch())