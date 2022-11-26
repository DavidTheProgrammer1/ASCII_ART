import os
import shutil
from functools import cache
from json import dumps as jsonDumps
from json import loads as jsonLoads
from time import sleep as sleepSeconds
import asyncio
from colorama import Fore, Back
from colorama import init as coloramaInit
from cv2 import cvtColor as cv2Color
from cv2 import VideoCapture as cv2VideoCapture
from cv2 import resize as cv2Resize
import keyboard

def ReadVideoFromJSON(filen):
    coloramaInit(autoreset = False)
    print(f"{Back.BLACK}{Fore.LIGHTWHITE_EX}", end = "\r")
    jsonfile = open(filen, "r", encoding = "cp437")
    asciidict = jsonLoads(jsonfile.read())
    fps = asciidict["fps"]
    sizeX = asciidict["sizeX"]
    sizeY = asciidict["sizeY"]
    os.system(f"mode con: cols={sizeX} lines={sizeY}")
    for f in asciidict["frames"]:
        print(f)
        sleepSeconds(1 / fps)
def GenerateASCIIVideo(video, FPS = None, Processes = 1, Dest = ""):
    print(Dest)
    coloramaInit(autoreset = False)
    async def mainfunc():
        if FPS == None:
            fps = round(cv2VideoCapture(video).get(5))
        elif FPS == "":
            fps = round(cv2VideoCapture(video).get(5))
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
        vidlen = int(cv2VideoCapture(video).get(7) / cv2VideoCapture(video).get(5))
        vidfps = int(cv2VideoCapture(video).get(5))
        vidcap = vidcap = cv2VideoCapture(video)
        if fps > vidfps:
            raise ValueError("Given Fps (" + str(fps) + ") higher than Original Video Fps (" + str(vidfps) + ")") 
        def GetFrameImage(frame):
            vidcap.set(1, frame)
            _, img = vidcap.read()
            img = cv2Color(img, 6) 
            return img 
        @cache
        def processPixel(b):
            for ii in range(15):
                if b <= (ii + 1) * 17 and b >= ii * 17:
                    return chars[ii]
        async def processFrame(index = 0):
            frame = GetFrameImage(index)

            frm = cv2Resize(frame, (frameX, frameY))
            outstrn = ""
            for y in range(frm.shape[0]):
                for x in range(frm.shape[1]):
                    outstrn += processPixel(int(frm[y, x]))
                outstrn += "\n"
            arr[index] = outstrn
            dic["frames"] = arr
        ran = range(0, vidlen * fps, Workers)
        global arr, dic 
        arr = [None] * vidlen * fps * Workers
        dic = {}
        jsonfile = open(video + "_ascii.json", "w")
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] The video will be generated in the size of this Window. \n    Please resize the window so that the video is as big as you want. \n    After that, press space to continue with the generation process.")
        print(f'[!] Note: if the code says something like "mmco: unref short failure", \n    that just means that the video is corrupted at the current frame. \n    But this doesnt really affect anything. {Back.BLACK}{Fore.LIGHTWHITE_EX}')
        while True:
            if keyboard.read_key() == "space":
                    break
        terCols = os.get_terminal_size().columns
        terLins = os.get_terminal_size().lines
        testfrme = GetFrameImage(0)
        testfrme = cv2Resize(testfrme, (testfrme.shape[1] * 5, testfrme.shape [0] * 2))
        while (testfrme.shape[1] > terCols) or (testfrme.shape[0] > terLins):
                testfrme = cv2Resize(testfrme, None, fx = 0.9, fy = 0.9)
        frameX = testfrme.shape[1]
        frameY = testfrme.shape[0]
        framesleft = cv2VideoCapture(video).get(7)
        for i in ran:
            processes = []
            if framesleft < Workers:
                for ii in range(framesleft):
                    p = asyncio.create_task(processFrame(index = i + ii))
                    processes.append(p)
                for p in processes:
                    await p
                    framesleft -= 1
            else:
                for ii in range(Workers):
                    p = asyncio.create_task(processFrame(index = i + ii))
                    processes.append(p)
                for p in processes:
                    await p
                    framesleft -= 1

            print(str(i) + "/" + str(len(ran) * Workers))
        dic["fps"] = fps
        dic["sizeX"] = testfrme.shape[1]
        dic["sizeY"] = testfrme.shape[0]
        print(dic["sizeX"], dic["sizeY"])
        jsonfile.write(jsonDumps(dic).replace('"', '\"'))
        jsonfile.close()
        print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Ready to Play! Space key to play. ")
        while True:
            if keyboard.read_key() == "space":
                break
        try:
            shutil.move(video + "_ascii.json", Dest)
        except:
            pass
        os.system(f"cd {Dest}")
        ReadVideoFromJSON(Dest + "\\" + os.path.basename(video) + "_ascii.json")
    
    asyncio.run(mainfunc())
