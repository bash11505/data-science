import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
data = {
    "student": ["A", "B", "C", "D"],
    "marks": [80, 90, 70, 85]
}

df = pd.DataFrame(data)

# Average marks
print("Average Marks:")
print(np.mean(df["marks"]))

# Highest marks
print("\nHighest Marks:")
print(np.max(df["marks"]))

# Graph
sns.barplot(
    x="student",
    y="marks",
    data=df,
    palette=["red", "green", "blue", "orange"]
)

plt.show()