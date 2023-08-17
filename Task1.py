# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, sep='|')

# Step 4. Mean age per occupation
mean_age_per_occupation = users.groupby('occupation')['age'].mean()

# Step 5. Male ratio per occupation
users['is_male'] = (users['gender'] == 'M')
male_ratio_per_occupation = users.groupby('occupation')['is_male'].mean().sort_values(ascending=False)

# Step 6. Minimum and maximum ages per occupation
min_max_age_per_occupation = users.groupby('occupation')['age'].agg(['min', 'max'])

# Step 7. Mean age per combination of occupation and sex
mean_age_per_combination = users.groupby(['occupation', 'gender'])['age'].mean()

# Step 8. Percentage of women and men per occupation
gender_percentage_per_occupation = users.groupby(['occupation', 'gender'])['is_male'].count() / users.groupby('occupation')['is_male'].count() * 100

print("Mean age per occupation:\n", mean_age_per_occupation)
print("\nMale ratio per occupation (most to least):\n", male_ratio_per_occupation)
print("\nMinimum and maximum ages per occupation:\n", min_max_age_per_occupation)
print("\nMean age per combination of occupation and sex:\n", mean_age_per_combination)
print("\nPercentage of women and men per occupation:\n", gender_percentage_per_occupation)
