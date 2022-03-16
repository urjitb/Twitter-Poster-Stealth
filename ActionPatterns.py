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
            
            wProfile.profileImage = profile["nameImg"]
            wProfile.browserChkImg = profile["browserChk"]
            wsu.switcher(profile["connection"])
            if i == 0:
                wProfile.InitIncogniton()
            wProfile.InitProfile()
            #wProfile.InitTwitter()
            #wProfile.TextTweet(self.data.randomTweet())
            wProfile.CloseProfile()

        #end
        wProfile.CloseIncognition()
