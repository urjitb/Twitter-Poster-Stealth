import random
import pyautogui as py


eases = [py.easeOutQuad, py.easeOutQuad,
                              py.easeOutQuad, py.easeOutBack, py.easeOutBack, py.easeInOutQuad]

def click(x, y, da=0.5, db=1.8):
    py.moveTo(x, y, random.uniform(da, db),
                random.choice(eases))
    py.click()

def rightClick(x, y, da=0.5, db=1.8):
    py.moveTo(x, y, random.uniform(da, db),
                random.choice(eases))
    py.rightClick()