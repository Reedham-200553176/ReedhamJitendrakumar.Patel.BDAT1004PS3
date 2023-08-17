import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('roman-emperor-reigns.csv')

# Calculate the number of emperors assassinated
assassinated_emperors = data[data['Cause_of_Death'] == 'Assassinated'].shape[0]

# Calculate the number of emperors not assassinated
total_emperors = data.shape[0]
not_assassinated_emperors = total_emperors - assassinated_emperors

# Plotting
labels = ['Assassinated', 'Not Assassinated']
sizes = [assassinated_emperors, not_assassinated_emperors]
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)  # explode 1st slice (Assassinated)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Fraction of Roman Emperors Assassinated')
plt.show()
