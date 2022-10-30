from cv2 import COLOR_BGR2GRAY as cv2Gray
from cv2 import cvtColor as cv2Color
from cv2 import imread as cv2ImageRead
from cv2 import resize as cv2Resize
from numpy import all as npAll
import sys
import os

terminal_stream = sys.stdout

chars = ["@", "#", "]", "P", "I", "L", "x", "+", "/", ":", '"', "_", "-", "`", "."]

image = cv2ImageRead(input("image name: "))

image = cv2Color(image, cv2Gray)

image = cv2Resize(image, (image.shape[1] * 5, image.shape [0] * 2))
image = cv2Resize(image, None, fx = 0.1, fy = 0.1)

in1 = input("do you want to keep the generated size? that would be: \n " + str(image.shape[1]) + " letters to the left, and " + str(image.shape[0]) + " letters to the bottom. (y/n)? ")

newscale = (0, 0)
newscalepercent = 100

def askRescaleText(imge):
    img = imge
    if in1 == "y":
        img = cv2Resize(img, (img.shape[1], img.shape[0]))
    elif in1 == "n":
        newscalepercent = int(input("enter the new size in percent (%): "))
        newscale = (int(img.shape[1] * (newscalepercent / 100)), int(img.shape[0] * (newscalepercent / 100)))
        in2 = input("the new scale would be: " + str(newscale[0]) + " and " + str(newscale[1]) + "\n Do you want to use this Size (y/n)? ")
        while in2 != "y":
            if in2 != "n":
                print("please enter one of the characters 'y' (for yes) or 'n' (for no) to continue. ")
            newscalepercent = int(input("enter the new size in percent (%): "))
            newscale = (int(img.shape[1] * (newscalepercent / 100)), int(img.shape[0] * (newscalepercent / 100)))
            in2 = input("the new scale would be: " + str(newscale[0]) + " and " + str(newscale[1]) + "\n Do you want to use this Size (y/n)? ")
        img = cv2Resize(img, newscale)
    else:
        print("please enter one of the characters 'y' (for yes) or 'n' (for no) to continue. ")
        askRescaleText()
    return img
image = askRescaleText(image)

os.system("cls")

print("Progress:")
print("0%                     50%                    100%")

sys.stdout = open("asciiArtGen_output.txt", "w")

percent = 0
printed = 0

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        if npAll(image[y, x] <= 1 * 17) and npAll(image[y, x] >= 0 * 17):
            print(chars[0], end = "")
        if npAll(image[y, x] <= 2 * 17) and npAll(image[y, x] >= 1 * 17):
            print(chars[1], end = "")
        if npAll(image[y, x] <= 3 * 17) and npAll(image[y, x] >= 2 * 17):
            print(chars[2], end = "")
        if npAll(image[y, x] <= 4 * 17) and npAll(image[y, x] >= 3 * 17):
            print(chars[3], end = "")
        if npAll(image[y, x] <= 5 * 17) and npAll(image[y, x] >= 4 * 17):
            print(chars[4], end = "")
        if npAll(image[y, x] <= 6 * 17) and npAll(image[y, x] >= 5 * 17):
            print(chars[5], end = "")
        if npAll(image[y, x] <= 7 * 17) and npAll(image[y, x] >= 6 * 17):
            print(chars[6], end = "")
        if npAll(image[y, x] <= 8 * 17) and npAll(image[y, x] >= 7 * 17):
            print(chars[7], end = "")
        if npAll(image[y, x] <= 9 * 17) and npAll(image[y, x] >= 8 * 17):
            print(chars[8], end = "")
        if npAll(image[y, x] <= 10 * 17) and npAll(image[y, x] >= 9 * 17):
            print(chars[9], end = "")
        if npAll(image[y, x] <= 11 * 17) and npAll(image[y, x] >= 10 * 17):
            print(chars[10], end = "")
        if npAll(image[y, x] <= 12 * 17) and npAll(image[y, x] >= 11 * 17):
            print(chars[11], end = "")
        if npAll(image[y, x] <= 13 * 17) and npAll(image[y, x] >= 12 * 17):
            print(chars[12], end = "")
        if npAll(image[y, x] <= 14 * 17) and npAll(image[y, x] >= 13 * 17):
            print(chars[13], end = "")
        if npAll(image[y, x] <= 15 * 17) and npAll(image[y, x] >= 14 * 17):
            print(chars[14], end = "")
    print()
    percent = int((y / image.shape[0]) * 50)
    if percent != printed:
        for i in range((percent - printed) + 1):
            print("-", file = terminal_stream, end = "", flush = True)
            printed = printed + 1
