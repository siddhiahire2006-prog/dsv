import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Display information
print(df.info())

# Statistical summary
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna("Unknown", inplace=True)

# Count plot
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows")
plt.show()

# Histogram
df["release_year"].hist()
plt.title("Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.show()
