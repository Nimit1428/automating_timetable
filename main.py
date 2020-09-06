
# Current date time in local system print(datetime.now())
import pyautogui as pag
import datetime
import calendar
from teams import Teams
from gui import WingMan
from current_class import current
from set_timetable import df_sample

# GUI Returns

# loggenIn = 1
# email = '19124034@outlook.com'
# password = 'Nimit2801'

# # Time Table Returns


# def weekDay(date):
#     day = datetime.datetime.strptime(date, "%d %m %Y").weekday()
#     return (calendar.day_name[day])


# def today_date():
#     t = datetime.date.today()
#     day = str(t.day)
#     type(t.month)
#     day += " " + str(t.month) + " " + str(t.year)
#     return day


# class update():
#     def started(self):
#         pag.alert("The Class has started")

#     def ended(self):
#         pag.alert("The Class has ended")

#     def school_started(self):
#         pag.alert("The School has started")


# update = update()
# start = 1
# while(start):

def main():
    teams = Teams()
    
    gui = WingMan()
    gui.homescreen()
    user_details=gui.returnDetails()
    loginStatus=user_details[0]
    email=user_details[1]
    password=user_details[2]

    teams.start_teams()

    if(loginStatus):
        teams.login(email, password)
    
    teams.teams_menu()
    pag.alert("The school has started!!")
    #hours while the loop will run
    h=len(df_sample['Time'])
    while(h):
        ongoing_class = current(df_sample)
        if (ongoing_class != 'NaN'):
            teams.join_team(ongoing_class)
            teams.join_meeting()
            teams.stay_online()
            teams.teams_menu()
        else:
            pag.alert("You have a free period! Join!")
        h-=1
    pag.alert("You are done with today's classes!")

main()
