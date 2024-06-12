from time import sleep

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://elgoog.im/dinosaur-game/")


# start the game
sleep(1)
pyautogui.press('up')

# get location of dino
loc = None
while(True):
    sleep(1)
    try:
        loc = pyautogui.locateCenterOnScreen('dinosaur.png', confidence=0.8)
        break
    except:
        pass

white = 255 * 3
while(True):
    im = pyautogui.screenshot()
    x = loc.x + 200
    y = loc.y

    pixels = [
        (x, y),
        (x + 25, y),
        (x + 50, y),
        (x, y + 25),
        (x + 25, y + 25),
        (x + 50, y + 50)
    ]

    for p in pixels:
        if sum(im.getpixel(p)) < white:
            print('jumped!')
            pyautogui.press('up')
            break

