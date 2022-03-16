import WifiSwitchUtil
from time import sleep

wSwitch = WifiSwitchUtil.WifiSwitch()

wSwitch.switcher(wSwitch.vivo)
sleep(5)
wSwitch.switcher(wSwitch.poco)