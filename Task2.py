# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
euro12 = pd.read_csv(url)

# Step 4. Select only the Goal column
goals = euro12['Goals']

# Step 5. How many teams participated in the Euro2012?
num_teams = euro12['Team'].nunique()

# Step 6. Number of columns in the dataset
num_columns = euro12.shape[1]

# Step 7. View only the columns Team, Yellow Cards, and Red Cards
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# Step 8. Sort the teams by Red Cards, then by Yellow Cards
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])

# Step 9. Calculate the mean Yellow Cards given per Team
mean_yellow_cards_per_team = euro12['Yellow Cards'].mean()

# Step 10. Filter teams that scored more than 6 goals
teams_more_than_6_goals = euro12[euro12['Goals'] > 6]

# Step 11. Select the teams that start with 'G'
teams_starting_with_G = euro12[euro12['Team'].str.startswith('G')]

# Step 12. Select the first 7 columns
first_seven_columns = euro12.iloc[:, :7]

# Step 13. Select all columns except the last 3
all_columns_except_last_three = euro12.iloc[:, :-3]

# Step 14. Present only the Shooting Accuracy from England, Italy, and Russia
shooting_accuracy = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]

# Print the results
print("Number of teams participated:", num_teams)
print("Number of columns:", num_columns)
print("Mean Yellow Cards per Team:", mean_yellow_cards_per_team)
print("Teams with more than 6 goals:\n", teams_more_than_6_goals)
print("Teams starting with 'G':\n", teams_starting_with_G)
print("First 7 columns:\n", first_seven_columns)
print("All columns except the last 3:\n", all_columns_except_last_three)
print("Shooting Accuracy for England, Italy, and Russia:\n", shooting_accuracy)
