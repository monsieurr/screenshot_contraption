import os
import pyautogui
import PIL
from datetime import datetime
import time
import random
import argparse
import keyboard
import sys

def create_folder(path="default"):
    try:
        if(path == "default"):
            rnd = random.randint(0,1000)
            os.mkdir(path + str(rnd))
            os.chdir(path + str(rnd))
            print(path+str(rnd))
        else:
            os.mkdir(path)
            os.chdir(path)
            print(path)
            
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)
    print("this creates a folder")


def take_screenshots(topic="default"):
    ## capture the window
    ## record into a .jpg file
    ## put the jpg file into the current directory (created previously)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.replace("/", "_")
    dt_string = dt_string.replace(":", "_")
    dt_string = dt_string.replace(" ", "-")

    name_screen = topic + "-" + dt_string + ".jpg"
    print(name_screen)
    image = pyautogui.screenshot(name_screen)

    print ("this takes screenshots")

    return image

def looping_screens():
    # infinite loop of taking screenshots
    while True:
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                sys.exit()
        except:
            break  # if user pressed a key other than the given key the loop will break

        ## That's some not so good code down there
        # time delay (put arg here)
        if(args.time):
            time.sleep(args.time)
        else:
            time.sleep(5)

        if(args.topic):
            take_screenshots(args.topic)
        else:
            take_screenshots()

if __name__ == "__main__":
    ## STEPS
    ## Arguments to define
    ## -n <name of the screen_collection       ////[optional, "default + time"] by default"] 
    ## -p <path to save the folder>            ////[optional, "default+number" by default]
    ## -t <time between each screen>           ////[optional, 5 by default]
    parser = argparse.ArgumentParser(description='List the content of a folder')    
    parser.add_argument("-p", "--path", help="specify the folder's  path")
    parser.add_argument("-t", "--time", help="specify the time between each screenshot", type=int)
    parser.add_argument("-top",
        "--topic", help="specify the name of the screen collection")
    args = parser.parse_args()

    if(args.path):
        create_folder(args.path)
    else:
        create_folder()

    looping_screens()

