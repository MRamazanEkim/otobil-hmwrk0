import cv2
import numpy as np

img = cv2.imread("resim.png")
hvs =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0,70,50])
upper = np.array([10,255,255])

mask = cv2.inRange(hvs, lower, upper)

cv2.imshow("resim", img)
cv2.imshow("sonuc", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()