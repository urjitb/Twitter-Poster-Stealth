from mimetypes import init
from time import sleep
import pyautogui as auto
import os
import data

class WifiSwitch:
    def __init__(self) -> None:
        self.netList = data.networks
         
    def switcher(self,network):
        netCred = self.netList[network].split(':')
        os.system("networksetup -setairportpower en0 on")
        os.system("networksetup -setairportnetwork en0 \""+ netCred[0]+"\" \'"+netCred[1]+"\'")

