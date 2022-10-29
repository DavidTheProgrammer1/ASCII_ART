import cv2
import sys
import numpy

terminal_stream = sys.stdout

chars = [  # set the ascii characters
    "@",
    "#",
    "]",
    "P",
    "I",
    "L",
    "x",
    "+",
    "/",
    ":",
    '"',
    "_",
    "-",
    "`",
    "."
]

image = cv2.imread(input("file name: "))  # read the image

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale it 

width = int(image.shape[1] * 40 / 100)
height = int(image.shape[0] * 40 / 100)
dim = (width, height)

image = cv2.resize(image, dim)   # make it smaller
image = cv2.resize(image, (int(input("letters on the X axis: ")), int(input("letters on the Y axis: ")))) # resize so that 1px = 1 ASCII char

print("Progress:")
print("0%                     50%                    100%")  # just the progress bar indicator

sys.stdout = open("asciiArtGen_output.txt", "w")   # all print statements will print to the output file by default

percent = 0
printed = 0

for y in range(image.shape[0]):
    for x in range(image.shape[1]):  # loop thru every pixel
        if numpy.all(image[y - 1, x - 1] <= 1 * 17) and numpy.all(image[y - 1, x - 1] >= 0 * 17):   # detect if pixel is dark or not, the darker the pixel, the other char gets printed
            print(chars[0], end = "") #print the char into the file
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[0], file = terminal_stream)     for debug only
        if numpy.all(image[y - 1, x - 1] <= 2 * 17) and numpy.all(image[y - 1, x - 1] >= 1 * 17):
            print(chars[1], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[1], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 3 * 17) and numpy.all(image[y - 1, x - 1] >= 2 * 17):
            print(chars[2], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[2], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 4 * 17) and numpy.all(image[y - 1, x - 1] >= 3 * 17):
            print(chars[3], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[3], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 5 * 17) and numpy.all(image[y - 1, x - 1] >= 4 * 17):
            print(chars[4], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[4], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 6 * 17) and numpy.all(image[y - 1, x - 1] >= 5 * 17):
            print(chars[5], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[5], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 7 * 17) and numpy.all(image[y - 1, x - 1] >= 6 * 17):
            print(chars[6], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[6], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 8 * 17) and numpy.all(image[y - 1, x - 1] >= 7 * 17):
            print(chars[7], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[7], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 9 * 17) and numpy.all(image[y - 1, x - 1] >= 8 * 17):
            print(chars[8], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[8], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 10 * 17) and numpy.all(image[y - 1, x - 1] >= 9 * 17):
            print(chars[9], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[9], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 11 * 17) and numpy.all(image[y - 1, x - 1] >= 10 * 17):
            print(chars[10], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 12 * 17) and numpy.all(image[y - 1, x - 1] >= 11 * 17):
            print(chars[11], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 13 * 17) and numpy.all(image[y - 1, x - 1] >= 12 * 17):
            print(chars[12], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 14 * 17) and numpy.all(image[y - 1, x - 1] >= 13 * 17):
            print(chars[13], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y - 1, x - 1] <= 15 * 17) and numpy.all(image[y - 1, x - 1] >= 14 * 17):
            print(chars[14], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
    print()    # prints newline into file
    percent = int((y / image.shape[0]) * 50)   # percent reaches from 0 to 50, idk
    if percent != printed:
        for i in range((percent - printed) + 1):
            print("-", file = terminal_stream, end = "", flush = True)   # print a small progress bar
            printed = printed + 1
