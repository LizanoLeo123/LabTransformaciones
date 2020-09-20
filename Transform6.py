import cv2

#Import the selected image
from main import img

# Default image
#img = cv2.imread("Resources/FotosMangoReducidas/IMG_0359.jpg")

# Dimensions of the image
(h, w, d) = img.shape

# Image smoothing using Gaussian blur kernel
print("Enter blur level: ")
try:
    bl = int(input()) # Resize measure
    if bl%2 > 0:
        blurred = cv2.GaussianBlur(img, (bl, bl), 0)
        cv2.imshow("Original", img)
        cv2.imshow("Blurred", blurred)
        cv2.waitKey(0)
    else:
        print("The kernel must be a odd number")
except ex:
    print("Please enter a valid number")
