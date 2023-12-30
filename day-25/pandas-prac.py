# with open('weather_data.csv', mode='r') as data:
#     weather = data.readlines()
#
# print(weather)

# import csv
#
# with open('weather_data.csv', mode='r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     print(type(temperatures[1]))

import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data)
#
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(f"average of temperature is  {average_temp}")
#
# highest_temp = data["temp"].max()
# print(highest_temp)

# highest_temp_day = data[data.temp == data["temp"].max()]
# print(highest_temp_day)


def covert_to_fahrenheit(temp):
    fahrenheit = (temp * (9/5)) + 32
    return fahrenheit


monday_temp_in_F = covert_to_fahrenheit(data[data.day == "Monday"]["temp"])

print(monday_temp_in_F)