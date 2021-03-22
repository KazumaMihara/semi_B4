import numpy as np
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread("cv2_doc/test01.png",1)

w = img1.shape[0]
h = img1.shape[1]

cv2.rectangle(img1,(0,0),(h,w),(0,0,0),thickness = -1)

d = w/2
h1 = int(d * (1 - (1/(2*(3**0.5)))))
h2 = int(d * (1 + 1 / (3**0.5) - (3**0.5) / 4))
h3 = int(d * (1 + 1 / (3**0.5)))
w_h = h / 2
d_q = d/4
d_h = d/2
a1 = int(w_h)
a2 = int(w_h-d_h)
a3 = int(w_h+d_h)
b2 = int(w_h-d_q)
b3 = int(w_h+d_q)

pts = np.array(((a1,h1),(a2,h3),(a3,h3),(b3,h2),(a1,h3),(b2,h2),(b3,h2)))
cv2.fillPoly(img1,[pts],(0,255,255))
cv2.imshow('Delta_Force',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
