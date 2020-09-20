import cv2

#Import the selected image
from main import img

# Default image
#img = cv2.imread("Resources/FotosMangoReducidas/IMG_0359.jpg")

# Dimensions of the image
(h, w, d) = img.shape

# Clean resize without afecting the ascpect ratio
print("Put a new dimension of the width to resize the image: ")

try:
    w = int(input()) # Width resize measure
    print("Put a new dimension of the height to resize the image: ")
    h = int(input()) # Height resize measure 
    resized = cv2.resize(img, (w, h))
    cv2.imshow("Original", img)
    cv2.imshow("Fixed Resize", resized)
    cv2.waitKey(0)
except:
    print("Please enter a valid number")
