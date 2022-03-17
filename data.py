import random

networks = {"poco":'POCO X3 Pro:Stricker32!',"vivo":'vivo 1818:worldHello7890231?@!'}

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

    def randomTweet(self):

        return (str(random.choice(self.tweetlist)).strip().replace('tuname1',self.snapName))

