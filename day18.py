import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {

    "movie": [
        "Leo",
        "Jailer",
        "RRR",
        "Pushpa"
    ],

    "rating": [
        8.5,
        9.0,
        9.5,
        8.8
    ]
}

df = pd.DataFrame(data)


print("Average Rating:")
print(np.mean(df["rating"]))


print("\nHighest Rating:")
print(np.max(df["rating"]))


print("\nLowest Rating:")
print(np.min(df["rating"]))


plt.pie()(
    x="movie",
    y="rating",
    data=df,
    palette=["red", "green", "blue", "orange"]
)

plt.show()