from pandas import DataFrame
import time
# import pdftables_api

# convet timetable pdf to csv file
# c = pdftables_api.Client('06eakkhgf2p2', timeout=(60, 3600))
# c.csv('timetable.pdf', 'timetable.csv')

# read csv file into pandas dataframe
# data = pd.read_csv("timetable.csv")

# create dictonary for df
# tt={'Time':[],'Mon':[],'Tue':[],'Wed':[],'Thur':[],'Fri':[]}
# keys=list(tt.keys())
# for i in range(0,6):
#     temp='Unnamed: '+str(i)
#     if(i==3):
#         temp='Second Year CSE'
#     tt[keys[i]]=data[temp][1:9]

# df = pd.DataFrame(tt)

x = {'Time': ['12 to 01', '6 to 7', '7 to 8'], 'Sat': [
    'trial', 'NaN', 'Aztechs'], 'Sun': ['trial', 'NaN', 'Aztechs']}
df_sample = DataFrame(x)

# print(df_sample)
