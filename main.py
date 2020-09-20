# Laboratório Ruido en Imágenes
# Danilo Chaves, Leonardo Lizano

import cv2
import importlib
import sys

# Set default image
imgSource = "Resources/FotosMangoReducidas/IMG_0359.jpg"
img = cv2.imread(imgSource)

switcher = {
    1: "Transform1",
    2: "Transform2",
    3: "Transform3",
    4: "Transform4",
    5: "Transform5",
    6: "Transform6"
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Laboratório Ruido en Imágenes" +
          "\nDanilo Chaves, Leonardo Lizano")
    while True:
        print("-" * 50 +
            "\nCurrent image: " + imgSource+
            "\n " + "-" * 50 +
            "\nSelect an option: " +
            "\n1. Show RGB values of a pixel" +
            "\n2. Extract ROI" +
            "\n3. Resize image" +
            "\n4. Resize image keeping aspect ratio" +
            "\n5. Rotate image" +
            "\n6. Smooth image (Blur)" +
            "\n0. Exit" +
            "\n>>")
        userInput = -1 
        try:
            userInput = int(input())
            if userInput > 0 and userInput < 7:
                importlib.import_module(switcher.get(userInput))
            elif userInput == 0:
                sys.exit()
            else:
                print("Invalid option")  
        except:
            print("Invalid option")



