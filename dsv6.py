import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("Salary.csv")

# Input and output
X = df[["YearsExperience"]]
y = df["Salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict salary
prediction = model.predict(X)

# Plot graph
plt.scatter(X, y)
plt.plot(X, prediction, color="red")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Simple Linear Regression")
plt.show()

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
