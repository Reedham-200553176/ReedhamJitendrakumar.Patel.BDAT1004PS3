# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the provided address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')

# Step 4. See the first 10 entries
print(chipo.head(10))

# Step 5. Number of observations in the dataset
num_observations = chipo.shape[0]

# Step 6. Number of columns in the dataset
num_columns = chipo.shape[1]

# Step 7. Print the name of all columns
print(chipo.columns)

# Step 8. How the dataset is indexed
print(chipo.index)

# Step 9. Most-ordered item
most_ordered_item = chipo['item_name'].value_counts().idxmax()

# Step 10. Number of the most-ordered item
most_ordered_item_count = chipo['item_name'].value_counts().max()

# Step 11. Most ordered item in the choice_description column
most_ordered_choice = chipo['choice_description'].value_counts().idxmax()

# Step 12. Total number of items ordered
total_ordered_items = chipo['quantity'].sum()

# Step 13. Convert item price to a float
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# Step 14. Revenue for the period
revenue = (chipo['item_price'] * chipo['quantity']).sum()

# Step 15. Number of orders made
num_orders = chipo['order_id'].nunique()

# Step 16. Average revenue amount per order
average_revenue_per_order = revenue / num_orders

# Step 17. Number of different items sold
num_different_items = chipo['item_name'].nunique()

# Print the results
print("Number of observations:", num_observations)
print("Number of columns:", num_columns)
print("Most-ordered item:", most_ordered_item)
print("Number of the most-ordered item:", most_ordered_item_count)
print("Most ordered choice in choice_description:", most_ordered_choice)
print("Total ordered items:", total_ordered_items)
print("Revenue for the period:", revenue)
print("Number of orders:", num_orders)
print("Average revenue per order:", average_revenue_per_order)
print("Number of different items sold:", num_different_items)
