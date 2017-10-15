import pandas as pd
import json
from itertools import islice
import os
import numpy as np

###########################################################################
# find out the number of cars in each segment
path = '.../Manila/Manila_Outer'

# read in the car segment associated file
file = path + '/carsegmentcount.csv'
df = pd.read_csv(file)
#print(df)

segment_id1 = df['join_segment_id'].tolist()
len1 = len(segment_id1)

# read in the segment length file
file2 = path + '/segmentlength.csv'
df2 = pd.read_csv(file2)
#print(df2)
segment_id2 = df2['segment_id'].tolist() #the number of segments we need
segment_length = df2['length'].tolist()
#print(segment_id2)
len2 = len(segment_id2)
print(len(segment_id2))

count = [0] * len2
for each_id in segment_id1:
    count[segment_id2.index(each_id)] += 1

#print(segment_id2)
#print(segment_length)
#print(count)
#############################################################################

#############################################################################
# produce the number of cars in each hour
path = '.../Manila_Outer_AllWeekday'
file3 = path + '/Manila_Outer.csv'
df3 = pd.read_csv(file3)
#print(df3)
Time_Start = df3['Time Start'].tolist()
num_vehicles = df3['Number of Observations'].tolist()
veh_count_hour = [0] * 24
count_hour = [0] * 24
iter1 = 0
for time in Time_Start:
    if time == '00:00':
        veh_count_hour[0] += num_vehicles[iter1]
        count_hour[0] += 1
    if time == '01:00':
        veh_count_hour[1] += num_vehicles[iter1]
        count_hour[1] += 1
    if time == '02:00':
        veh_count_hour[2] += num_vehicles[iter1]
        count_hour[2] += 1
    if time == '03:00':
        veh_count_hour[3] += num_vehicles[iter1]
        count_hour[3] += 1
    if time == '04:00':
        veh_count_hour[4] += num_vehicles[iter1]
        count_hour[4] += 1
    if time == '05:00':
        veh_count_hour[5] += num_vehicles[iter1]
        count_hour[5] += 1
    if time == '06:00':
        veh_count_hour[6] += num_vehicles[iter1]
        count_hour[6] += 1
    if time == '07:00':
        veh_count_hour[7] += num_vehicles[iter1]
        count_hour[7] += 1
    if time == '08:00':
        veh_count_hour[8] += num_vehicles[iter1]
        count_hour[8] += 1
    if time == '9:00':
        veh_count_hour[9] += num_vehicles[iter1]
        count_hour[9] += 1
    if time == '10:00':
        veh_count_hour[10] += num_vehicles[iter1]
        count_hour[10] += 1
    if time == '11:00':
        veh_count_hour[11] += num_vehicles[iter1]
        count_hour[11] += 1
    if time == '12:00':
        veh_count_hour[12] += num_vehicles[iter1]
        count_hour[12] += 1
    if time == '13:00':
        veh_count_hour[13] += num_vehicles[iter1]
        count_hour[13] += 1
    if time == '14:00':
        veh_count_hour[14] += num_vehicles[iter1]
        count_hour[14] += 1
    if time == '15:00':
        veh_count_hour[15] += num_vehicles[iter1]
        count_hour[15] += 1
    if time == '16:00':
        veh_count_hour[16] += num_vehicles[iter1]
        count_hour[16] += 1
    if time == '17:00':
        veh_count_hour[17] += num_vehicles[iter1]
        count_hour[17] += 1
    if time == '18:00':
        veh_count_hour[18] += num_vehicles[iter1]
        count_hour[18] += 1
    if time == '19:00':
        veh_count_hour[19] += num_vehicles[iter1]
        count_hour[19] += 1
    if time == '20:00':
        veh_count_hour[20] += num_vehicles[iter1]
        count_hour[20] += 1
    if time == '21:00':
        veh_count_hour[21] += num_vehicles[iter1]
        count_hour[21] += 1
    if time == '22:00':
        veh_count_hour[22] += num_vehicles[iter1]
        count_hour[22] += 1
    if time == '0-1:00':
        veh_count_hour[23] += num_vehicles[iter1]
        count_hour[23] += 1
    iter1 += 1

final_count = [0] * 24
for i in range(0, 24):
    final_count[i] = veh_count_hour[i] / count_hour[i]
#print(count_hour)
#print(veh_count_hour)
# final_count is the vehicle count per hour
print(final_count)
#######################################################################

