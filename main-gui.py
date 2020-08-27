# This is the main module implementing the GUI for getting objects and text from image

import get_image_data as gimd
import PySimpleGUI as sg
import PIL
import io
import base64
import pyperclip
from time import sleep
import speech_recognition as sr
import  PySimpleGUI as sg
import random
import os
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
CURRENT_DIR = os.getcwd()
ASSETS_DIR = os.path.join(CURRENT_DIR, "assets")
slide1 = os.path.join(CURRENT_DIR, "images\A.jpg")
slide2 = os.path.join(CURRENT_DIR, "images\B.png")
slide3 = os.path.join(CURRENT_DIR, "images\C.jpg")
slide4 = os.path.join(CURRENT_DIR, "images\D.png")
shows = [slide1,slide2,slide3,slide4]
dict = { slide1: 'a', slide2: 'b', slide3: 'c', slide4: 'd'}

image1_path = os.path.join(CURRENT_DIR, "images\learn.png")
image2_path = os.path.join(CURRENT_DIR, "images\qtest.png")
image3_path = os.path.join(CURRENT_DIR, "images\Read.gif")

THEME = "DarkGrey2"
RESULT_BUTTON_SIZE = (15 , 2)
FONT = 'Arial 10 bold'
sg.theme(THEME)
DISPLAY_TEXT = "hello"
BRAILLE_DISPLAY_TEXT = "hello"

layout = [[sg.Text('   Self Tutor', font="default 52 bold", size = (25,1), justification= 'c')],
                 [sg.Text('                      BE YOUR OWN TEACHER',font= "Comic 32 bold", justification= 'c')],
                 [sg.HorizontalSeparator(pad=(5, 5))],
                 [sg.HorizontalSeparator(pad=(5, 5))],
                 [sg.Text("   Let's Learn", font = "comic 24 bold", size = (13,0), justification='l'), sg.Text("Test Myself", font = "comic 24 bold", size = (20,0), justification='c')
                 ,sg.Text("Help me read", font = "comic 24 bold", size = (20,0), justification='c')],
                 [sg.Image(image1_path, size = (270,270)),sg.VSeperator(pad=(5,0)), sg.Image(image2_path, size = (300,400), pad = ((20,0))),sg.VSeperator(pad=(5,0)),
                  sg.Image(image3_path, size = (270,270), pad = (50, (10,0))) ],
                  [sg.SimpleButton('LEARN', pad = ((35,20), 0), key='', size=(10, 4)), sg.Button('LEARN',pad = ((35,30), 0), key='', size=(10, 4)), sg.Button('LEARN',pad = ((50,30),0) ,key='Written_Test', size=(10, 4)), sg.Button('LEARN',pad = ((50,60),0), key='Audio_test', size=(10, 4)),
                  sg.Button('HELP ME READ',pad = ((75,0),0),  key='READ', size=(20, 4))]]

IMG_SIZE = (500, 500)
IMG_BUTTON_SIZE = (15, 2)
RESULT_BUTTON_SIZE = (15, 2)
DISPLAY_TEXT, BRAILLE_DISPLAY_TEXT = gimd.text_to_braille(
    "Please Select an Image and Press Detect.")
FONT = 'Arial 10 bold'


