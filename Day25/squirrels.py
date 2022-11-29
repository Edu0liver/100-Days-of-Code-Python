import pandas

data = pandas.read_csv("./Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": [ "gray", "black", "red" ],
    "Count": [ gray_squirrels_count, black_squirrels_count, red_squirrels_count ]
}

data_csv = pandas.DataFrame(data_dict)
data_csv.to_csv("./Day25/new_data_squirrels.csv")
