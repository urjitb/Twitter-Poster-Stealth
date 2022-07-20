import random
from bs4 import BeautifulSoup
from html import unescape

networks = {"poco":'POCO X3 Pro:Stricker32!',"vivo":'vivo 1818:worldHello7890231?@!',"xenu":'Xenu_5g:Stricker32!'}

#change p1 and p2 to somthing more readable
profiles = [{"nameImg": "images/p1/start.png",
                "browserChk": "images/p1/browser.png",
                "connection":"poco","sc":"ashieblax"},{"nameImg": "images/p2/start.png",
                "browserChk": "images/p2/browser.png",
                "connection":"poco","sc":"ashieblax"},{"nameImg": "images/p3/start.png",
                "browserChk": "images/p3/browser.png",
                "connection":"xenu","sc":"ashieblax"}]



class TwData:
    def __init__(self):

        file = open("tweets")
        tlist = []
        rep = []
        self.tweetlist = rep

        for st in file:
            st.replace("\n","")
            if "http" in st:
                tlist.append(st[0:len(st)-24])
            else:
                tlist.append(st)

        
        
        for x in tlist:
            rep.append(BeautifulSoup(unescape(x.replace("\n", "")+ '\n'),'lxml').text)


        file.close()


    def randomTweet(self):

        return (str(random.choice(self.tweetlist)).strip().replace('tuname1',self.snapName))

    def randomUniqueTweetFetch(self, snap, profileCounter = 40):

       
        tweets = self.tweetlist
        
        tweet = random.choice(tweets)

        prevtweets = open("PrevTweets.txt",'r')
        prevtweetsList =  [eachtweet.lstrip() for eachtweet in prevtweets.readlines()]

        prevtweets.close()    

        prevtweetsList = list(filter(None, prevtweetsList))

        while '\n' in prevtweetsList:
            prevtweetsList.remove('\n')

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

        return tweet.strip().replace('tuname1',snap)