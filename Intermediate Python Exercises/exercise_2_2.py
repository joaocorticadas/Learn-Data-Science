from numpy._core.defchararray import index
import pandas as pd

country_capitals = {
  "Country": ["USA", "CA", "FR", "DE", "JP"],
  "Name": ["United States", "Canada", "France", "Germany", "Japan"],
  "Capital": ["Washington D.C.", "Ottawa", "Paris", "Berlin", "Tokyo"]
}

table = pd.DataFrame.from_dict(country_capitals)
table.set_index("Country", inplace = True)

#a)
print(table)
print("")

#b)
print(table[table["Capital"].str.startswith("B")])
print("")

#c)
print(table.loc[["JP", "FR"], ["Name", "Capital"]])
print("")

#d)
print(table.iloc[[1], [1]])
print("")