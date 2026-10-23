import numpy as np
import pandas as pd

data = np.array([12, 25, 36, 48, 59, 62, 75, 84, 91, 100])

print("Array:", data)
print("Sum =", np.sum(data))
print("Mean =", np.mean(data))
print("Standard Deviation =", np.std(data))

df = pd.DataFrame(data, columns=["Numbers"])
print("\nFirst five Records:")
print(df.head())