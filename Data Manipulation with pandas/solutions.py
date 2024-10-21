
# Solution 1: Load and Inspect the Data
import pandas as pd

# Load the CSV file
real_estate = pd.read_csv('real_estate.csv')

# Print first five rows
print(real_estate.head())

# Print info
print(real_estate.info())

# Print shape
print(real_estate.shape)


# Solution 2: Sorting the Data

# Sort by price in ascending order
sorted_by_price = real_estate.sort_values('price')
print(sorted_by_price)

# Sort by price in descending order
sorted_by_price_desc = real_estate.sort_values('price', ascending=False)
print(sorted_by_price_desc)

# Sort by price and square feet in descending order
sorted_by_price_sqft = real_estate.sort_values(['price', 'square_feet'], ascending=[False, False])
print(sorted_by_price_sqft)


# Solution 3: Subsetting the Data

# Subset to show location, type, and price
print(real_estate[['location', 'type', 'price']])

# Subset rows where square feet > 1500
large_properties = real_estate[real_estate['square_feet'] > 1500]
print(large_properties)

# Subset rows where type is House
houses = real_estate[real_estate['type'] == 'House']
print(houses)


# Solution 4: Adding New Columns

# Add a new column for price per square foot
real_estate['price_per_sqft'] = real_estate['price'] / real_estate['square_feet']
print(real_estate)

# Add a new column for price in millions
real_estate['price_in_million'] = real_estate['price'] / 1e6
print(real_estate)


# Solution 5: Filtering and Sorting Based on Conditions

# Filter properties where price_per_sqft > 800
expensive_per_sqft = real_estate[real_estate['price_per_sqft'] > 800]

# Sort by price_in_million in descending order
expensive_sorted = expensive_per_sqft.sort_values('price_in_million', ascending=False)

# Print location, price_in_million, and price_per_sqft
print(expensive_sorted[['location', 'price_in_million', 'price_per_sqft']])
