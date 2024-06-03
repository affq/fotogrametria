import cv2
import numpy as np

img = cv2.imread('3_mario/mario.png')
gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('3_mario/moneta.png', 0)
w, h = template.shape[::-1]

wynik = cv2.matchTemplate(gImg, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wynik)
print(max_loc)
prawy = (max_loc[0] + w, max_loc[1] + h)
img = cv2.rectangle(img, max_loc, prawy, (0, 0, 255), 5)

# threshold = 0.75
# lokalizacja = np.where(wynik >= threshold)
# for lokalizacja_kwadrat in zip(*lokalizacja[::-1]):
#     prawy = (lokalizacja_kwadrat[0] + w, lokalizacja_kwadrat[1] + h)
#     img = cv2.rectangle(img, lokalizacja_kwadrat, prawy, (0, 0, 255), 5)

cv2.imshow('wynik', img)
cv2.waitKey(0)

# global img
# imgOriginal = cv2.imread('3_mario/724.tif')

# def match(event, x, y, flags, param):
#     global imgCropped
#     if event == cv2.EVENT_LBUTTONDOWN:
#         gImg = cv2.cvtColor(imgCropped, cv2.COLOR_BGR2GRAY)
#         template = cv2.imread('3_mario/krzyz.png', 0)
#         w, h = template.shape[::-1]
#         wynik = cv2.matchTemplate(gImg, template, cv2.TM_CCOEFF_NORMED)
#         threshold = 0.2
#         lokalizacja = np.where(wynik >= threshold)
#         for lokalizacja_kwadrat in zip(*lokalizacja[::-1]):
#             prawy = (lokalizacja_kwadrat[0] + w, lokalizacja_kwadrat[1] + h)
#             imgCropped = cv2.rectangle(imgCropped, lokalizacja_kwadrat, prawy, (0, 0, 255), 5)
#         cv2.imshow('zoom', imgCropped)
#         cv2.waitKey(0)

# def zoom(event, x, y, flags, param):
#     global imgOriginal, imgCropped
#     if event == cv2.EVENT_LBUTTONDOWN:
#         zoom_level = 300
#         if x < zoom_level:
#             x = zoom_level
#         if x > imgOriginal.shape[1] - zoom_level:
#             x = imgOriginal.shape[1] - zoom_level
#         if y < zoom_level:
#             y = zoom_level
#         if y > imgOriginal.shape[0] - zoom_level:
#             y = imgOriginal.shape[0] - zoom_level
#         imgCropped = imgOriginal[y-zoom_level:y+zoom_level, x-zoom_level:x+zoom_level]
#         cv2.namedWindow('zoom', cv2.WINDOW_NORMAL)
#         cv2.setMouseCallback('zoom', match)
#         cv2.imshow('zoom', imgCropped)
#         cv2.waitKey(0)
        

# cv2.namedWindow('main', cv2.WINDOW_NORMAL)
# cv2.setMouseCallback('main', zoom)

# while(1):
#     cv2.namedWindow('main', cv2.WINDOW_NORMAL)
#     cv2.imshow('main', imgOriginal)
#     if cv2.waitKey(20) == 27:
#         break

# cv2.destroyAllWindows()