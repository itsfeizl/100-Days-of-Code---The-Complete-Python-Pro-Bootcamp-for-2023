import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_sq = data[data["Primary Fur Color"] == "Gray"]
grey_sq_count = len(grey_sq)

cinnamon_sq = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_sq_count = len(cinnamon_sq)

black_sq = data[data["Primary Fur Color"] == "Black"]
black_sq_count = len(black_sq)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Squirrel Count": [grey_sq_count, cinnamon_sq_count, black_sq_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")
