# USAGE
# python practice.py --image images/coins.png

# import the necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
        help="Path to the input file")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()











