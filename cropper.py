# CHANGE ALL THE FILE PATHS TO THEIR FULL PATHS

import pyautogui
import cv2
import sys
import os 
from time import sleep
from PIL import Image
import keyboard

refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	
	global refPt, cropping
	
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
	
	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x, y))
		left,top = refPt[0]
		right,bottom = refPt[1]
		cropping = False
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 3)
		cv2.imshow("image", image)

# while True:
# 	if keyboard.is_pressed('s'):
#       pyautogui.screenshot().save('./test.png')
# 		break
# 	else:
# 		continue

sleep(1)
pyautogui.screenshot().save('./test.png')

image = cv2.imread('./test.png')
clone = image.copy()
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
pysize = pyautogui.size()
cv2.resizeWindow('image', pysize[0], pysize[1])
cv2.setMouseCallback("image", click_and_crop)

while True:
	key = cv2.waitKey(1) & 0xFF
	
	cv2.imshow("image", image)
	
	if key == ord("r"):
		image = clone.copy()
	elif key == ord("c"):
		break

if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
	imS = cv2.resize(roi, (1920, 1080))
	cv2.imshow("ROI", imS)
	cv2.imwrite('./cropped.png', roi)

cv2.destroyAllWindows()

