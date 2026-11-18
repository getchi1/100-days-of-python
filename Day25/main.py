# import csv
#
# with open("weather_data.csv", "r") as csvfile:
#     data = csv.reader(csvfile, delimiter=",")
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#
#     print(temps)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temperature = data["temp"] # here calling by key
# condition = data.condition # here calling by attribute
#                            # both temp and condition syntax works same
# print(condition)
# # print(type(temperature))
# #
# temp_list = temperature.tolist()
# print(temp_list)
#
# # avg_temp = sum(temp_list) / len(temp_list)
# # avg_temp = data["temp"].mean()
# # print(avg_temp)
#
# # max_temp = max(temp_list)
# max_temp = data["temp"].max()
# print(max_temp)

# Get particular row
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday.temp)
# print(monday_temp_F)

# Get the particular row where temp is maximum
# print(data[data.temp == data["temp"].max()])

# Create Dataframe from scratch

# data_dict = {
#     "students" : ["Chitra", "Sachin", "Dan"],
#     "scores" : [89, 98, 78]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # Creating new csv file
# data.to_csv("data.csv")

#Using 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261117

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261117.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)

data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [2473, 392, 103]
}

color_counts_data = pandas.DataFrame(data_dict)
print(color_counts_data)

color_counts_data.to_csv("squirrel_counts.csv")