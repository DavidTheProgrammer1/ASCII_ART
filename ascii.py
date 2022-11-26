"""
Python ASCII Art Generation Tool
"""
import os
import keyboard
from cv2 import waitKey
from tkinter import filedialog as fd
from colorama import init as coloramaInit
from colorama import Fore, Back, Style
from Ascii_Art_Gen_Lib.create_image import GenerateASCII as Gen_Ascii_Art
from Ascii_Art_Gen_Lib.create_video import GenerateASCIIVideo as Gen_Ascii_Art_Video
from Ascii_Art_Gen_Lib.create_video import ReadVideoFromJSON as PlayVideo


def openImgFile():
    """IMage open function"""
    f = fd.askopenfilename(title = "Select a Image", 
                            filetypes = [
                                ("Supported Images", "*.jpg *.jpeg *.jpg *.bmp *.dib *.jp2 *.png *.webp *.pbm *.pgm *.ppm *.pxm *.pnm *.pfm *.sr *.ras *.tiff *.tif *.exr *.hdr *.pic")
                            ])
    return os.path.abspath(f)
def openVidFile():
    """Video open function"""
    f = fd.askopenfilename(title = "Select a Video",
                            filetypes = [
                                ("Video", "*.*")
                            ])
    return os.path.abspath(f)
def openJsonFile():
    f = fd.askopenfilename(title = "Select the Json File Containing the Video",
                            filetypes = [
                                ("JSON File", "*.json")
                            ])
    return os.path.abspath(f)
def show_error_message(err):
    print(f"""{Back.BLACK}{Fore.LIGHTRED_EX}
[!] Generating ASCII Art Returned an Error:
    {err}
[!] Usually Code retrieved invalid user input.
    Try using only numbers when entering a input, without any letters.
    Otherwise it might be caused by a bug in the code.""")
    print()
def show_banner():
    """Show ASCII_ART banner"""
    os.system("cls")
    banner = r"""
         ___                                                 ___
        /   \         ____    ____   _   _                  /   \      ___     _______
       / / \ \       /  __|  / ___| | | | |                / / \ \    |    \  |__   __|
      / /___\ \      \  \   / /     | | | |               / /___\ \   |   _/     | |
     / _______ \   __/  /   \ \___  | | | |              / ______\ \  | |\ \     | |
    /_/       \_\ |____/     \____| |_| |_|   ________  /_/       \_\ |_| \_\    |_|
                                             |________|   """ + f"""{Back.BLACK}{Fore.LIGHTBLACK_EX}(This is not the actual Art)  """
    credentials = """
                   A simple ASCII Art creation Code made by David L.""" 
    helpd = """
                                type "help" for help"""
    print(f"{Fore.RED}{Back.BLACK}{banner}")
    print(f"{Fore.RED}{Back.BLACK}{Style.BRIGHT}{credentials}", flush = True, end = "")
    print(f"{Fore.LIGHTRED_EX}{Back.BLACK}{Style.DIM}{helpd}")

def main():
    """Main Loop"""
    os.system("title Ascii_Art")
    coloramaInit(autoreset = True)
    show_banner()

    while True:
        inp = input(f"{Back.BLACK}{Fore.LIGHTBLACK_EX}Ascii_Art $> ").strip()
        if inp == "image":
            try:
                Gen_Ascii_Art(openImgFile())
            except Exception as e:
                show_error_message(e)
        elif inp == "video":
            try:
                Gen_Ascii_Art_Video(openVidFile(), input("[?] FPS? (leave empty for max) "), input("[?] Processes to work? Default is 1, \n    for mid-tier devices is 2 recommended, \n    but if you have a high-tier PC, you can set higher numbers. "), Dest = os.getcwd())
            except Exception as e:
                show_error_message(e)
        elif inp == "play":
            try:
                v = openJsonFile()
                print(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}[!] Ready to Play! Space key to play. ")
                while True:
                    if keyboard.read_key() == "space":
                        break
                PlayVideo(v)
            except Exception as e:
                show_error_message(e)
        elif inp == "":
            pass
        elif inp == "help":
            print(f"""{Back.BLACK}{Fore.WHITE}
[!] This is the ASCII Art Command Help.
    The currently supported commands are:
      help    -   Show this help
      image   -   Generate ASCII Art Image
      video   -   Generate ASCII Art Video
      play    -   Play ASCII Art Video from File
                  """)
        else:
            print(f"""{Fore.LIGHTRED_EX}{Back.BLACK}
[!] Command not Recognized.
    Type "help" for Information about available Commands.
                  """)
if __name__ == "__main__":
    main()
