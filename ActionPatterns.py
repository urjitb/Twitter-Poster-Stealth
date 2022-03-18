from time import sleep
import TweetUtils as utils
import data
import WifiSwitchUtil



class Patterns:
    def __init__(self):
        pass

    def SendTweets(self, images=None):
        self.d = data.TwData()
        #begin
        wProfile = utils.Utilities()
        wsu = WifiSwitchUtil.WifiSwitch()
        
        for i, profile in enumerate(data.profiles):
            
            wsu.switcher(profile["connection"])
            if i == 0:
                wProfile.InitIncogniton()
            wProfile.InitProfile(profile["nameImg"],profile["browserChk"])
            if(wProfile.InitTwitter()):
                wProfile.TextTweet(self.d.randomUniqueTweetFetch(profile["sc"]))
            wProfile.CloseProfile()

        #end
        wProfile.CloseIncognition()
