import pyautogui as pag
from time import sleep
from pw import email, password


class Teams:

    def w(self):
        print("This thing is running!")

    def search_and_click(self, img):
        self.img = img
        loc = pag.locateOnScreen('./images/'+img+'.png')
        if(loc):
            center = pag.center(loc)
            pag.moveTo(x=center.x, y=center.y, duration=0.2)
            pag.click(button='left', clicks=1)
            sleep(1)
        else:
            print(loc, "not found!")

    def maximize(self):
        pag.keyDown('alt')
        pag.press(' ')
        pag.press('x')
        pag.keyUp('alt')
        pag.press('enter')

    def start_teams(self):
        pag.hotkey('win')
        sleep(2)
        pag.write('teams', interval=0.25)
        pag.press('enter')
        sleep(7)
        # self.maximize()

    def login(self, email, password):
        sleep(3)
        self.email = email
        self.password = password
        pag.write(email, interval=0.25)
        pag.press('enter')
        sleep(4)
        pag.write(password, interval=0.25)
        pag.press('enter')
        sleep(2)
        self.search_and_click('allow_permissions')
        self.search_and_click('signin')
        sleep(2)

    def teams_menu(self):
        self.search_and_click('teams')

    def join_team(self, team_name):
        self.team_name = team_name
        self.search_and_click(team_name)
        sleep(2)

    def join_meeting(self):
        sleep(2)
        self.search_and_click('join')
        self.search_and_click('join2')
        sleep(1)
        self.search_and_click('video1')
        self.search_and_click('audio')
        sleep(1)
        self.search_and_click('join_now')
        self.search_and_click('ifmute')
        # self.maximize()

    def stay_online(self):
        # self.start_time=start_time
        # self.end_time=end_time
        # duration=60-start_time
        # duration*=60
        duration = 30
        while duration >= 0:
            sleep(10)
            print("in the meeting vibing")
            pag.moveTo(500, 150, 2)
            duration = duration - 10

    def leave_meeting(self):
        self.search_and_click('leave')

    def cross(self):
        pag.press()

# obj = Teams()
# print("Starting teams!")
# obj.start_teams()
# print("Entereing email/password")
# obj.login('19124052@nuv.ac.in', 'rajiv@1964')
# sleep(10)
# print("selecting menu")
# obj.teams_menu()
# print("Joining team")
# obj.join_team('t')
# print("Joining meeting")
# obj.join_meeting()
# print("Stay online")
# obj.stay_online()
# print("leaving meeting")

# obj.leave_meeting()
# print("team menu")
# obj.teams_menu()
