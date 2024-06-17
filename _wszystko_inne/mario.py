import cv2
import numpy as np
import os

os.chdir('_wszystko_inne/')

img = cv2.imread('mario.png')
gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('moneta.png', 0)
w, h = template.shape[::-1]

wynik = cv2.matchTemplate(gImg, template, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wynik)
# prawy = (max_loc[0] + w, max_loc[1] + h)
# img = cv2.rectangle(img, max_loc, prawy, (0, 0, 255), 5)

threshold = 0.75
lokalizacja = np.where(wynik >= threshold)
for lokalizacja_kwadrat in zip(*lokalizacja[::-1]):
    prawy = (lokalizacja_kwadrat[0] + w, lokalizacja_kwadrat[1] + h)
    img = cv2.rectangle(img, lokalizacja_kwadrat, prawy, (0, 0, 255), 5)

cv2.imshow('wynik', img)
cv2.waitKey(0)