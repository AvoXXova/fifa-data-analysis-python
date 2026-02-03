import pandas as pd

# Load dataset
data = pd.read_csv("players_15.csv")

# Basic statistics
mean_age = data["age"].mean()
mean_overall = data["overall"].mean()

# Correlation
correlation = data["age"].corr(data["overall"])

print("Mean Age:", mean_age)
print("Mean Overall Rating:", mean_overall)
print("Correlation between Age and Overall:", correlation)
