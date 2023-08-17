import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('actor_kill_counts.csv')

# Sort the data by kill count
sorted_data = data.sort_values(by='Count', ascending=True)

# Plotting
plt.figure(figsize=(10, 8))

plt.barh(sorted_data['Actor'], sorted_data['Count'], color='skyblue')
plt.xlabel('Kill Count')
plt.ylabel('Actor')
plt.title('Deadliest Actors in Hollywood')
plt.xticks(rotation=45)
plt.tight_layout()

# Label each bar with the actor's name
for index, value in enumerate(sorted_data['Count']):
    plt.text(value + 5, index, str(value), va='center', color='black')

plt.show()
