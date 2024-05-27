import cv2
import numpy as np

tiff = cv2.imread('4_transformacja/724.tif')

template_1 = cv2.imread('4_transformacja/krzyz_1.png', 0)
w_1, h_1 = template_1.shape[::-1]

template_2 = cv2.imread('4_transformacja/krzyz_2.png', 0)
w_2, h_2 = template_2.shape[::-1]

def zoom(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        zoom_level = 300


while(1):
    cv2.namedWindow('zdjecie pelne', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('zdjecie pelne', zoom)
    cv2.imshow('zdjecie pelne', tiff)
    if cv2.waitKey(20) == 27:
        break