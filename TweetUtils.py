from cgitb import grey
from re import X
from time import sleep
import pyautogui as auto
import random as r
import os
import HumanActions as ha


class Utilities:
    PAUSE = 2

    def __init__(self):
        auto.PAUSE = self.PAUSE
        pass

    def WaitForImage(self, imageAddress):
        image = auto.locateOnScreen(
            imageAddress, grayscale=True, confidence=.9)
        while image == None:
            image = auto.locateOnScreen(imageAddress, confidence=0.9)
            print(imageAddress)

    def WaitForImageClick(self, imageAddress:str, diff_x=20, diff_y=20):
        iAddress = imageAddress.split(',')
        image = None
        for img in iAddress:
            image = auto.locateOnScreen(
                img, grayscale=True, confidence=.9)
        while image == None:
            for img in iAddress:
                image = auto.locateOnScreen(
                    img, grayscale=True, confidence=.9)
                print("still haven't found the image")

        print(image)

        ha.click(image.left/2+diff_x, image.top/2+diff_y)

    def WaitForImageRightClick(self, imageAddress, diff_x=20, diff_y=20):

        image = auto.locateOnScreen(
            imageAddress, grayscale=True, confidence=.8)
        while image == None:
            image = auto.locateOnScreen(imageAddress, confidence=0.9)
            print("still haven't found the image for right click " + imageAddress)

        print(image)

        ha.rightClick(image.left/2+diff_x, image.top/2+diff_y)

    def InitIncogniton(self, pendingUpdates=False):
        auto.PAUSE = 1
        os.system("open /applications/Incogniton.app/Contents/MacOS/incogniton")

        if(pendingUpdates):
            self.WaitForImageClick("images/cancel_incog.png")
            self.WaitForImageClick("images/cancel_incog.png")

        auto.PAUSE = 2

    def InitProfile(self,profileImg,browserImg):
        
        self.WaitForImageClick(profileImg, diff_x=960)

        self.WaitForImage(browserImg)
        auto.keyDown("fn")
        auto.press("f")
        auto.keyUp("fn")

    def CheckIfLoggedIn(self,):
        self.WaitForImage()

    def InitTwitter(self):
        
        ha.click(r.randint(255, 600), r.randint(52, 68))
        auto.typewrite("twitter.com/home")
        auto.PAUSE = 5
        auto.press('enter')
        
        signIn = auto.locateOnScreen("images/sign_In_With_Google.png",grayscale=True, confidence=0.8)
       
        auto.PAUSE = 2
        if(signIn):
            return False
        else:
            return True
        
    def Tweet(self, textTweet="hi #hashtag", image = None):
        
        self.WaitForImageClick("images/tweet.png",diff_y=r.randint(20,50),diff_x=r.randint(30,80))
        auto.typewrite(textTweet)
        auto.press("enter")
        
        if(image):
            self.WaitForImageClick("images/imageUpload.png")
            self.WaitForImageClick("images/imageSearch.png",diff_y=5)
            auto.typewrite(image)
            ha.click(565,365)
            ha.click(1065,645)
            pass


        #self.WaitForImageClick("images/tweetbtn.png", diff_x=80)

    def CloseProfile(self):
        auto.PAUSE = 1
        auto.keyDown("fn")
        auto.press("f")
        auto.keyUp("fn")
        self.WaitForImageRightClick("images/profile.png")
        auto.press("up")
        auto.press("enter")
        auto.PAUSE = 2

    def CloseIncognition(self):

        browserOpen = auto.locateOnScreen(
            "images/browserOnScreen.png", grayscale=True, confidence=.9)

        if browserOpen:
            self.CloseProfile()

        self.WaitForImageClick("images/term.png")
        auto.keyDown("command")
        auto.press("w")
        auto.keyUp("command")
        auto.press("enter")
