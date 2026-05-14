import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
data={
    "student": ["A", "B", "C", "D", "E"],
    "marks": [75, 88, 92, 67, 81]
}
df=pd.DataFrame(data)
print("Average marks:")
print(np.mean(df["marks"]))

print("\nHighest Marks:")
print(np.max(df["marks"]))

sns.barplot(
    x="student",
    y="marks",
    data=df
)
plt.show()