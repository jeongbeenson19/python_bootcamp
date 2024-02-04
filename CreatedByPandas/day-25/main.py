import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data1 = data["Primary Fur Color"].value_counts()

data1 = pd.DataFrame(data1)

print(type(data1))
# data1.to_csv("color_distribution.csv")
