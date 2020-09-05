import pyautogui as pag
import time
from pw import email,password

def open_teams():

    #start menu
    loc=pag.locateOnScreen('./images/start.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left', clicks=1)
    pag.write('teams',interval=1)
    pag.press('enter')
    time.sleep(8)

    #enter email
    pag.write(email)
    pag.press('enter')

    #enter password
    time.sleep(8)
    pag.write(password)
    pag.press('enter')
    time.sleep(3)

    #check for popups
    loc=pag.locateOnScreen('./images/allow_permissions.png')
    if(loc):
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)
        loc=pag.locateOnScreen('./images/signin.png')
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)
        time.sleep(1)

    #maximize screen
    pag.keyDown('alt')
    pag.press(' ')
    pag.press('x')
    pag.keyUp('alt')
    pag.press('enter')
    time.sleep(10)
    join_class()

#joining class
#add images of all class. sirf logo rakhna text nai
def join_class():
    time.sleep(2)
    loc=pag.locateOnScreen('./images/trial.png')
    print(loc)
    print(pag.center(loc))
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)
    time.sleep(3)
    join_meeting()

#join perticular meeting in class
def join_meeting():
    loc=pag.locateOnScreen('./images/join.png')
    if(loc):
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)

    #maximize the screen
    pag.keyDown('alt')
    pag.press(' ')
    pag.press('x')
    pag.keyUp('alt')
    pag.press('enter')

    time.sleep(3)

    #mute audio
    loc=pag.locateOnScreen('./images/audio.png')
    if(loc):
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)

    #turn off video
    loc=pag.locateOnScreen('./images/video.png')
    if(loc):
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)
    
    #join meetin now
    loc=pag.locateOnScreen('./images/join_now.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)
    stay_online()

#sleep mode me na jai esliye
def stay_online():
    duration=10
    try:
        while duration >= 0:
            time.sleep(5)
            pag.moveTo(200, 200, 2)
            duration = duration - 5
        leave_meeting()
    except KeyboardInterrupt:
        print('stopping...')

#exit meeting 
def leave_meeting():
    loc=pag.locateOnScreen('./images/leave.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)
    time.sleep(1)
    teams_screen()


#go to main teams home screen
def teams_screen():
    loc=pag.locateOnScreen('./images/teams.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)

open_teams()
# join_class()
# join_meeting()
# teams_screen()

