import cv2

# Default image
img = cv2.imread("Resources/FotosMangoReducidas/IMG_0359.jpg")

# Dimensions of the image
(h, w, d) = img.shape

# Clean resize without afecting the ascpect ratio
print("Put a new dimension of the width to resize the image: ")
r = 0
try:
    r = int(input()) # Resize measure
    dim = (r, int(h * (r / w)))
    resized = cv2.resize(img, dim)
    cv2.imshow("Original", img)
    cv2.imshow("Aspect Ratio Resize", resized)
    cv2.waitKey(0)
except:
    print("Please enter a valid number")
