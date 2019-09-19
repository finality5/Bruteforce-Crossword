import cv2
import numpy as np
import pyautogui
import time

time.sleep(2)
img = pyautogui.screenshot('img.png')
img = cv2.imread('img.png')

lower = np.array([0, 0, 200])
upper = np.array([127, 127,255])

mask = cv2.inRange(img, lower, upper)

cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()