import cv2
import numpy as np
import pyautogui
import time

alp="aeioulnstrdgbcmpfhvwykjxqz"
lower = np.array([0, 0, 200])
upper = np.array([127, 127,255])
time.sleep(2)

for i in range(15*15):
    pyautogui.press('a')

for i in range(1,len(alp)):
    img = pyautogui.screenshot('img.png')
    time.sleep(1)
    img = cv2.imread('img.png')
    img = cv2.resize(img,None,fx=0.5,fy=0.5)

    result = img.copy()
    mask = cv2.inRange(img, lower, upper)

    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    pos=[]
    for cnt in contours :
        area = cv2.contourArea(cnt)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(result,[box],0,(0,0,255),2)

        center, _, _ = cv2.minAreaRect(cnt)
        x, y = center
        pyautogui.click(int(x), int(y))
        pyautogui.press(alp[i])

      

