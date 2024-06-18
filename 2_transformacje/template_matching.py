import cv2
import numpy as np
import os   

os.chdir('2_transformacje/')

img = cv2.imread('724.tif')
img = cv2.rotate(img, cv2.ROTATE_180)
gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

krzyz_1 = cv2.imread('krzyz_1.tif',0)
krzyz_2 = cv2.imread('krzyz_2.tif',0)
templates = [krzyz_1, krzyz_2]

topleft_x = 0
topleft_y = 0

zoom_level = 200

cropped_img = None

centers = []

def match(event, x, y, flags, params):
    global topleft_x, topleft_y, cropped_img, zoom_level, img, w, h, centers, templates
    if event == cv2.EVENT_LBUTTONDBLCLK:
        g_cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

        for template in templates:
            w, h = template.shape[::-1]
            result = cv2.matchTemplate(g_cropped_img, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > 0.75:
                max_loc_img = (max_loc[0] + topleft_x - zoom_level, max_loc[1] + topleft_y - zoom_level)
                btm_right_img = (max_loc_img[0] + w, max_loc_img[1] + h)

                center_x = max_loc_img[0] + w / 2
                center_y = max_loc_img[1] + h / 2
                centers.append((center_x, center_y))
                rec = cv2.rectangle(img, max_loc_img, btm_right_img, (0, 0, 255), 5)
        
                cv2.imshow('zdjecie pelne', rec)
                cv2.destroyWindow('zoom')


def zoom(event, x, y, flags, params):
    global topleft_x, topleft_y, cropped_img
    if event == cv2.EVENT_LBUTTONDBLCLK:
        topleft_x = x
        topleft_y = y

        min_x = max(x - zoom_level, 0)
        max_x = min(x + zoom_level, img.shape[1])
        min_y = max(y - zoom_level, 0)
        max_y = min(y + zoom_level, img.shape[0])
        cropped_img = img[min_y:max_y, min_x:max_x]

        cv2.imshow('zoom', cropped_img)
        cv2.setMouseCallback('zoom', match)

while(1):
    cv2.namedWindow('zdjecie pelne', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('zdjecie pelne', zoom)
    cv2.imshow('zdjecie pelne', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

if len(centers) == 8:
    with open('pikselowe.txt', 'w') as f:
        for i,center in enumerate(centers):
            f.write(f'{i+1} {center[0]} {center[1]}\n')

tlowe = []
with open('tlowe.txt', 'r') as f:
    for line in f:
        _, x, y = map(float, line.split())
        tlowe.append((x, y))
tlowe = np.array(tlowe)

pikselowe = []
with open('pikselowe.txt', 'r') as f:
    for line in f:
        _, x, y = map(float, line.split())
        pikselowe.append((x, y))
pikselowe = np.array(pikselowe)

A = []
L = []
for xi, yi, Xi, Yi in zip(pikselowe[:,0], pikselowe[:,1], tlowe[:,0], tlowe[:,1]):
    L.append([Xi])
    L.append([Yi])
    A.append([1, xi, yi, 0, 0, 0])
    A.append([0, 0, 0, 1, xi, yi])
A = np.array(A)
L = np.array(L)

X = np.linalg.inv(A.T @ A) @ A.T @ L
X = np.array(X).reshape(-1)
print(f"Wyznaczone parametry:\n {X}\n")

X0 = np.array([X[0], X[3]])
A = np.array([[X[1], X[2]], [X[4], X[5]]])

nowe = []
for xi, yi in pikselowe:
    x, y = X0 + A @ np.array([xi, yi])
    nowe.append((x, y))
nowe = np.array(nowe)
print(f"Obliczone współrzędne:\n {nowe}\n")

v = nowe - tlowe
print(f"Wartości błędów na badanych punktach:\n {v}\n")

m0 = np.sqrt(np.sum(v**2)/(len(v)-6))
print(f"Wartość błędu wyrównania:\n {m0}\n")