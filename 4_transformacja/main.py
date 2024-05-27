import cv2
import numpy as np

tiff = cv2.imread('4_transformacja/724.tif')
w, h = tiff.shape[::-1]

template_1 = cv2.imread('4_transformacja/krzyz_1.png', 0)
w_1, h_1 = template_1.shape[::-1]

template_2 = cv2.imread('4_transformacja/krzyz_2.png', 0)
w_2, h_2 = template_2.shape[::-1]

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
        imgCropped = tiff[y-zoom_level:y+zoom_level, x-zoom_level:x+zoom_level]



while(1):
    cv2.namedWindow('zdjecie pelne', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('zdjecie pelne', zoom)
    cv2.imshow('zdjecie pelne', tiff)
    if cv2.waitKey(20) == 27:
        break