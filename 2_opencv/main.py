import cv2
import numpy as np

print(cv2.__version__)

img = cv2.imread(r"C:\Users\adria\OneDrive\Pulpit\obrazki\IMG_1701.JPG", 0)
# 0 - skala szarości
print(img)

cv2.namedWindow("Obraz w skali szarości", cv2.WINDOW_AUTOSIZE)
#cv2.WINODOW_NORMAL
cv2.imshow("obraz w skali szarości", img)
cv2.waitKey(0)
cv2.destroyAllWindows()