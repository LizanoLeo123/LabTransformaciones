import cv2

#Import the selected image
from main import img

# Default image
#img = cv2.imread("Resources/FotosMangoReducidas/IMG_0359.jpg")

#Image rotation to a user espcified degrees
print("Put the degrees to rotate the image: ")
rd = 0
try:
    rd = int(input()) #Rotation degree
    (h, w, d) = img.shape
    center = (w//2, h//2)
    rMatrix = cv2.getRotationMatrix2D(center, rd, 1.0)
    rotated = cv2.warpAffine(img, rMatrix, (w, h))
    cv2.imshow("Original", img)
    cv2.imshow("Rotation", rotated)
    cv2.waitKey(0)
except:
    print("Please enter a valid number")
    
