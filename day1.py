import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

marks = np.array([89, 99, 98, 98, 97])

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": marks
}

df = pd.DataFrame(data)

print(df)

plt.figure()
plt.bar(df["Student"], df["Marks"])
plt.title("Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()