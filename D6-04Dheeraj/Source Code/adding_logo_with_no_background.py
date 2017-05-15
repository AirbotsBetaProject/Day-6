import cv2
import numpy as np

img2 = cv2.imread("images.jpg")
img1 = cv2.imread("new quantum.PNG")


rows, cols, channels = img2.shape  # Reading image details
roi = img1[0:rows, 0:cols]


img2g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # converting to grayscale
# defining mask , makes our logo black and background white
ret, mask = cv2.threshold(img2g, 220, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow('mask',mask)

mask_inv = cv2.bitwise_not(mask)  # defining non_masked area
# adds our inv_mask to region of image of main image
img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img_fg = cv2.bitwise_and(img2, img2, mask=mask)  # our logo after adding mask
dst = img_bg+img_fg  # we get our logo with our original image background
# swaps the region of image original image to logo with same backgound
img1[0:rows, 0:cols] = dst


cv2.imshow('res', img1)
cv2.imwrite('result.jpg', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
