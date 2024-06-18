import cv2
import numpy as np
import os

os.chdir('2_transformacje/')

img = cv2.imread('724.tif')
gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
w, h = gImg.shape[::-1]

top_left = [0, 0]

def measure(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x:', x + top_left[0], 'y:', y + top_left[1])

def zoom(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        zoom_level = 400
        if x < zoom_level:
            x = zoom_level
        if x > h - zoom_level:
            x = h - zoom_level
        if y < zoom_level:
            y = zoom_level
        if y > w - zoom_level:
            y = w - zoom_level
        
        imgCropped = img[y-zoom_level:y+zoom_level, x-zoom_level:x+zoom_level]
        global top_left
        top_left = [x-zoom_level, y-zoom_level]
        cv2.namedWindow('zoom', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('zoom', measure)
        cv2.imshow('zoom', imgCropped)

while(1):
    cv2.namedWindow('zdjecie pelne', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('zdjecie pelne', zoom)
    cv2.imshow('zdjecie pelne', img)
    cv2.waitKey(0)

