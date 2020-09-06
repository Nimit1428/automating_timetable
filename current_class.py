from datetime import datetime


def current(df_sample):
    now = datetime.now()
    current_time = now.strftime("%I")
    # print(current_time)
    current_day = now.strftime("%a")
    current_class=''

    for i in range(len(df_sample['Time'])):
        # temp=df_sample[current_day][i]
        temp = list(df_sample['Time'][i].split())
        if(int(current_time) < 10):
            if(current_time == ('0'+temp[0])):
                current_class = df_sample[current_day][i]
        else:
            if(current_time == (temp[0])):
                current_class = df_sample[current_day][i]

    return current_class
