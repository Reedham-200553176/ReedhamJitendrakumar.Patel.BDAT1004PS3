# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

# Step 2. Create Series
series_1 = pd.Series(np.random.randint(1, 5, size=100))
series_2 = pd.Series(np.random.randint(1, 4, size=100))
series_3 = pd.Series(np.random.randint(10000, 30001, size=100))

# Step 3. Create DataFrame by joining the Series by column
data = {'bedrs': series_1, 'bathrs': series_2, 'price_sqr_meter': series_3}
df = pd.DataFrame(data)

# Step 4. Change column names
df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']

# Step 5. Create a one column DataFrame
bigcolumn = pd.DataFrame(pd.concat([series_1, series_2, series_3], axis=0))

# Step 6. Check if 'bigcolumn' goes only until index 99
print("Is it true that 'bigcolumn' goes only until index 99:", bigcolumn.index.max() == 99)

# Step 7. Reindex the DataFrame
bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn.index = range(300)

# Print the resulting DataFrame
print(bigcolumn)
