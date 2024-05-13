import cv2
import numpy as np

print(cv2.__version__)

img = cv2.imread(r"C:\Users\adria\OneDrive\Pulpit\obrazki\IMG_1701.JPG", 0)
# 0 - skala szarości
print(img)

# cv2.namedWindow("Obraz w skali szarości", cv2.WINDOW_AUTOSIZE)
#cv2.WINDOW_NORMAL
# cv2.imshow("obraz w skali szarości", img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('z'):
    cv2.imwrite(r"szarosc.png", img)
    cv2.destroyAllWindows()

imgRGB = cv2.imread(r"C:\Users\adria\OneDrive\Pulpit\obrazki\IMG_1701.JPG")

# wiersze, kolumny = img.shape
# img[200:800, 100:300] = 255
# cv2.imshow("obraz w skali szarości", img)
# k = cv2.waitKey(0)

# wiersze, kolumny, kanaly = imgRGB.shape
# imgRGB[200:800, 100:300] = [0, 0, 255]
# cv2.imshow("obraz RGB", imgRGB)
# k = cv2.waitKey(0)

b, g, r = cv2.split(imgRGB)

newImgGRB = cv2.merge((g, r, b))
# cv2.imshow("obraz RGB", newImgGRB)

# imgRGB[:, :, 0] = 0
# cv2.imshow("obraz RGB", imgRGB)

img1 = cv2.imread(r"C:\Users\adria\OneDrive\Pulpit\fotogrametria\2_opencv\poland.png")
img2 = cv2.imread(r"C:\Users\adria\OneDrive\Pulpit\fotogrametria\2_opencv\dog.png")
img3 = cv2.addWeighted(img1, 0.6, img2, 0.4, 20)
# cv2.imshow("obraz RGB", img3)
# k = cv2.waitKey(0)
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x, y), 20, (172,90,255), -1)
# # Create a black image, a window and bind the function to window
# img = np.zeros((1024,860,3), np.uint8)
# cv2.namedWindow('paint')
# cv2.setMouseCallback('paint',draw_circle)
# while(1):
#     cv2.imshow('paint',img)
#     if cv2.waitKey(20) == 27:
#         break
# cv2.destroyAllWindows()

def draw_coords(x, y, img):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, f'x: {x}, y: {y}', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

def measure(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if x < 200:
            x = 200
        if x > img3.shape[1] - 200:
            x = img3.shape[1] - 200
        if y < 200:
            y = 200
        if y > img3.shape[0] - 200:
            y = img3.shape[0] - 200
        roi = img3[y-200:y+200, x-200:x+200]
        cv2.imshow('zoom', roi)
        k = cv2.waitKey(0)

cv2.namedWindow('zoom')
cv2.setMouseCallback('zoom', measure)
while(1):
    cv2.imshow('zoom', img3)
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()
