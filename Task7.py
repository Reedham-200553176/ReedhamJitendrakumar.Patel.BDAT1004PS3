import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('us-marriages-divorces-1867-2014.csv')

# Filter data for years 1900, 1950, and 2000
years = [1900, 1950, 2000]
filtered_data = data[data['Year'].isin(years)]

# Plotting
plt.figure(figsize=(10, 6))

plt.bar(filtered_data['Year'] - 2, filtered_data['Marriages_per_1000'], width=0.4, label='Marriages per 1000')
plt.bar(filtered_data['Year'] + 2, filtered_data['Divorces_per_1000'], width=0.4, label='Divorces per 1000')

plt.xlabel('Year')
plt.ylabel('Per Capita')
plt.title('Comparison of Marriages and Divorces per Capita in the U.S. (1900, 1950, 2000)')
plt.xticks(years)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
