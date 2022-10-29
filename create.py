import cv2
import sys
import numpy

terminal_stream = sys.stdout

chars = [
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

image = cv2.imread(input("file name: "))

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

width = int(image.shape[1] * 40 / 100)
height = int(image.shape[0] * 40 / 100)
dim = (width, height)

image = cv2.resize(image, dim)
image = cv2.resize(image, (int(input("letters on the X axis: ")), int(input("letters on the Y axis: "))))

print("Progress:")
print("0%                     50%                    100%")

sys.stdout = open("asciiArtGen_output.txt", "w")

percent = 0
printed = 0

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        if numpy.all(image[y, x] <= 1 * 17) and numpy.all(image[y, x] >= 0 * 17):
            print(chars[0], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[0], file = terminal_stream)
        if numpy.all(image[y, x] <= 2 * 17) and numpy.all(image[y, x] >= 1 * 17):
            print(chars[1], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[1], file = terminal_stream)
        if numpy.all(image[y, x] <= 3 * 17) and numpy.all(image[y, x] >= 2 * 17):
            print(chars[2], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[2], file = terminal_stream)
        if numpy.all(image[y, x] <= 4 * 17) and numpy.all(image[y, x] >= 3 * 17):
            print(chars[3], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[3], file = terminal_stream)
        if numpy.all(image[y, x] <= 5 * 17) and numpy.all(image[y, x] >= 4 * 17):
            print(chars[4], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[4], file = terminal_stream)
        if numpy.all(image[y, x] <= 6 * 17) and numpy.all(image[y, x] >= 5 * 17):
            print(chars[5], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[5], file = terminal_stream)
        if numpy.all(image[y, x] <= 7 * 17) and numpy.all(image[y, x] >= 6 * 17):
            print(chars[6], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[6], file = terminal_stream)
        if numpy.all(image[y, x] <= 8 * 17) and numpy.all(image[y, x] >= 7 * 17):
            print(chars[7], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[7], file = terminal_stream)
        if numpy.all(image[y, x] <= 9 * 17) and numpy.all(image[y, x] >= 8 * 17):
            print(chars[8], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[8], file = terminal_stream)
        if numpy.all(image[y, x] <= 10 * 17) and numpy.all(image[y, x] >= 9 * 17):
            print(chars[9], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[9], file = terminal_stream)
        if numpy.all(image[y, x] <= 11 * 17) and numpy.all(image[y, x] >= 10 * 17):
            print(chars[10], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y, x] <= 12 * 17) and numpy.all(image[y, x] >= 11 * 17):
            print(chars[11], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y, x] <= 13 * 17) and numpy.all(image[y, x] >= 12 * 17):
            print(chars[12], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y, x] <= 14 * 17) and numpy.all(image[y, x] >= 13 * 17):
            print(chars[13], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
        if numpy.all(image[y, x] <= 15 * 17) and numpy.all(image[y, x] >= 14 * 17):
            print(chars[14], end = "")
            # print("x: " + str(x) + " y: " + str(y) + " color: " + str(image[y - 1, x - 1]) + " char: " + chars[10], file = terminal_stream)
    print()
    percent = int((y / image.shape[0]) * 50)
    if percent != printed:
        for i in range((percent - printed) + 1):
            print("-", file = terminal_stream, end = "", flush = True)
            printed = printed + 1
