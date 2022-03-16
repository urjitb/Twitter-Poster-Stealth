from re import X
from time import sleep
import pyautogui as auto
import random as r
import os

image = auto.locateOnScreen(
    "images/p1/a4y4.png", grayscale=True, confidence=.9)

if(image):
    print(image)
else:
    print("no image found")
