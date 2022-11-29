import pandas
import csv

with open("./Day25/weather_data.csv", mode="r") as data_file:
    # listData = data_file.readlines()
    # print(listData)

    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] == "temp":
            continue

        rowTemperature = row[1]
        temperatures.append(int(rowTemperature))

    print(temperatures)

data = pandas.read_csv("./Day25/weather_data.csv")

print(type(data))
print(type(data["temp"]))

dataDict = data.to_dict()
print(dataDict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

maxTemp = data["temp"].max()
print(maxTemp)

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./Day25/new_data.csv")