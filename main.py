
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
    obj = Teams()
    ongoing_class = current(df_sample)
    gui = WingMan().homescreen()
    user_details = gui.returndetails()
    print(user_details)


main()
