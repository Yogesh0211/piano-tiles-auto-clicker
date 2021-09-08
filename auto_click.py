from pynput.mouse import Button, Controller
import fastgrab.screenshot as ss
import time
import cv2
import numpy as np

def click(x, y):
    mouse.position = (x,y)
    mouse.press(Button.left)
    mouse.release(Button.left)

def clickfirstblock(im):
    global gameCoordinates, previouslane, score
    for y_ in range(5, len(im)-5, 5):
        for i in range(4):
            if previouslane == i:
                continue
            w = gameCoordinates[2] - gameCoordinates[0]
            y = len(im) - y_
            x = i*w//4 + w//8
            if im[y,x] < 30:
                actual_x = x + gameCoordinates[0]
                actual_y = y + gameCoordinates[1]
                if score > 100:
                    actual_y += 20
                if score > 300:
                    actual_y += 20
                if score > 500:
                    actual_y += 20
                if score > 700:
                    actual_y += 20
                if score > 1000:
                    actual_y += 20
                if score > 1100:
                    actual_y += 20
                if score > 1300:
                    actual_y += 20
                click(actual_x, actual_y)
                score += 1
                previouslane = i
                return
time.sleep(5)
gameCoordinates = [680, 243, 1243, 1079]
starttime = time.time()
mouse = Controller()
mouse.position = (742, 729) # First
mouse.position = (885, 721) # Second
mouse.position = (1025, 729) # Third
mouse.position = (1170, 725) # Fourth
mouse.press(Button.left)
mouse.release(Button.left)
score = 0
# time.sleep(1)
num = 1
previouslane = -1
while True:
#     ss_time = time.time()
    im = ss.Screenshot().capture(bbox = [680, 243, 563, 836])
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    clickfirstblock(im)
#     print(f'Time taken by {num} frame is {time.time() - ss_time} seconds ')
#     num += 1
    pos = mouse.position
    if pos[0] > gameCoordinates[2]:
        break