# match the segment with speed
path = '.../Manila/Manila_Outer'
file4 = path + '/speed.csv'
df4 = pd.read_csv(file4)
#print(df4)
segment_with_speed = df4['Edge Id'].tolist()
segment_speed = df4['Average Speed KPH'].tolist()
#print(len(segment_with_speed))

path = '.../Manila_Outer_AllWeekday'
file5 = path + '/Manila_Outer.csv'
df5 = pd.read_csv(file5)
total_segment_with_speed = df5['Edge Id'].tolist()
wednesday = df5['Wednesday'].tolist()
time = df5['Time Start'].tolist()
total_segment_speed = df5['Average Speed KPH'].tolist()
#print(len(segment_with_speed))
print(total_segment_with_speed)

values = np.array(total_segment_with_speed)
values1 = np.array(wednesday)
values2 = np.array(time)
speed = [0] * len2
iter2 = 0
for segment in segment_id2:
    if segment not in segment_with_speed:
        if segment in total_segment_with_speed:
            searchval = segment
            searchval1 = 1
            searchval2 = '10:00'
            ii = np.where(values == searchval)[0]
            ii2 = np.where(values1 == searchval1)[0]
            ii3 = np.where(values2 == searchval2)[0]
            ix = np.intersect1d(ii, ii2)
            ix2 = np.intersect1d(ix, ii3)
            if ix2.size == 0:
                speed[iter2] = 50
            else:
                speed[iter2] = total_segment_speed[ix2[0]]
        else:
            speed[iter2] = 50
    else:
        speed[iter2] = segment_speed[segment_with_speed.index(segment)]
    iter2 += 1
print(speed)
print(len(speed))

emission_rate = [0] * len2
iter3 = 0
factor = 1.15
speed1 = [0] * len2
for i in range(0, len(speed)):
    speed1[i] = speed[i] * factor
#print(speed)
for spd in speed1:
    if spd / 1.6 < 2.5:
        emission_rate[iter3] = 1100
    elif spd / 1.6 < 7.5:
        emission_rate[iter3] = 1100
    elif spd / 1.6 < 12.5:
        emission_rate[iter3] = 1100 + (spd / 1.6 - 7.5) * (700 - 1100) / (12.5 - 7.5)
    elif spd / 1.6 < 17.5:
        emission_rate[iter3] = 700 + (spd / 1.6 - 12.5) * (625 - 700) / (17.5 - 12.5)
    elif spd / 1.6 < 22.5:
        emission_rate[iter3] = 625 + (spd / 1.6 - 17.5) * (500 - 625) / (12.5 - 7.5)
    elif spd / 1.6 < 27.5:
        emission_rate[iter3] = 500 + (spd / 1.6 - 22.5) * (450 - 500) / (12.5 - 7.5)
    elif spd / 1.6 < 32.5:
        emission_rate[iter3] = 450 + (spd / 1.6 - 27.5) * (400 - 450) / (12.5 - 7.5)
    elif spd / 1.6 < 37.5:
        emission_rate[iter3] = 400 + (spd / 1.6 - 32.5) * (390 - 400) / (12.5 - 7.5)
    elif spd / 1.6 < 42.5:
        emission_rate[iter3] = 390 + (spd / 1.6 - 37.5) * (375 - 390) / (12.5 - 7.5)
    elif spd / 1.6 < 47.5:
        emission_rate[iter3] = 375 + (spd / 1.6 - 42.5) * (360 - 375) / (12.5 - 7.5)
    elif spd / 1.6 < 52.5:
        emission_rate[iter3] = 360 + (spd / 1.6 - 47.5) * (355 - 360) / (12.5 - 7.5)
    elif spd / 1.6 < 57.5:
        emission_rate[iter3] = 355 + (spd / 1.6 - 52.5) * (350 - 355) / (12.5 - 7.5)
    elif spd / 1.6 < 62.5:
        emission_rate[iter3] = 350 + (spd / 1.6 - 57.5) * (350 - 350) / (12.5 - 7.5)
    elif spd / 1.6 < 67.5:
        emission_rate[iter3] = 350 + (spd / 1.6 - 62.5) * (360 - 350) / (12.5 - 7.5)
    elif spd / 1.6 < 72.5:
        emission_rate[iter3] = 360 + (spd / 1.6 - 67.5) * (375 - 360) / (12.5 - 7.5)
    else:
        emission_rate[iter3] = 400
    iter3 += 1
print(emission_rate)

final_df = pd.DataFrame(np.transpose([segment_id2, count, segment_length, speed, emission_rate]))
final_df.to_csv('output.csv', header=['segment_id', 'count', 'length', 'speed', 'emission_rate'])