def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize(
            (int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

# Create the main master Window
window = sg.Window('SELF-TUTOR', layout, size=(1030, 677) )
img_path = ""

win2_active=False
win3_active = False
win5_active = False
while True:  # Event Loop for master window
    event, values = window.read()
    print(event, values)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    if event == 'Written_Test' and not win3_active:
        win3_active = True
        layout3 = [[sg.Image(background_color="grey", size=IMG_SIZE, key="image", pad=(10, 10))],
                        [sg.Button("START", size=IMG_BUTTON_SIZE,
                                  font="default 12 bold", key="START", enable_events=True),
                         sg.Button("CAPTURE", size=IMG_BUTTON_SIZE,
                                   font="default 12 bold", key="-CAPIMG-", enable_events=True),
                         sg.Button("CHECK", size=IMG_BUTTON_SIZE, key="CHECK", enable_events=True, font="default 12 bold")]]
        win3 = sg.Window('Written Test', layout3,
                           size=(530,610),
                           no_titlebar=False,
                           grab_anywhere=True,
                           keep_on_top=True,
                           background_color='white',
                           alpha_channel=1,
                           margins=(1, 1),
                           element_justification='center')
        count = 0
#-----------------------event loop for Written_Test slave window --------------------#
        while True:
            event_3, values = win3.read()
            random_alphabet= l[random.randint(0,25)]
            if event_3 == 'START':
                window.refresh()
                STRING = "WRITE DOWN THE ALPHABET"
                engine.say(STRING + " " + random_alphabet + "    ")
                engine.runAndWait()
            elif event_3 == '-CAPIMG-':
                try:
                    cap_img_path = gimd.capture_image()
                    if cap_img_path:
                        img_path = cap_img_path
                        img_data = convert_to_bytes(cap_img_path, IMG_SIZE)
                        win3['image'].update(data=img_data)
                        engine.say('Image captured, press Detect to continue.')
                        engine.runAndWait()
                    # else:
                    #     sg.popup_ok("No Image Captured!", keep_on_top=True)
                except:
                    pass
            elif event_3 == "CHECK":
                engine.say("let's check your answer")
                engine.runAndWait()
                window.refresh()
                #hard coded for now till an alternative to pytesseract is figured out
                if count == 0:
                    engine.say("CONGRATULATIONS! YOU GOT IT RIGHT")
                    engine.runAndWait()
                    count += 1
                else:
                    STRING ="SORRY. TRY AGAIN. THE ALPHABET DOES NOT LOOK LIKE"
                    engine.say(STRING + random_alphabet + "    ")
                    engine.runAndWait()


            if event_3 in (None, 'Exit', 'Cancel'):
                break



#-----------------------------------------Audio test slave window starts-------------------------------------------------------------------------------------------------------------------------#

    if event == 'Audio_test' and not win2_active:
        win2_active = True
        show = shows[0]
        #layout2 = [
        #[sg.Button('Forward',key='Forward')],
        #[sg.Button('Identify',key='Identify')],
        #[sg.Image(data=convert_to_bytes(slide1, IMG_SIZE), enable_events=True, background_color='white', key='IMAGE', right_click_menu=['UNUSED', 'Exit'])]
        #]
        layout2  = [[sg.Image(data=convert_to_bytes(slide1, IMG_SIZE), enable_events=True, background_color='white', key='IMAGE', right_click_menu=['UNUSED', 'Exit'])],
                        [
                         sg.Button("Identify", size=IMG_BUTTON_SIZE,
                                   font="default 12 bold", key="Identify", enable_events=True),
                         sg.Button("Next ", size=IMG_BUTTON_SIZE, key="Forward", enable_events=True, font="default 12 bold"),
                         sg.Button("Previous", size=IMG_BUTTON_SIZE, key="Back", enable_events=True, font="default 12 bold")]]


        #win2 = sg.Column(image_layout, element_justification='center', size=(530, 610))

        win2 = sg.Window('My new window', layout2,
                   size=(530,610),
                   no_titlebar=False,
                   grab_anywhere=True,
                   keep_on_top=True,
                   background_color='white',
                   alpha_channel=1,
                   margins=(1, 1),
                   element_justification='center')
        offset = 0
        show = shows[0]
        r = sr.Recognizer()
        m = sr.Microphone()
        while True:
            event, values = win2.read()
            if event in (None, 'Exit', 'Cancel'):
                break

            elif event == 'Forward': #if clicked on the image
                offset += (offset < len(shows) - 1)  # add 1 until the last one
                show = shows[offset]  # get a new image
            # update the image in the window

            elif event == 'Identify':
                with m as source:
                    r.adjust_for_ambient_noise(source)
                    audio= r.listen(source,5)
                    value = r.recognize_google(audio, language="en-US")
                    print(value)
                    print(dict[show])
                    if value == dict[show]:

                        print("correct")
                        engine.say('Correct answer. Move to the next alphabet')
                        engine.runAndWait()
                    else:
                        print("incorrect")
                        engine.say('Wrong answer. Try again')
                        engine.runAndWait()
    # update the image in the window
            img_data_path = convert_to_bytes(show, IMG_SIZE)
            win2['IMAGE'].update(data = img_data_path)
            win3_active = False





    if win2_active:
        ev2, vals2 = win2.Read(timeout=100)
        if ev2 is None or ev2 == 'Exit':
            win2.Close()
            win2_active = False

#---------------------------------------------Audio_test ends------------------------------------------------------------------------------------------------------------------------#

#----------------- READ SLAVE WINDOW---------------------------------------------------------------------------------------------------------------------------------------#

    if event == 'READ' and not win5_active:
        win5_active = True
        image_layout = [[sg.Image(background_color="grey", size=IMG_SIZE, key="-IMAGE-", pad=(10, 10))],
                        [sg.Input(key="-FILE-", enable_events=True, visible=False),
                         sg.FileBrowse("Select Image", size=IMG_BUTTON_SIZE, file_types=(
                             ("Image Files", "*.png;*.jpg;*.jpeg"),), target="-FILE-", font="default 12 bold"),
                         sg.Button("Capture Image", size=IMG_BUTTON_SIZE,
                                   font="default 12 bold", key="-CAPIMG-", enable_events=True),
                         sg.Button("Detect", size=IMG_BUTTON_SIZE, key="-DETECT-", enable_events=True, font="default 12 bold")],
                        [sg.Text("Please select an image to continue", size=(50, None), justification='c', border_width=4, key="-WAIT-")]]



        result_layout = [[sg.Text('Detection results', font="default 12 bold")],
                         [sg.Text('Click a button to see the corresponding result')],
                         [sg.Button("Detected\nText", size=RESULT_BUTTON_SIZE, key="-DTEXT-", enable_events=True),

                          sg.Button("Detected\nObjects", size=RESULT_BUTTON_SIZE, key="-DOBJS-", enable_events=True),],
                         [sg.HorizontalSeparator(pad=(10, 10))],
                         [sg.Text("Detection in English\n(Pre-Processed for conversion to Braille)"),
                          sg.Button("Copy", size=(6, None), key="-CPFTEXT-", enable_events=True)],
                         [sg.Multiline(DISPLAY_TEXT, key='-FTEXT-', size=(None, 10), disabled=True)],
                         [sg.Text("Converted to Grade 1 Braille\n(utf-8 encoding)"),
                          sg.Button("Copy", size=(6, None), key="-CPBTEXT-", enable_events=True)],
                         [sg.Multiline(BRAILLE_DISPLAY_TEXT,
                                       key='-BTEXT-', size=(None, 10), disabled=True)],
                         [sg.Button('LEARN',key='LEARN', size=(7, 1))],
                         [sg.Button('TEST',key='TEST', size=(7, 1))],[sg.Text("Braille Project", font="default 11", text_color="grey")]]

        layout = [
            [
                sg.Column(image_layout, element_justification='center', size=(530, 610)),
                sg.VSeperator(),
                sg.Column(result_layout, size=(350, 610))
            ]
        ]
        window = sg.Window('Image to Braille').Layout(layout)
        while True:
            event, values = window.read()
            if event in (None, 'Exit', 'Cancel'):
                break
            if event == "-FILE-":
                try:
                    if values["-FILE-"]:
                        img_path = values["-FILE-"]
                        img_data = convert_to_bytes(img_path, IMG_SIZE)
                        print("img_data captured")
                        print(img_data)
                        window['-IMAGE-'].update(data=img_data)
                        ftext, btext = DISPLAY_TEXT, BRAILLE_DISPLAY_TEXT
                        fobj_text, bobj_text = DISPLAY_TEXT, BRAILLE_DISPLAY_TEXT
                        window['-FILE-'].update('')
                        window['-FTEXT-'].update(ftext)
                        window['-BTEXT-'].update(btext)
                        window["-WAIT-"].update("Image selected, press Detect to continue.")
                        engine.say('Image selected, press Detect to continue.')
                        engine.runAndWait()
                except:
                    pass

            if event == "-CAPIMG-":
                try:
                    cap_img_path = gimd.capture_image()
                    if cap_img_path:
                        img_path = cap_img_path
                        img_data = convert_to_bytes(cap_img_path, IMG_SIZE)
                        window['-IMAGE-'].update(data=img_data)
                        ftext, btext = DISPLAY_TEXT, BRAILLE_DISPLAY_TEXT
                        fobj_text, bobj_text = DISPLAY_TEXT, BRAILLE_DISPLAY_TEXT
                        window['-FTEXT-'].update(ftext)
                        window['-BTEXT-'].update(btext)
                        window["-WAIT-"].update("Image captured, press Detect to continue.")
                        engine.say('Image captured, press Detect to continue.')
                        engine.runAndWait()
                    # else:
                    #     sg.popup_ok("No Image Captured!", keep_on_top=True)
                except:
                    pass

            if event == "-DETECT-":
                try:
                    engine.say("detect button is pressed")
                    engine.runAndWait()
                    print(f"Image Path: {img_path}")
                    window["-WAIT-"].update("Please wait while Detecting Text and Objects...")
                    engine.say('Please wait while Detecting Text and Objects...')
                    engine.runAndWait()
                    window.refresh()
                    # if img_path:
                    #     sg.popup_no_buttons("Please Wait...", no_titlebar=True, keep_on_top=True,
                    #                         auto_close=True, non_blocking=True, auto_close_duration=1)
                    text, ftext, btext = gimd.get_text_from_image(img_path)


                    dtext_path = gimd.get_text_bounding_box(img_path)
                    dimg_path, objs = gimd.get_objects_from_image(img_path)
                    fobj_text, bobj_text = gimd.text_to_braille(
                        '\n'.join(objs) or "No Objects Detected.")
                    img_data = convert_to_bytes(dimg_path, IMG_SIZE)
                    dtext_data = convert_to_bytes(dtext_path, IMG_SIZE)
                    window['-IMAGE-'].update(data=dtext_data)
                    window['-FTEXT-'].update(ftext)
                    window['-BTEXT-'].update(btext)
                    window["-WAIT-"].update("Detection Complete!")
                    engine.say('Detection Complete. Press detect text or detect objects to continue')
                    engine.runAndWait()
                    # sg.popup_ok("Detection Complete!", keep_on_top=True)
                except:
                    window["-WAIT-"].update("Detection unsuccessful!")
                    sg.popup_ok("Make sure you have installed tesseract-ocr.\nIf you do, make sure you have the following files\nin the currect directory as shown:\n./assets/yolov3.cfg\n./assets/yolov3.weights\n./assets/yolov3.txt - for classes", title="An Error occurred!", keep_on_top=True)
                    engine.say('Detection unsuccessful!')
                    engine.runAndWait()

            if event == "-DOBJS-":
                try:
                    window['-FTEXT-'].update(fobj_text)
                    window['-BTEXT-'].update(bobj_text)
                    window['-IMAGE-'].update(data=img_data)
                    engine.say("These objects are present in your surroundings")
                    engine.say(fobj_text)
                    engine.runAndWait()


                except:
                    pass

            if event == "-DTEXT-":
                try:
                    window['-FTEXT-'].update(ftext)
                    window['-BTEXT-'].update(btext)
                    window['-IMAGE-'].update(data=dtext_data)
                    engine.say(ftext)
                    engine.runAndWait()


                except:
                    pass

            if event == "-CPFTEXT-":
                pyperclip.copy(values["-FTEXT-"])
                window["-WAIT-"].update("English Text Copied!")

            if event == "-CPBTEXT-":
                pyperclip.copy(values["-BTEXT-"])
                window["-WAIT-"].update("Braille Text Copied!")

            if event == sg.WIN_CLOSED:
                break

  #if event == sg.WIN_CLOSED:
     # break





#--------------------------------------------------------READ SLAVE WINDOW ENDS--------------------------------------------------------------------------------------#






window.close()
