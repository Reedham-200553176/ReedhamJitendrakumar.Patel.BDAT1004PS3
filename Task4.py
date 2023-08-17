# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the attached file wind.txt
data = pd.read_csv('wind.txt', delim_whitespace=True)

# Step 3. Create a proper datetime index
data['Date'] = pd.to_datetime(data['Dy'].astype(str) + '/' + data['Mo'].astype(str) + '/' + data['Yr'].astype(str), format='%d/%m/%y')
data.set_index('Date', inplace=True)
data.drop(['Dy', 'Mo', 'Yr'], axis=1, inplace=True)

# Step 4. Fix the year function
def fix_year(year):
    if year > 2000:
        return year - 100
    return year

data.index = data.index.to_series().apply(lambda x: x.replace(year=fix_year(x.year)))


# Step 5. Set the right dates as the index
data.index = pd.to_datetime(data.index)
data.index.name = 'Date'

# Step 6. Count missing values per location
missing_per_location = data.isnull().sum()

# Step 7. Count non-missing values in total
non_missing_total = data.notnull().sum().sum()

# Step 8. Calculate the mean windspeeds over all locations and times
mean_windspeed = data.mean().mean()

# Step 9. Calculate min, max, mean, and standard deviation per location
loc_stats = data.describe()

# Step 10. Calculate min, max, mean, and standard deviation per day
day_stats = data.resample('D').agg(['min', 'max', 'mean', 'std'])

# Step 11. Calculate average windspeed in January for each location
january_data = data.resample('M').mean()  # Resample to monthly frequency
january_data = january_data[january_data.index.month == 1]  # Filter January data
january_avg = january_data.groupby(january_data.index.year).mean()

# Step 12. Downsample to yearly frequency
yearly_data = data.resample('Y').mean()

# Step 13. Downsample to monthly frequency
monthly_data = data.resample('M').mean()

# Step 14. Downsample to weekly frequency
weekly_data = data.resample('W').mean()

# Step 15. Calculate min, max, mean, and standard deviation for each week (first 52 weeks)
weekly_stats = weekly_data.iloc[1:53].describe()

# Print the results
print("Missing values per location:\n", missing_per_location)
print("Total non-missing values:", non_missing_total)
print("Mean windspeeds over all locations and times:", mean_windspeed)
print("Location statistics:\n", loc_stats)
print("Day statistics:\n", day_stats)
print("Average windspeed in January:\n", january_avg)
print("Yearly downsampled data:\n", yearly_data)
print("Monthly downsampled data:\n", monthly_data)
print("Weekly downsampled data:\n", weekly_data)
print("Weekly statistics for the first 52 weeks:\n", weekly_stats)
