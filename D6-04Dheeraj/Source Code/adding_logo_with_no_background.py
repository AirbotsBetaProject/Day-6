import cv2
import numpy as np
img2=cv2.imread ("images.jpg")
img1=cv2.imread("new quantum.PNG")
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
img2g=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2g, 220,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('mask',mask)
mask_inv=cv2.bitwise_not(mask)
img_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img_fg=cv2.bitwise_and(img2,img2,mask=mask)
dst=img_bg+img_fg
img1[0:rows,0:cols]=dst
cv2.imshow('res',img1)
cv2.imwrite('result.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
