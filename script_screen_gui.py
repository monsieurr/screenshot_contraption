import PySimpleGUI as sg
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
        rnd = random.randint(0, 1000)
        if(path == "default"):
            os.mkdir(path + str(rnd))
            os.chdir(path + str(rnd))
            print(path+str(rnd))
        elif not os.path.exists(path):
            os.mkdir(path)
            os.chdir(path)
            print(path)
        else:
            os.mkdir(path +str(rnd))
            os.chdir(path + str(rnd))
            print(path+str(rnd))

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

    print("this takes screenshots")

    return image


def looping_screens(topic="default", pause=5):
    # infinite loop of taking screenshots
    counter = 0

    # time delay (put arg here)
        
    time.sleep(int(pause))
    take_screenshots(topic)
    counter+=1
    print("Number of screens taken ", counter)

if __name__ == "__main__":
    # Defines the basic layout of hte window

    sg.theme("DarkPurple")

    layout = [
        [sg.Text(
            " 💎💎💎 Please enter a topic, a folder name and a time or let it run by default 💎💎💎 ")],
        [sg.Text("Default values are topic='default+curent time', folder name='default+random number', time='5s'")],
        [sg.Text("Topic", size=(15, 1), font='Lucida',
                 justification='right'), sg.Input()],
        [sg.Text("Folder name", size=(15, 1), font='Lucida',
                 justification='right'), sg.Input()],
        [sg.Text("Time", size=(15, 1), font='Lucida',
                 justification='right'), sg.Input('', enable_events=True, key="-INPUT-")],

        [sg.Button('Ok'), sg.Button('Exit')]
    ]

    # Gives a title to the window
    # Defines the window
    # Read the values inside
    # Close the window
    window = sg.Window('Screen Capturer 2000', layout, no_titlebar=True, grab_anywhere=True)
    
    while True:
        event, values = window.read()
        print(event, values)

        if event in (sg.WIN_CLOSED, 'Exit'):
            print("Exit")
            break
        if event == 'Ok':
            print('Submitted')
            break
        # if last character entered not a digit
        if len(values['-INPUT-']) and values['-INPUT-'][-1] not in ('0123456789'):
            # delete last char from input
            window['-INPUT-'].update(values['-INPUT-'][:-1])    


    window.close()

    layout = [[sg.Text('Stopwatch', size=(20, 2), justification='center')],
              [sg.Text(size=(10, 2), font=('Helvetica', 20),
                       justification='center', key='-OUTPUT-')],
              [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

    window = sg.Window('Stopwatch Timer', layout)


    create_folder(values[1])
    old_window_values = values


    timer_running, counter = True, 0

    while True:                                 # Event Loop
        # Please try and use as high of a timeout value as you can
        event, values = window.read(timeout=10)

        # if user closed the window using X or clicked Quit button
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        if timer_running:
            window['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format(
                (counter // 100) // 60, (counter // 100) % 60, counter % 100))
            counter += 1
            looping_screens(old_window_values[0], old_window_values['-INPUT-'])


    window.close()



    #sg.popup("click OK and the program will proceed and create" + "\nfolder : " +
    #        values[0] + "\ntopic : " + values[1] + "\ntime between shots : " + values['-INPUT-'])
    #create_folder(values[1])
    #looping_screens(values[0], values['-INPUT-'])

    #window.close()

    #   text_input = values
    #   sg.popup('You entered', text_input)
