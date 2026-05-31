import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Library dataset
data = {
    "book": [
        "Python",
        "Java",
        "Python",
        "C++",
        "Java",
        "Python",
        "C++"
    ],
    
    "copies_borrowed": [
        10,
        8,
        15,
        5,
        12,
        20,
        7
    ]
}

df = pd.DataFrame(data)

# Total borrowed copies by book
book_stats = df.groupby("book")["copies_borrowed"].sum()

print("Total Borrowed Copies")
print(book_stats)

# Most borrowed book
print("\nMost Borrowed Book")
print(book_stats.idxmax())

# Average borrowed copies
print("\nAverage Borrowed Copies")
print(np.mean(df["copies_borrowed"]))

# Graph
sns.barplot(
    x=book_stats.index,
    y=book_stats.values,
    palette=["red", "green", "blue"]
)

plt.title("Books Borrowed")
plt.show()