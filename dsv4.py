import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Display first records
print(df.head())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna("Unknown", inplace=True)

# Plot graph
df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()