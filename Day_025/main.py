# with open("weather_data.csv", "r") as data_file:
#     data = data_file.read().split("\n")
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())

# print(data["temp"].max())

# Det data in columns

# print(data["condition"])
# Alternatively you can use data.condition
# print(data.condition)

# Set data in row
# print(data[data.day == "Monday"])

# Print row of data when temperature is highest
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 9/5 + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

st_data = pandas.DataFrame(data_dict)
print(st_data)

# Create csv data
st_data.to_csv("new_st_data.csv")
