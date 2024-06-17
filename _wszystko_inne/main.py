import cv2
import numpy as np

tiff = cv2.imread('724.tif')
gtiff = cv2.cvtColor(tiff, cv2.COLOR_BGR2GRAY)
w, h = tiff.shape[:2]

template_1 = cv2.imread('4_transformacja/krzyz_1.png', 0)
w_1, h_1 = template_1.shape[::-1]

template_2 = cv2.imread('4_transformacja/krzyz_2.png', 0)
w_2, h_2 = template_2.shape[::-1]

def measure(event, x, y, flags, param):
    global imgCropped
    wynik1 = cv2.matchTemplate(imgCropped, template_1, cv2.TM_CCOEFF_NORMED)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(wynik1)
    print(max_loc1)
    right1 = (max_loc1[0] + w_1, max_loc1[1] + h_1)
    imgCropped = cv2.rectangle(imgCropped, max_loc1, right1, (0, 0, 255), 5)
    # cv2.imshow('zoom', imgCropped)

def zoom(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        zoom_level = 300
        if x < zoom_level:
            x = zoom_level
        if x > h - zoom_level:
            x = h - zoom_level
        if y < zoom_level:
            y = zoom_level
        if y > w - zoom_level:
            y = w - zoom_level
        
        global imgCropped
        imgCropped = tiff[y-zoom_level:y+zoom_level, x-zoom_level:x+zoom_level]
        cv2.namedWindow('zoom', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('zoom', measure)
        cv2.imshow('zoom', imgCropped)



while(1):
    cv2.namedWindow('zdjecie pelne', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('zdjecie pelne', zoom)
    cv2.imshow('zdjecie pelne', tiff)
    if cv2.waitKey(20) and 0xFF == 27:
        break