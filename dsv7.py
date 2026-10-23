import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Salary.csv")

# Correlation
print(df.corr(numeric_only=True))

# Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Regression plot
sns.regplot(x="YearsExperience", y="Salary", data=df)
plt.title("Regression Analysis")
plt.show()
