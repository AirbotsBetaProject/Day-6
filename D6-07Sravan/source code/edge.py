import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F, ksize=1)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=7)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=7)
    canny = cv2.Canny(frame, 50, 50)
    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("sobely", sobely)
    cv2.imshow("canny", canny)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
video.release()
