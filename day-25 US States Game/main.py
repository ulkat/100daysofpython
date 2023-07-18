# # #Using just file methods
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
# #
# #
# # #Using csv library
# import csv
#
import pandas

#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# #
# # # Using the pandas library
# import pandas

data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# Get Data in Columns
# print(data["condition"])
# print(data.condition)
# #
# # # Get Data in Row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# # # Create a dataframe from scratch
# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {"fur_color" : ["Gray", "Cinnamon", "Black"],
#              "count" : [gray, cinnamon, black]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")
#
