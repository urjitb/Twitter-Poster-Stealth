import random

networks = {"poco":'POCO X3 Pro:Stricker32!',"vivo":'vivo 1818:worldHello7890231?@!'}

#change p1 and p2 to somthing more readable
profiles = [{"nameImg": "images/p1/start.png",
                "browserChk": "images/p1/browser.png",
                "connection":"poco"},{"nameImg": "images/p2/start.png",
                "browserChk": "images/p2/browser.png",
                "connection":"vivo"}]

class TwData:
    

    def __init__(self, snapName):

        self.snapName = snapName
        file = open("tweets")
        tlist = []
        self.tweetlist = tlist

        for st in file:

            if "http" in st:
                tlist.append(st[0:len(st)-24])
            else:
                tlist.append(st)

        file.close()


    def randomTweet(self):

        return (str(random.choice(self.tweetlist)).strip().replace('tuname1',self.snapName))

    def randomUniqueTweetFetch(self,profileCounter = 7, tweetCounter = 7):


        tweets = self.tweetlist


        tweet = random.choice(tweets)

        prevtweets = open("PrevTweets.txt",'r')
        prevtweetsList =  [eachtweet.lstrip() for eachtweet in prevtweets.readlines()]
        prevtweets.close()    

        prevtweetsList = list(filter(None, prevtweetsList))

        #print(prevtweetsList)


        while tweet in prevtweetsList:
            tweet = random.choice(tweets)
    
        if len(prevtweetsList) == profileCounter:
            del prevtweetsList[0]

        prevtweetsList.append(tweet)
        #print(prevtweets)
        prevtweets = open("PrevTweets.txt",'w')
        prevtweets.writelines(prevtweetsList)
        prevtweets.close()    


        return tweet.strip()