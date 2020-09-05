import pyautogui as pag
from time import sleep
from pw import email,password

class Teams:

    def search_and_click(self,img):
        self.img=img
        loc=pag.locateOnScreen('./images/'+img+'.png')
        if(loc):
            center=pag.center(loc)
            pag.moveTo(x=center.x,y=center.y)
            pag.click(button='left',clicks=1)
            sleep(1)

    def maximize(self):
        pag.keyDown('alt')
        pag.press(' ')
        pag.press('x')
        pag.keyUp('alt')
        pag.press('enter')

    def start_teams(self):
        pag.hotkey('win')
        sleep(1)
        pag.write('teams',interval=0.25)
        pag.press('enter')
        sleep(8)
        # self.maximize()

    def login(self,email,password):
        self.email=email
        self.password=password
        pag.write(email,interval=0.25)
        pag.press('enter')
        sleep(3)
        pag.write(password,interval=0.25)
        pag.press('enter')
        sleep(3)
        self.search_and_click('allow_permissions')
        self.search_and_click('signin')
        sleep(2)

    def teams_menu(self):
        self.search_and_click('teams')

    def join_team(self,team_name):
        self.team_name=team_name
        self.search_and_click(team_name)
        sleep(2)

    def join_meeting(self):
        self.search_and_click('join')
        sleep(0.5)
        self.search_and_click('audio')
        self.search_and_click('video')
        self.search_and_click('join_now')
        # self.maximize()
    
    def stay_online(self):
        # self.start_time=start_time
        # self.end_time=end_time
        # duration=60-start_time
        # duration*=60
        duration=5
        while duration >= 0:
            sleep(3)
            # pag.moveTo(500, 150, 2)
            duration = duration - 3

    def leave_meeting(self):
        self.search_and_click('leave')

obj=Teams()
# obj.start_teams()
# obj.login(email,password)
# obj.teams_menu()
obj.join_team('trial')
obj.join_meeting()
obj.stay_online()
obj.leave_meeting()
obj.teams_menu()