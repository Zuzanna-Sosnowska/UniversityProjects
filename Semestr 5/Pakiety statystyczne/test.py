import pandas as pd

data = pd.read_csv('book1-100k.csv')
empty_spaces = data.isna().sum()
print(empty_spaces)
# print(pd.isnull(data))
