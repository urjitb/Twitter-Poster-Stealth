from time import sleep
import TweetUtils as utils

profiles = [{"nameImg": "images/start_a4y4.png",
             "browserChk": "images/a4y4.png"},
            {"nameImg": "images/start_a6y6.png",
             "browserChk": ""}]

for i, profile in enumerate(profiles):

    wProfile = utils.Utilities(profile["nameImg"], profile["browserChk"])

    if i == 0:
        wProfile.InitIncogniton()

    wProfile.InitTwitter()
    wProfile.TextTweet()
    wProfile.CloseProfile()
