from datetime import datetime
from set_timetable import df_sample

now = datetime.now()
current_time = now.strftime("%I")
# print(current_time)
current_day=now.strftime("%a")
# print(current_day)

for i in range(len(df_sample['Time'])):
    # temp=df_sample[current_day][i]

    temp=list(df_sample['Time'][i].split())
    if(current_time==('0'+temp[0])):
        current_class=df_sample[current_day][i]
        print(current_class)