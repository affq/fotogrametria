import numpy as np
import cv2

img = cv2.imread(r'mario.png')
imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cx, cy - połowa szerokości i wysokości obrazu; punkt centralny obrazu
#fx, fy - ogniskowa obrazu
fx = fy = 4680

K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

#punkty pomierzone na 2 zdjęciach float32

pkt1 = np.float32([[],[],[]])
pkt2 = np.float32([[],[],[]])

E, mask = cv2.findEssentialMat(pkt1, pkt2, K, method=xxx)

_,R,t,_ = cv2.recoverPose(E, pkt1, pkt2, K, mask=mask)

P1 = np.hstack((np.eye(3), np.zeros(3,1)))
P2 = np.hstack((R, t))   

P1 = K@P1
P2 = K@P2

points3D = cv2.triangulatePoints(P1, P2, pkt1, pkt2)
points3D = points3D/points3D[3]
points3D = points3D[:3,:].T 

#na ocene 3 transofrmacja anificzna
#na ocene 4 pomiar na 2 obrazach - otwieramy 2 okiienka, klikamy na lewej pojawia sie zoom; na zommie mierzymy; przechodzimy na 2 obraz, klikamy  wten sam punkt, też zoom; dokladnie mierzymy na zoomie ten sam puntk; wykonujmy orientacje wzajemna; pobieramy wspolrzedne z elwego i prawego zdjecia; wyznaczamy macierz rotacji i translacju
#na ocene 4.5 po orientacji wzajemnej mierzymy punkty na 1 i 2 obrazie, wyznaczamy wspolrzedne 3d punktow i zapisywac je do pliku tekstowego lub ascii
#na ocene 5 modul do wyznaczenie elementow orientacji zewnetrznej