import pandas as pd

#Exercise 3.1
real_estate = pd.read_csv("real_estate.csv", index_col=0)

#Exercise 3.2
print(real_estate.head())

#Exercise 3.3
print(real_estate.info())

#Exercise 3.4
print(real_estate.shape)

#Exercise 2.1
price_sort_asc = real_estate.sort_values("price")
print(price_sort_asc)

#Exercise 2.2
price_sort_des = real_estate.sort_values("price", ascending=False)
print(price_sort_des)

#Exercise 2.3
price_square_sort = real_estate.sort_values(["price", "square_feet"], ascending=False)
print(price_square_sort)