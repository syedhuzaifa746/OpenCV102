import cv2

image = cv2.imread("car.png")

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply thresholding to get a binary image
blur = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)

#Edge Cascade
canny = cv2.Canny(image, 180, 175)

#Dilating the image
for i in range(0, 3):
    dilated = cv2.dilate(canny, (3,7),iterations= i+1 )
    cv2.imshow("dilated",dilated)
    cv2.waitKey(0)

cropped = image[50:200, 200:400]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)

# Eroding
# Eroded = cv2.erode(dilated, )
# cv2.imshow("Original Image",image)
# cv2.imshow("Gray Image",gray)
# cv2.imshow("Blur Image",blur)
# cv2.imshow("canny edges",canny)
    
# cv2.imshow("dilated",dilated)

cv2.waitKey(0)
cv2.destroyAllWindows