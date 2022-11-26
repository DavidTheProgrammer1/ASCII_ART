import os
import sys
from functools import cache
from colorama import Back, Fore
from colorama import init as coloramaInit
from cv2 import cvtColor as cv2Color
from cv2 import imread as cv2ImageRead
from cv2 import resize as cv2Resize

print("")

def GenerateASCII(imgname) -> None:
    
    coloramaInit(autoreset = True)
    
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Starting Ascii Art Generation Process...")
    
    terminal_stream = sys.stdout
    chars = ["@", "#", "]", "P", "I", "L", "x", "+", "/", ":", '"', "_", "-", ".", "`"]
    
    image = cv2ImageRead(imgname)
    image = cv2Color(image, 6)
    image = cv2Resize(image, (image.shape[1] * 5, image.shape [0] * 2))
    image = cv2Resize(image, None, fx = 0.1, fy = 0.1)
    def askRescaleText(imge):
        in1 = input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}[?] Do you want to keep the generated size? that would be: \n    " + str(imge.shape[1]) + f"{Back.BLACK}{Fore.LIGHTBLACK_EX} letters to the left, and " + str(imge.shape[0]) + f"{Back.BLACK}{Fore.LIGHTBLACK_EX} letters to the bottom. (y/n)? ")
        img = imge
        if in1 == "y":
            img = cv2Resize(img, (img.shape[1], img.shape[0]))
        elif in1 == "n":
            newscalepercent = int(float((input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}[?] Enter the new size in percent (%): "))))
            newscale = (int(img.shape[1] * (newscalepercent / 100)), int(img.shape[0] * (newscalepercent / 100)))
            in2 = input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}[?] The new scale would be: " + str(newscale[0]) + f"{Back.BLACK}{Fore.LIGHTBLACK_EX} and " + str(newscale[1]) + f"{Back.BLACK}{Fore.LIGHTBLACK_EX}\n    Do you want to use this Size (y/n)? ")
            while in2 != "y":
                if in2 != "n":
                    print(f"{Back.BLACK}{Fore.LIGHTRED_EX}[!] Please enter one of the characters 'y' (for yes) or 'n' (for no) to continue. ")
                newscalepercent = int(float(input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}[?] enter the new size in percent (%): ")))
                newscale = (int(img.shape[1] * (newscalepercent / 100)), int(img.shape[0] * (newscalepercent / 100)))
                in2 = input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}[?] The new scale would be: " + str(newscale[0]) + f"{Back.BLACK}{Fore.LIGHTBLACK_EX} and " + str(newscale[1]) + f"{Back.BLACK}{Fore.LIGHTBLACK_EX}\n    Do you want to use this Size (y/n)? ")
            img = cv2Resize(img, newscale)
        else:
            print(f"{Back.BLACK}{Fore.LIGHTRED_EX}[!] Please enter one of the characters 'y' (for yes) or 'n' (for no) to continue. ")
            image = askRescaleText(img)
        return img
    image = askRescaleText(image)
    html = False
    if input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}[?] Invert the colors? (y/n)? ") == "y":
        chars = chars[::-1]
    if input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}[?] Save Ascii Art inside HTML document (Is able to Display larger sizes)? (y/n)? ") == "y":
        html = True
    if image.shape[1] >= 750:
        if not html:
            print(f"{Back.BLACK}{Fore.LIGHTYELLOW_EX}[!] Forcing to save as HTML document because image is too large.")
            html = True
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Starting Generation of Ascii Art...\n")
    if not html:
        sys.stdout = open("asciiArtGen_output.txt", "w")
    percent = 0
    printed = 0
    todo = 49
    donestr = "#"    # or █
    todostr = "-"    # or ░
    loadinganim = ["|", "|", "/", "/", "-", "-", "\\", "\\"]
    progrss = 0
    line = ""
    lines = []
    @cache
    def processPixel(b):
        for ii in range(15):
            if b <= (ii + 1) * 17 and b >= ii * 17:
                return chars[ii]
    for y in range(image.shape[0]):
        line = ""
        for x in range(image.shape[1]):
            pix = processPixel(int(image[y, x]))
            if html:
                line += pix
            else:
                print(pix, end = "")
        if html:
            lines.append(line)
        else:
            print()
        percent = int((y / image.shape[0]) * 50)
        if percent != printed:
            for _ in range((percent - printed) + 1):
                if progrss == 7:
                    progrss = 0
                else:
                    progrss = progrss + 1
                print(Back.BLACK + Fore.WHITE + "Progress: [" + donestr * printed + todostr * todo + "]  [" + loadinganim[progrss] + "] ", file = terminal_stream, end = "\r", flush = True)
                printed = printed + 1
                todo = todo - 1
    print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}\n[!] Finished Ascii Art...", file = terminal_stream)
    if not html:
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Finished writing Ascii Art to text file...", file = terminal_stream)
    if html:
        htmlpage = """
<!DOCTYPE html>
<head>
    <title>""" + imgname + """</title>
    <style>
        p {
            white-space: nowrap;
            font-family: monospace;
            display: inline;
        }
    </style>
</head>
<body>"""
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Preparing image to save...")
        for l in lines:
            htmlpage += "<p>" + l.strip() + "</p>\n"
        htmlpage += """
</body>
</html>"""
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Saving image to HTML document...")
        with open("asciiArtGen_output.html", "w") as out:
            out.write(htmlpage)
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Finished saving Ascii Art to HTML...")
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Opening Ascii Art...")
        os.system("start asciiArtGen_output.html")
    else:
        sys.stdout.close()
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}\n[!] Opening Ascii Art...", file = terminal_stream)
        os.system("notepad asciiArtGen_output.txt")
        sys.stdout = terminal_stream
