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
price_square_sort = real_estate.sort_values(["price", "square_feet"], ascending=[False, False])
print(price_square_sort)

#Exercise 3.1
show_loc_type_price = real_estate[["location", "type", "price"]]
print(show_loc_type_price)

#Exercise 3.2
square_ft = real_estate["square_feet"] > 1500
filter_square_ft = real_estate[square_ft]
print(filter_square_ft)

#Exercise 3.3
prop_house = real_estate["type"] == "House"
filter_prop_house = real_estate.loc[prop_house]
print(filter_prop_house)

#Exercise 4.1
real_estate["price_per_sqft"] = real_estate["price"] / real_estate["square_feet"]

#Exercise 4.2
real_estate["price_in_million"] = real_estate["price"] / 1000000
print(real_estate)

#Exercise 5.1
price_sqft_800 = real_estate[real_estate["price_per_sqft"] > 800]

#Exercise 5.2
sort_price_mill = price_sqft_800.sort_values("price_in_million", ascending = False)

#Exercise 5.3
filt_col = sort_price_mill[["location", "price_in_million", "price_per_sqft"]]
print(filt_col)