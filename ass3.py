import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Show missing values
print("Missing Values:")
print(df.isnull().sum())

# Replace missing numeric values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset saved successfully.")
