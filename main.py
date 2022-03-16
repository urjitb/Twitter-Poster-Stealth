from time import sleep
import TweetUtils as utils

profiles = [{"nameImg": "images/p1/start_a4y4.png",
             "browserChk": "images/p1/a4y4.png"},
            {"nameImg": "images/p2/start_a6y6.png",
             "browserChk": "images/p2/a6y6.png"}]

for i, profile in enumerate(profiles):

    wProfile = utils.Utilities(profile["nameImg"], profile["browserChk"])

    if i == 0:
        wProfile.InitIncogniton()

    wProfile.InitTwitter()
    wProfile.TextTweet()
    wProfile.CloseProfile()
