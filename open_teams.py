import pyautogui as pag
import time

def open_teams():
    #196,748 start menu to open teams
    loc=pag.locateOnScreen('start.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left', clicks=1)
    pag.write('teams',interval=1)
    pag.press('enter')
    time.sleep(3)

    #enter email
    # loc=pag.locateOnScreen('email.png')
    # print(loc)
    # print(pag.center(loc))
    # center=pag.center(loc)
    # pag.moveTo(x=center.x,y=center.y)
    # pag.click(button='left',clicks=1)


    pag.write('email')
    pag.press('enter')

    #enter password
    time.sleep(4)
    pag.write('password')
    pag.press('enter')
    time.sleep(2)


    #check for popups
    # loc=pag.locateOnScreen('allow_pemissions.png')
    # if(loc):
    #     print(loc)
    #     print(pag.center(loc))
    #     center=pag.center(loc)
    #     pag.moveTo(x=center.x,y=center.y)
    #     pag.click(button='left',clicks=1)
    #     loc=pag.locateOnScreen('signin.png')
    #     print(loc)
    #     print(pag.center(loc))
    #     center=pag.center(loc)
    #     pag.moveTo(x=center.x,y=center.y)
    #     pag.click(button='left',clicks=1)
    #     time.sleep(1)

    #maximize screen
    pag.keyDown('alt')
    pag.press(' ')
    pag.press('x')
    pag.keyUp('alt')
    pag.press('enter')
    time.sleep(1)
    join_class()

def join_class():
    loc=pag.locateOnScreen('trial.png')
    print(loc)
    print(pag.center(loc))
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)
    time.sleep(1)
    join_meeting()

def join_meeting():
    loc=pag.locateOnScreen('join.png')
    if(loc):
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)

    pag.keyDown('alt')
    pag.press(' ')
    pag.press('x')
    pag.keyUp('alt')
    pag.press('enter')

    time.sleep(3)

    loc=pag.locateOnScreen('audio.png')
    if(loc):
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)

    loc=pag.locateOnScreen('video.png')
    if(loc):
        print(loc)
        print(pag.center(loc))
        center=pag.center(loc)
        pag.moveTo(x=center.x,y=center.y)
        pag.click(button='left',clicks=1)
    
    loc=pag.locateOnScreen('join_now.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)
    stay_online()


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

def leave_meeting():
    loc=pag.locateOnScreen('leave.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)
    time.sleep(1)
    teams_screen()

def teams_screen():
    loc=pag.locateOnScreen('teams.png')
    center=pag.center(loc)
    pag.moveTo(x=center.x,y=center.y)
    pag.click(button='left',clicks=1)

open_teams()
# join_class()
# join_meeting()
# teams_screen()


