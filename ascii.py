import os
from tkinter import filedialog as fd
import colorama
from colorama import Fore, Back, Style
import cv2
import numpy as np
from functools import cache
from functools import wraps
import sys
import time
import keyboard
import json
import shutil
import zlib
import subprocess
import asyncio
import math
import ffmpeg
import wave
from pytube import YouTube
import humanize
import mss
import platform
from screeninfo import get_monitors
with open(os.devnull, "w") as devnull:
    stdout = sys.stdout
    sys.stdout = devnull
    from pygame import mixer
    sys.stdout = stdout

def get_os():
    if platform.system() == "Windows":
        return "win"
    elif platform.system() == "Linux":
        return "unix"
    elif platform.system() == "Darwin":
        return "unix"

def hide_file(file):
    if get_os() == "win":
        subprocess.check_call(["attrib", "+H", file])

def resize_terminal_window(x, y):
    if get_os() == "win":
        os.system(f"mode con: cols={x} lines={y}")

def sync(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        async def f(*args, **kwargs):
            pass
        f = func
        asyncio.run(f(*args, **kwargs))
    return wrapper

def Gen_Image(image):
    
    if image.endswith(".txt"):
        img = open(image).read()
    elif image.endswith(".html"):
        html = open(image).read()
        s_index = html.index("<body>") + 6
        html_arr = list(html)
        html_arr = html_arr[s_index:]
        html = ""
        for c in html_arr:
            html += c
        html = html.replace("</body>", "")
        html = html.replace("</html>", "")
        html = html.replace("\n", "")
        html = html.replace("<p>", "")
        html = html.replace("</p>", "\n")
        img = html
    else:
        raise ValueError("Image has to be a .txt or a .html File")
        
    inversed_chars = {
        "`": 17,
        ".": 34, "-": 51,
        "_": 68, '"': 85, 
        ":": 102, "/": 119, 
        "+": 136, "x": 153,
        "L": 170, "I": 187,
        "P": 204, "]": 221,
        "#": 238, "@": 255
    }
    chars = {
        "`": 255,
        ".": 238, "-": 221,
        "_": 204, '"': 187,
        ":": 170, "/": 153,
        "+": 136, "x": 119,
        "L": 102, "I": 85,
        "P": 68, "]": 51,
        "#": 34, "@": 17
    }
    
    img_split_lines = img.split("\n")
    lines_chars = []
    
    for line in img_split_lines:
        lines_chars.append([*line])
    
    lines_chars.pop()
    
    height = int(len(lines_chars))
    width = len(lines_chars[0])
    blank_image = np.zeros((height, width, 1), np.uint8)
    
    for y in range(height):
        for x in range(width):
            if y > 290:
                print(y, x)
            blank_image[y, x] = (chars[lines_chars[y][x]])
            
    blank_image = cv2.resize(blank_image, (None, None), fx = 1, fy = 2.5)
    
    cv2.imwrite("output_image.png", blank_image)

def Gen_ASCII_Image(imgname):
    
    colorama.init(autoreset = True)
    
    print(f"{Fore.LIGHTGREEN_EX}[!] Starting Ascii Art Generation Process...")
    
    terminal_stream = sys.stdout
    chars = ["@", "#", "]", "P", "I", "L", "x", "+", "/", ":", '"', "_", "-", ".", "`"]
    
    image = cv2.imread(imgname)
    image = cv2.cvtColor(image, 6)
    image = cv2.resize(image, (image.shape[1] * 5, image.shape [0] * 2))
    image = cv2.resize(image, None, fx = 0.1, fy = 0.1)
    def askRescaleText(imge):
        in1 = input(f"{Fore.LIGHTBLACK_EX}[?] Do you want to keep the generated size? that would be: \n    " + str(imge.shape[1]) + f"{Fore.LIGHTBLACK_EX} letters to the left, and " + str(imge.shape[0]) + f"{Fore.LIGHTBLACK_EX} letters to the bottom. (y/n)? ")
        img = imge
        if in1 == "y":
            img = cv2.resize(img, (img.shape[1], img.shape[0]))
        elif in1 == "n":
            newscalepercent = int(float((input(f"{Fore.LIGHTBLACK_EX}[?] Enter the new size in percent (%): "))))
            newscale = (int(img.shape[1] * (newscalepercent / 100)), int(img.shape[0] * (newscalepercent / 100)))
            in2 = input(f"{Fore.LIGHTBLACK_EX}[?] The new scale would be: " + str(newscale[0]) + f"{Fore.LIGHTBLACK_EX} and " + str(newscale[1]) + f"{Fore.LIGHTBLACK_EX}\n    Do you want to use this Size (y/n)? ")
            while in2 != "y":
                if in2 != "n":
                    print(f"{Fore.LIGHTRED_EX}[!] Please enter one of the characters 'y' (for yes) or 'n' (for no) to continue. ")
                newscalepercent = int(float(input(f"{Fore.LIGHTBLACK_EX}[?] enter the new size in percent (%): ")))
                newscale = (int(img.shape[1] * (newscalepercent / 100)), int(img.shape[0] * (newscalepercent / 100)))
                in2 = input(f"{Fore.LIGHTBLACK_EX}[?] The new scale would be: " + str(newscale[0]) + f"{Fore.LIGHTBLACK_EX} and " + str(newscale[1]) + f"{Fore.LIGHTBLACK_EX}\n    Do you want to use this Size (y/n)? ")
            img = cv2.resize(img, newscale)
        else:
            print(f"{Fore.LIGHTRED_EX}[!] Please enter one of the characters 'y' (for yes) or 'n' (for no) to continue. ")
            image = askRescaleText(img)
        return img
    image = askRescaleText(image)
    html = False
    if input(f"{Fore.LIGHTBLACK_EX}[?] Invert the colors? (y/n)? ") == "y":
        chars = chars[::-1]
    if input(f"{Fore.LIGHTBLACK_EX}[?] Save Ascii Art inside HTML document (Is able to Display larger sizes)? (y/n)? ") == "y":
        html = True
    if image.shape[1] >= 750:
        if not html:
            print(f"{Fore.LIGHTYELLOW_EX}[!] Forcing to save as HTML document because image is too large.")
            html = True
    print(f"{Fore.LIGHTGREEN_EX}[!] Starting Generation of Ascii Art...\n")
    if not html:
        sys.stdout = open("asciiArtGen_output.txt", "w")
    percent = 0
    printed = 0
    todo = 49
    donestr = "#"    # █
    todostr = "-"    # ░
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
    print(f"{Fore.LIGHTGREEN_EX}\n[!] Finished Ascii Art...", file = terminal_stream)
    if not html:
        print(f"{Fore.LIGHTGREEN_EX}[!] Finished writing Ascii Art to text file...", file = terminal_stream)
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
        print(f"{Fore.LIGHTGREEN_EX}[!] Preparing image to save...")
        for l in lines:
            htmlpage += "<p>" + l.strip() + "</p>\n"
        htmlpage += """
</body>
</html>"""
        print(f"{Fore.LIGHTGREEN_EX}[!] Saving image to HTML document...")
        with open("asciiArtGen_output.html", "w") as out:
            out.write(htmlpage)
        print(f"{Fore.LIGHTGREEN_EX}[!] Finished saving Ascii Art to HTML...")
        print(f"{Fore.LIGHTGREEN_EX}[!] Opening Ascii Art...")
        os.system("start asciiArtGen_output.html")
    else:
        sys.stdout.close()
        print(f"{Fore.LIGHTGREEN_EX}\n[!] Opening Ascii Art...", file = terminal_stream)
        os.system("notepad asciiArtGen_output.txt")
        sys.stdout = terminal_stream

def ReadVideoFromJSON(filen):
    colorama.init(autoreset = False)
    print(f"{Fore.LIGHTWHITE_EX}", end = "\r")
    if filen.endswith(".asciivid"):
        if os.path.isdir("ascii_video_out"):
            for f in os.listdir("ascii_video_out"):
                os.remove("ascii_video_out/" + f)
            os.removedirs("ascii_video_out")
        os.makedirs("ascii_video_out")
        hide_file("ascii_video_out")
        os.rename(filen, filen.replace(".asciivid", ".zip"))
        shutil.unpack_archive(filen.replace(".asciivid", ".zip"), "ascii_video_out")
        os.rename(filen.replace(".asciivid", ".zip"), filen)
        jsonfile = open("ascii_video_out/video.json", "rb")
        asciidict = json.loads(zlib.decompress(jsonfile.read()).decode())
    else:
        jsonfile = open(filen, "r", encoding = "cp437")
        asciidict = json.loads(jsonfile.read())
        print(f"{Fore.LIGHTYELLOW_EX}[!] Old File format detected.")
    fps = asciidict["fps"]
    sizeX = asciidict["sizeX"]
    sizeY = asciidict["sizeY"]
    frames = asciidict["frames"]
    crnt_frame = 0
    mixer.init()
    snd = mixer.Sound("ascii_video_out/audio.mp3")
    resize_terminal_window(sizeX, sizeY)
    print(f"{Fore.LIGHTGREEN_EX}[!] Ready to Play! Space key to play. ")
    while True:
        if keyboard.read_key() == "space":
            break
    st_tme = time.time()
    snd.play()
    try:
        while crnt_frame < len(frames):
            des_frame = int((time.time() - st_tme) * fps)
            if not des_frame == crnt_frame:
                print(frames[des_frame])
                crnt_frame = des_frame
    except:
        mixer.music.stop()

def Live_Video():
    colorama.init(autoreset = True)
    chars = ["@", "#", "]", "P", "I", "L", "x", "+", "/", ":", '"', "_", "-", ".", " "]
    chars = chars[::-1]
    vidcap = cv2.VideoCapture(0)
    fx, fy = 0, 0
    ret, stestframe = vidcap.read()
    cv2.waitKey(0)
    testframe = stestframe
    testframe = cv2.resize(testframe, None, fx = 2.5, fy = 1)
    last_tf_size = testframe.shape
    terx = os.get_terminal_size().columns
    tery = os.get_terminal_size().lines
    tersize = os.get_terminal_size()
    while (testframe.shape[1] > terx) or (testframe.shape[0] > tery):
        testframe = cv2.resize(testframe, None, fx = 0.98, fy = 0.98)
        if testframe.shape[1] == last_tf_size[1]:
            break
        if testframe.shape[0] == last_tf_size[0]:
            break
        last_tf_size = testframe.shape
    sx = testframe.shape[1]
    sy = testframe.shape[0]
    print(f"{Fore.LIGHTGREEN_EX}Press Space Key to Start!")
    while True:
        if keyboard.read_key() == "space":
                break
    @cache
    def processPixel(b):
        for ii in range(15):
            if b <= (ii + 1) * 17 and b >= ii * 17:
                return chars[ii]
    def processFrame(fr):
        outs = ""
        for y in range(fr.shape[0]):
            for x in range(fr.shape[1]):
                outs += processPixel(int(fr[y, x]))
            outs += "\n"
        return outs
    while True:
        ret, frame = vidcap.read()
        if not ret:
            break
        _tersize = os.get_terminal_size()
        if (not _tersize.columns == tersize.columns) or (not _tersize.lines == tersize.lines):
            tersize = _tersize
            terx = tersize.columns
            tery = tersize.lines
            testframe = stestframe
            testframe = cv2.resize(testframe, None, fx = 2.5, fy = 1)
            while (testframe.shape[1] > terx) or (testframe.shape[0] > tery):
                testframe = cv2.resize(testframe, None, fx = 0.98, fy = 0.98)
                if testframe.shape[1] == last_tf_size[1]:
                    break
                if testframe.shape[0] == last_tf_size[0]:
                    break
                last_tf_size = testframe.shape
                sx = testframe.shape[1]
                sy = testframe.shape[0]
        frame = cv2.resize(frame, (sx, sy))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(processFrame(frame))

def Live_Screen():
    colorama.init(autoreset = True)
    chars = ["@", "#", "]", "P", "I", "L", "x", "+", "/", ":", '"', "_", "-", ".", " "]
    chars = chars[::-1]
    width, height = get_monitors()[0].width, get_monitors()[0].height
    sct = mss.mss()
    monitor = {"top": 0, "left": 0, "width": width, "height": height}
    stestframe = np.array(sct.grab(monitor))
    cv2.waitKey(0)
    testframe = stestframe
    testframe = cv2.resize(testframe, None, fx = 2.5, fy = 1)
    last_tf_size = testframe.shape
    terx = os.get_terminal_size().columns
    tery = os.get_terminal_size().lines
    tersize = os.get_terminal_size()
    while (testframe.shape[1] > terx) or (testframe.shape[0] > tery):
        testframe = cv2.resize(testframe, None, fx = 0.98, fy = 0.98)
        if testframe.shape[1] == last_tf_size[1]:
            break
        if testframe.shape[0] == last_tf_size[0]:
            break
        last_tf_size = testframe.shape
    sx = testframe.shape[1]
    sy = testframe.shape[0]
    print(f"{Fore.LIGHTGREEN_EX}Press Space Key to Start!")
    while True:
        if keyboard.read_key() == "space":
                break
    @cache
    def processPixel(b):
        for ii in range(15):
            if b <= (ii + 1) * 17 and b >= ii * 17:
                return chars[ii]
    def processFrame(fr):
        outs = ""
        for y in range(fr.shape[0]):
            for x in range(fr.shape[1]):
                outs += processPixel(int(fr[y, x]))
            outs += "\n"
        return outs
    while True:
        
        frame = np.array(sct.grab(monitor))
        
        _tersize = os.get_terminal_size()
        if (not _tersize.columns == tersize.columns) or (not _tersize.lines == tersize.lines):
            tersize = _tersize
            terx = tersize.columns
            tery = tersize.lines
            testframe = stestframe
            testframe = cv2.resize(testframe, None, fx = 2.5, fy = 1)
            while (testframe.shape[1] > terx) or (testframe.shape[0] > tery):
                testframe = cv2.resize(testframe, None, fx = 0.98, fy = 0.98)
                if testframe.shape[1] == last_tf_size[1]:
                    break
                if testframe.shape[0] == last_tf_size[0]:
                    break
                last_tf_size = testframe.shape
                sx = testframe.shape[1]
                sy = testframe.shape[0]
        frame = cv2.resize(frame, (sx, sy))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(processFrame(frame))

@sync
async def Gen_Ascii_Art_Video(video, FPS = None, Processes = 1, Dest = "", _Debug = False):
    
    colorama.init(autoreset = False)
    
    if FPS == None:
        fps = math.floor(cv2.VideoCapture(video).get(5))
    elif FPS == "":
        fps = math.floor(cv2.VideoCapture(video).get(5))
    else:
        fps = int(FPS)
    chars = ["@", "#", "]", "P", "I", "L", "x", "+", "/", ":", '"', "_", "-", ".", " "]
    if Processes == "":
        Workers = 1
    elif Processes == None:
        Workers = 1
    else:
        Workers = int(Processes)
    chars = chars[::-1]
    vidlen = int(cv2.VideoCapture(video).get(7) / cv2.VideoCapture(video).get(5))
    vidfps = int(cv2.VideoCapture(video).get(5))
    vidcap = vidcap = cv2.VideoCapture(video)
    frameX = 0
    frameY = 0
    if fps > vidfps:
        raise ValueError("Given Fps (" + str(fps) + ") higher than Original Video Fps (" + str(vidfps) + ")") 
    def GetFrameImage(frame, sx = None, sy = None):
        if _Debug:
            print("setting cap frame")
        vidcap.set(1, frame)
        if _Debug:
            print("getting frame image")
        _, img = vidcap.read()
        if _Debug:
            print("downscaling frame image")
        if not sx == None and not sy == None:
            img = cv2.resize(img, (sx, sy))
        if _Debug:
            print("grayscale image")
        img = cv2.cvtColor(img, 6) 
        return img
    @cache
    def processPixel(b):
        for ii in range(15):
            if b <= (ii + 1) * 17 and b >= ii * 17:
                return chars[ii]
    def processFrame(fr):
        if _Debug:
            print("Processing frame")
        outs = ""
        for y in range(fr.shape[0]):
            for x in range(fr.shape[1]):
                outs += processPixel(int(fr[y, x]))
            outs += "\n"
        return outs
    # @sync
    async def processFrameByIndex(index = 0):
        if _Debug:
            print("Getting frame")
        frm = GetFrameImage(index, frameX, frameY)
        outstrn = processFrame(frm)
        if _Debug:
            print("Adding output to list")
        arr[index] = outstrn
        dic["frames"] = arr
    ran = range(0, vidlen * fps, Workers)
    global arr, dic 
    arr = [None] * vidlen * fps * Workers
    dic = {}
    jsonfile = open("video.json", "wb")
    hide_file("video.json")
    print(f"{Fore.LIGHTGREEN_EX}[!] The video will be generated in the size of this Window. \n    Please resize the window so that the video is as big as you want. \n    After that, press space to continue with the generation process.")
    print(f'[!] Note: if the code says something like "mmco: unref short failure", \n    that just means that the video is corrupted at the current frame. \n    But this doesnt really affect anything. {Fore.LIGHTWHITE_EX}')
    while True:
        if keyboard.read_key() == "space":
                break
    terCols = os.get_terminal_size().columns
    terLins = os.get_terminal_size().lines
    
    audio, _ = (ffmpeg.input(video).output("-", format = "s16le", acodec = "pcm_s16le", loglevel = "quiet").overwrite_output().run(capture_stdout = True))
    
    with wave.open("audio.wav", "wb") as wavfile:
        wavfile.setparams((2, 2, 44100, 0, "NONE", "NONE"))
        wavfile.writeframes(audio)
    
    (ffmpeg.input("audio.wav").output("audio.mp3", acodec = "libmp3lame", loglevel = "quiet").run())
    
    os.remove("audio.wav")
    
    testfrme = GetFrameImage(0)
    testfrme = cv2.resize(testfrme, (testfrme.shape[1] * 5, testfrme.shape[0] * 2))
    while (testfrme.shape[1] > terCols) or (testfrme.shape[0] > terLins):
            testfrme = cv2.resize(testfrme, None, fx = 0.98, fy = 0.98)
    frameX = testfrme.shape[1]
    frameY = testfrme.shape[0]
    framesleft = cv2.VideoCapture(video).get(7)
    for i in ran:
        processes = []
        if framesleft < Workers:
            for ii in range(framesleft):
                p = asyncio.create_task(processFrameByIndex(index = i + ii))
                processes.append(p)
            for p in processes:
                await p
                framesleft -= 1
        else:
            for ii in range(Workers):
                p = asyncio.create_task(processFrameByIndex(index = i + ii))
                processes.append(p)
            for p in processes:
                await p
                framesleft -= 1
        print("Rendering Frame " + str(i) + "/" + str(len(ran) * Workers))
    dic["fps"] = fps
    dic["sizeX"] = testfrme.shape[1]
    dic["sizeY"] = testfrme.shape[0]
    compressed = zlib.compress(json.dumps(dic).replace('"', '\"').encode())
    jsonfile.write(compressed)
    jsonfile.close()
    
    os.makedirs(Dest + "\\out", exist_ok = True)
    
    hide_file(Dest + "\\out")
    
    shutil.move("video.json", Dest + "\\out")
    
    shutil.move("audio.mp3", Dest + "\\out")
    
    os.system(f"cd {Dest}")
    
    shutil.make_archive(video, "zip", Dest + "\\out")
    
    shutil.rmtree(Dest + "\\out")
    
    os.rename(Dest + video + ".zip", Dest + video + ".asciivid")
    
    ReadVideoFromJSON(Dest + "\\" + os.path.basename(video) + ".asciivid")

def download_yt(url):

    yt = YouTube(url)

    streams = yt.streams.filter(progressive = True, file_extension = "mp4")

    i = 1
    for stream in streams:
        print(f"{Fore.LIGHTGREEN_EX}[!] Video Source {Fore.LIGHTWHITE_EX}[ {i} ]{Fore.LIGHTGREEN_EX}: \n    fps: {stream.fps}\n    resolution: {stream.resolution}\n    size: {humanize.naturalsize(stream.filesize)}")
        i += 1

    stream = streams[int(input(f"{Fore.RESET}[?] Which Source to get Video from? ")) - 1]

    print(f"{Fore.LIGHTGREEN_EX}[!] Downloading video, Size:", humanize.naturalsize(stream.filesize))
    stream.download()
    print(f"{Fore.LIGHTGREEN_EX}[!] Download complete.")

    return stream.default_filename

def open_img_file():
    f = fd.askopenfilename(title = "Select a Image", 
                            filetypes = [
                                ("Supported Images", "*.jpg *.jpeg *.jpg *.bmp *.dib *.jp2 *.png *.webp *.pbm *.pgm *.ppm *.pxm *.pnm *.pfm *.sr *.ras *.tiff *.tif *.exr *.hdr *.pic")
                            ])
    return os.path.abspath(f)
def open_vid_file():
    f = fd.askopenfilename(title = "Select a Video",
                            filetypes = [
                                ("Video", "*.*")
                            ])
    return os.path.abspath(f)
def open_json_file():
    f = fd.askopenfilename(title = "Select the Json File Containing the Video",
                            filetypes = [
                                ("Custom Video File", "*.asciivid *.json")
                            ])
    return os.path.abspath(f)
def open_txt_file():
    f = fd.askopenfilename(title = "Select the File containing the ASCII Art",
                            filetypes = [
                                ("Text File", "*.txt")
                            ])
    return os.path.abspath(f)
def show_error_message(err):
    print(f"""{Fore.LIGHTRED_EX}
[!] Generating ASCII Art Returned an Error:
    {err}
[!] Usually Code retrieved invalid user input.
    Try using only numbers when entering a input, without any letters.
    Otherwise it might be caused by a bug in the code.""")
    print()

def show_banner():

    quiet = ""
    try:
        quiet = sys.argv[1]
    except:
        pass
    if not quiet == "q":
        os.system("cls")
        banner = r"""
             ___                                                 ___
            /   \         ____    ____   _   _                  /   \      ___     _______
           / / \ \       /  __|  / ___| | | | |                / / \ \    |    \  |__   __|
          / /___\ \      \  \   / /     | | | |               / /___\ \   |   _/     | |
         / _______ \   __/  /   \ \___  | | | |              / ______\ \  | |\ \     | |
        /_/       \_\ |____/     \____| |_| |_|   ________  /_/       \_\ |_| \_\    |_|
                                                 |________|   """ + f"""{Fore.LIGHTBLACK_EX}(This is not the actual Art)  """
        credentials = """
                       A simple ASCII Art creation Code made by David L.""" 
        helpd = """
                                    type "help" for help"""
        print(f"{Fore.RED}{banner}")
        print(f"{Fore.RED}{Style.BRIGHT}{credentials}", flush = True, end = "")
        print(f"{Fore.LIGHTRED_EX}{Style.DIM}{helpd}")

def main():
    os.system("title Ascii_Art")
    colorama.init(autoreset = True)
    show_banner()

    while True:
        inp = input(f"{Fore.LIGHTBLACK_EX}Ascii_Art $> ").strip()
        if inp == "image":
            try:
                Gen_ASCII_Image(open_img_file())
            except Exception as e:
                show_error_message(e)
        elif inp == "video":
            try:
                Gen_Ascii_Art_Video(open_vid_file(), input("[?] FPS? (leave empty for max) "), Dest = os.getcwd()) # input("[?] Processes to work? Default is 1, \n    for mid-tier devices is 2 recommended, \n    but if you have a high-tier PC, you can set higher numbers. "),
            except Exception as e:
                show_error_message(e)
        elif inp == "live":
            try:
                Live_Video()
            except Exception as e:
                show_error_message(e)
        elif inp == "screen":
            try:
                Live_Screen()
            except Exception as e:
                show_error_message(e)
        elif inp == "youtube":
            try:
                Gen_Ascii_Art_Video(download_yt(input("[?] YouTube Video URL: ")), input("[?] FPS? (leave empty for max) "), Dest = os.getcwd()) # input("[?] Processes to work? Default is 1, \n    for mid-tier devices is 2 recommended, \n    but if you have a high-tier PC, you can set higher numbers. "),
            except Exception as e:
                show_error_message(e)
        elif inp == "debug_video":
            try:
                Gen_Ascii_Art_Video(open_vid_file(), input("[?] FPS? (leave empty for max) "), Dest = os.getcwd(), _Debug = True) # input("[?] Processes to work? Default is 1, \n    for mid-tier devices is 2 recommended, \n    but if you have a high-tier PC, you can set higher numbers. "),
            except Exception as e:
                show_error_message(e)
        elif inp == "reverse":
            try:
                Gen_Image(open_txt_file())
            except Exception as e:
                show_error_message(e)
        elif inp == "play":
            try:
                v = open_json_file()
                ReadVideoFromJSON(v)
            except Exception as e:
                show_error_message(e)
        elif inp == "":
            pass
        elif inp == "help":
            print(f"""{Fore.WHITE}
[!] This is the ASCII Art Command Help.
    The currently supported commands are:
      help    -   Show this help
      image   -   Generate ASCII Art Image
      reverse -   Generate Image from ASCII Art
      video   -   Generate ASCII Art Video
      live    -   Render ASCII Art Live from Webcam
      screen  -   Render ASCII Art Live from Screen
      youtube -   Download YouTube Video and generate a ASCII Art
      play    -   Play ASCII Art Video from File
                  """)
        else:
            print(f"""{Fore.LIGHTRED_EX}
[!] Command not Recognized.
    Type "help" for Information about available Commands.
                  """)
if __name__ == "__main__":
    main()
