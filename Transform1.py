import cv2

img = cv2.imread("Resources/FotosMangoReducidas/IMG_0359.jpg", cv2.IMREAD_UNCHANGED)

# Ask for x and y pixels
xAxis = 0
yAxis = 0
try:
    print("Enter the x axis value: ")
    xAxis = int(input())
    print("Enter the y axis value: ")
    yAxis = int(input())
except:
    print("Please enter a valid number")

# Show RGB vector for those pixels
b,g,r = (img[xAxis, yAxis])
print ("Red:" + str(r))
print ("Green:" + str(g))
print ("Blue:" + str(b))

# End of the code