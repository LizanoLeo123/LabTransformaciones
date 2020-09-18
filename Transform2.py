import cv2

# Default image
img = cv2.imread("Resources/FotosMangoReducidas/IMG_0359.jpg")

# Coordenates
xAxisBegin, yAxisBegin, xAxisEnd, yAxisEnd = 0, 0, 0, 0
try:
    print("Enter the begin X axis value: ")
    xAxisBegin = int(input())
    print("Enter the begin Y axis value: ")
    yAxisBegin = int(input())
    print("Enter the end X axis value: ")
    xAxisEnd = int(input())
    print("Enter the end Y axis value: ")
    yAxisEnd = int(input())
except:
    print("Please enter a valid number")

# Image cropped
# imgCropped = img[0:200, 0:500] this was for testing / comparing
imgCropped2 = img[yAxisBegin:yAxisEnd, xAxisBegin:xAxisEnd]

# cv2.imshow("Cropped", imgCropped)
cv2.imshow("Cropped with measurements", imgCropped2)
cv2.waitKey(0)