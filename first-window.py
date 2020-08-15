# Create a simple graphic interface

import PySimpleGUI as sg
import os
CURRENT_DIR = os.getcwd()



image1_path = os.path.join(CURRENT_DIR, "images\learn.png")
image2_path = os.path.join(CURRENT_DIR, "images\qtest.png")
image3_path = os.path.join(CURRENT_DIR, "images\Read.gif")

THEME = "DarkGrey2"
RESULT_BUTTON_SIZE = (15 , 2)
FONT = 'Arial 10 bold'
sg.theme(THEME)
DISPLAY_TEXT = "hello"
BRAILLE_DISPLAY_TEXT = "hello"

result_layout = [[sg.Text('   Self Tutor', font="default 52 bold", size = (25,1), justification= 'c')],
                 [sg.Text('                      BE YOUR OWN TEACHER',font= "Comic 32 bold", justification= 'c')],
                 [sg.HorizontalSeparator(pad=(5, 5))],
                 [sg.HorizontalSeparator(pad=(5, 5))],
                 [sg.Text("   Let's Learn", font = "comic 24 bold", size = (13,0), justification='l'), sg.Text("Test Myself", font = "comic 24 bold", size = (20,0), justification='c')
                 ,sg.Text("Help me read", font = "comic 24 bold", size = (20,0), justification='c')],
                 [sg.Image(image1_path, size = (270,270)),sg.VSeperator(pad=(5,0)), sg.Image(image2_path, size = (300,400), pad = ((20,0))),sg.VSeperator(pad=(5,0)),
                  sg.Image(image3_path, size = (270,270), pad = (50, (10,0))) ],
                  [sg.SimpleButton('LEARN', pad = ((35,20), 0), key='', size=(10, 4)), sg.Button('LEARN',pad = ((35,30), 0), key='Audio_test', size=(10, 4)), sg.Button('LEARN',pad = ((50,30),0) ,key='Written_Test', size=(10, 4)), sg.Button('LEARN',pad = ((50,60),0), key='LEARN', size=(10, 4)),
                  sg.Button('HELP ME READ',pad = ((75,0),0),  key='READ', size=(20, 4))]]




#element_justification='center'



# Create the Window
window = sg.Window('SELF-TUTOR', result_layout, size=(1030, 677) )
# Event Loop to process "events"
while True:
    event, values = window.read()
    print(event,values)
    if event in (None, 'QUIT'):
        break


window.close()
