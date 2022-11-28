import pandas
# import csv

# with open("./Day25/weather_data.csv", mode="r") as data_file:
#     # listData = data_file.readlines()
#     # print(listData)

#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         if row[1] == "temp":
#             continue

#         rowTemperature = row[1]
#         temperatures.append(int(rowTemperature))

#     print(temperatures)

data = pandas.read_csv("./Day25/weather_data.csv")

dataDict = data.to_dict()
print(dataDict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)