import os
import pandas as pd
import numpy as np

path = os.getcwd()
file = path + '/Manila_Outer_10h.csv'
output_df = pd.read_csv(file)
print(output_df)

file = path + '/Manila_Outer_Relation.csv'
relation_df = pd.read_csv(file)
print(relation_df)

count = output_df['count'].tolist()
length = output_df['length'].tolist()
speed = output_df['speed'].tolist()
emission_rate = output_df['emission_rate'].tolist()


VMT = [0] * len(count)
for i in range(0, len(count)):
    VMT[i] = count[i] / length[i] * 1000 * speed[i] * length[i] / 1000

flow_relation = relation_df['Flow'].tolist()
speed_relation = relation_df['Speed'].tolist()
car_emission = []
puj_emission = []
bus_emission = []
truck_emission = []
mc_emission = []
total_emission = []
factor = 1.15
factor2 = 0.9
for hour in range(0, 24):
    speed_hour = [0] * len(speed)
    VMT_hour = [0] * len(speed)
    emission_rate_hour = [0] * len(speed)
    if 5 < hour < 22:
        for i in range(0, len(speed)):
            speed_hour[i] = speed[i] * speed_relation[hour] / speed_relation[10]
            VMT_hour[i] = VMT[i] * flow_relation[hour] / flow_relation[10] * factor2
    else:
        for i in range(0, len(speed)):
            speed_hour[i] = speed[i] * speed_relation[hour] / speed_relation[10] / factor
            VMT_hour[i] = VMT[i] * flow_relation[hour] / flow_relation[10]
    for i in range(0, len(speed)):
        speed_hour[i] = speed_hour[i] * factor
        if speed_hour[i] / 1.6 < 2.5:
            emission_rate_hour[i] = 1100
        elif speed_hour[i] / 1.6 < 7.5:
            emission_rate_hour[i] = 1100
        elif speed_hour[i] / 1.6 < 12.5:
            emission_rate_hour[i] = 1100 + (speed_hour[i] / 1.6 - 7.5) * (700 - 1100) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 17.5:
            emission_rate_hour[i] = 700 + (speed_hour[i] / 1.6 - 12.5) * (625 - 700) / (17.5 - 12.5)
        elif speed_hour[i] / 1.6 < 22.5:
            emission_rate_hour[i] = 625 + (speed_hour[i] / 1.6 - 17.5) * (500 - 625) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 27.5:
            emission_rate_hour[i] = 500 + (speed_hour[i] / 1.6 - 22.5) * (450 - 500) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 32.5:
            emission_rate_hour[i] = 450 + (speed_hour[i] / 1.6 - 27.5) * (400 - 450) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 37.5:
            emission_rate_hour[i] = 400 + (speed_hour[i] / 1.6 - 32.5) * (390 - 400) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 42.5:
            emission_rate_hour[i] = 390 + (speed_hour[i] / 1.6 - 37.5) * (375 - 390) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 47.5:
            emission_rate_hour[i] = 375 + (speed_hour[i] / 1.6 - 42.5) * (360 - 375) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 52.5:
            emission_rate_hour[i] = 360 + (speed_hour[i] / 1.6 - 47.5) * (355 - 360) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 57.5:
            emission_rate_hour[i] = 355 + (speed_hour[i] / 1.6 - 52.5) * (350 - 355) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 62.5:
            emission_rate_hour[i] = 350 + (speed_hour[i] / 1.6 - 57.5) * (350 - 350) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 67.5:
            emission_rate_hour[i] = 350 + (speed_hour[i] / 1.6 - 62.5) * (360 - 350) / (12.5 - 7.5)
        elif speed_hour[i] / 1.6 < 72.5:
            emission_rate_hour[i] = 360 + (speed_hour[i] / 1.6 - 67.5) * (375 - 360) / (12.5 - 7.5)
        else:
            emission_rate_hour[i] = 400

    car_emission_hour = [0] * len(count)
    puj_emission_hour = [0] * len(count)
    bus_emission_hour = [0] * len(count)
    truck_emission_hour = [0] * len(count)
    mc_emission_hour = [0] * len(count)

    for i in range(0, len(count)):
        car_emission_hour[i] = VMT_hour[i] * emission_rate_hour[i] / 1.6 * 0.75
        puj_emission_hour[i] = VMT_hour[i] * emission_rate_hour[i] / 1.6 * 0.03 * 350 / 270
        bus_emission_hour[i] = VMT_hour[i] * emission_rate_hour[i] / 1.6 * 0.05 * 450 / 270
        truck_emission_hour[i] = VMT_hour[i] * emission_rate_hour[i] / 1.6 * 0.02 * 830 / 270
        mc_emission_hour[i] = VMT_hour[i] * emission_rate_hour[i] / 1.6 * 0.15 * 75 / 270

    car_emission.append(sum(car_emission_hour))
    puj_emission.append(sum(puj_emission_hour))
    bus_emission.append(sum(bus_emission_hour))
    truck_emission.append(sum(truck_emission_hour))
    mc_emission.append(sum(mc_emission_hour))
    total_emission.append(car_emission[-1] + puj_emission[-1] + bus_emission[-1] + truck_emission[-1] + mc_emission[-1])

final_df = pd.DataFrame(np.transpose([car_emission, puj_emission, bus_emission, truck_emission, mc_emission, total_emission]))
final_df.to_csv('output.csv', header=['car_emission', 'puj_emission', 'bus_emission', 'truck_emission', 'mc_emission','total_emission'])

