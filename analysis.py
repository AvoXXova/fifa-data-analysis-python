import pandas as pd

# Load dataset
data = pd.read_csv("players_15.csv")

# Select required columns
age = data["age"]
overall = data["overall"]

# Basic statistics
mean_age = age.mean()
mean_overall = overall.mean()

# Correlation
correlation = age.corr(overall)

print(f"Mean Age: {mean_age:.2f}")
print(f"Mean Overall Rating: {mean_overall:.2f}")
print(f"Correlation between Age and Overall: {correlation:.4f}")
