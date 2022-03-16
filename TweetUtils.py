from re import X
from time import sleep
import pyautogui as auto
import random as r
import os


class Utilities:
    PAUSE = 2

    def __init__(self, profileImg, browserChkImg):
        self.profileImage = profileImg
        self.browserChkImg = browserChkImg
        auto.PAUSE = self.PAUSE
        pass

    def WaitForImage(self, imageAddress):
        image = auto.locateOnScreen(
            imageAddress, grayscale=True, confidence=.9)
        while image == None:
            image = auto.locateOnScreen(imageAddress, confidence=0.9)

    def WaitForImageClick(self, imageAddress, diff_x=20, diff_y=20):

        image = auto.locateOnScreen(
            imageAddress, grayscale=True, confidence=.9)
        while image == None:
            image = auto.locateOnScreen(imageAddress, confidence=0.9)
            print("still haven't found the image")

        print(image)

        auto.moveTo(image.left/2+diff_x, image.top/2+diff_y, 0.2)
        auto.click()

    def WaitForImageRightClick(self, imageAddress, diff_x=20, diff_y=20):

        image = auto.locateOnScreen(
            imageAddress, grayscale=True, confidence=.7)
        while image == None:
            image = auto.locateOnScreen(imageAddress, confidence=0.9)
            print("still haven't found the image for right click")

        print(image)

        auto.moveTo(image.left/2+diff_x, image.top/2+diff_y, 0.2)
        auto.rightClick()

    def InitIncogniton(self, pendingUpdates=False):
        os.system("open /applications/Incogniton.app/Contents/MacOS/incogniton")

        if(pendingUpdates):
            self.WaitForImageClick("images/cancel_incog.png")
            self.WaitForImageClick("images/cancel_incog.png")

        self.WaitForImageClick(self.profileImage, diff_x=960)

        self.WaitForImage(self.profileImage)
        auto.keyDown("fn")
        auto.press("f")
        auto.keyUp("fn")

    def InitProfile(self):
        self.WaitForImageClick(self.browserChkImg, diff_x=960)
        self.WaitForImage(self.browserChkImg)

    def InitTwitter(self):

        auto.click(r.randint(255, 600), r.randint(52, 68))
        auto.typewrite("twitter.com/home")
        auto.press('enter')

    def TextTweet(self, textTweet="hi #hashtag"):
        self.WaitForImageClick("images/tweet.png")
        auto.typewrite(textTweet)
        auto.press("enter")
        self.WaitForImageClick("images/tweetbtn.png", diff_x=80)

    def CloseProfile(self):
        auto.keyDown("fn")
        auto.press("f")
        auto.keyUp("fn")
        self.WaitForImageRightClick("images/profile.png")
        auto.press("up")
        auto.press("enter")

    def CloseIncognition(self):
        
        browserOpen = auto.locateOnScreen(
            "images/browserOnScreen.png", grayscale=True, confidence=.9)

        if browserOpen:
            self.CloseProfile()

        self.WaitForImageRightClick("images/incogInDock.png")
        auto.press("up")
        auto.press("enter")

        

