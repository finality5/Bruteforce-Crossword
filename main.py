import cv2
import time
import pyautogui
from numpy import array

# string of alphabet ordered which frequenly used .
alp = "aeioulnstrdgbcmpfhvwykjxqz"

# red color .
lower = array([0, 0, 200])
upper = array([127, 127,255])

time.sleep(2)

# initial alphabet 'A' into 15*15table .
for i in range(15*15):
    pyautogui.press('a')

# replace wrong slots with new alphabet .
for i in range(1, len(alp)):

    img = pyautogui.screenshot('img.png')
    img = cv2.imread('img.png')
    # img = cv2.resize(img,None,fx=0.5,fy=0.5)

    mask = cv2.inRange(img, lower, upper)

    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours :
        center, _, _ = cv2.minAreaRect(cnt)
        x, y = center
        pyautogui.click(int(x), int(y))
        pyautogui.press(alp[i])
