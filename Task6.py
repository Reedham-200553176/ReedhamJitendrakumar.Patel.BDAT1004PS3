import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('us-marriages-divorces-1867-2014.csv')

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(data['Year'], data['Marriages_per_1000'], label='Marriages per 1000')
plt.plot(data['Year'], data['Divorces_per_1000'], label='Divorces per 1000')

plt.xlabel('Year')
plt.ylabel('Per Capita')
plt.title('Number of Marriages and Divorces per Capita in the U.S. (1867-2014)')
plt.legend()
plt.grid(True)
plt.show()
