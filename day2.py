import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Temperature data
temp = np.array([12, 23, 34, 45, 57, 59])


data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    "Location": ["Eluru", "Vijayawada", "Guntur", "Visakhapatnam", "Vizag", "Krishna"],
    "Temp": temp
}

df = pd.DataFrame(data)


print("Weather Data:\n", df)


print("Average Temp:", df["Temp"].mean())
print("Max Temp:", df["Temp"].max())

plt.figure()
plt.plot(df["Day"], df["Temp"], marker='o')
plt.title("Weather Report")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()