from time import sleep
import TweetUtils as utils
import data
import WifiSwitchUtil



class Patterns:
    def __init__(self,snapUser):
        self.data = data.TwData(snapUser)
        pass

    def SendTweets(self, images=None):

        #begin
        wProfile = utils.Utilities()
        wsu = WifiSwitchUtil.WifiSwitch()

        for i, profile in enumerate(data.profiles):
            
            wsu.switcher(profile["connection"])
            if i == 0:
                wProfile.InitIncogniton()
            wProfile.InitProfile(profile["nameImg"],profile["browserChk"])
            #wProfile.InitTwitter()
            #wProfile.TextTweet(self.data.randomTweet())
            wProfile.CloseProfile()

        #end
        wProfile.CloseIncognition()
