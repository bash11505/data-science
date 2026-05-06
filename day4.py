import pandas as pd
import matplotlib.pyplot as plt


data = {
    "timestamp": pd.date_range(start="2024-01-01", periods=20, freq="H"),
    "status": ["success", "error", "success", "success", "error"] * 4
}

df = pd.DataFrame(data)


error_count = df[df["status"] == "error"].shape[0]
print("Total Errors:", error_count)


df["hour"] = df["timestamp"].dt.hour
activity = df.groupby("hour").size()


activity.plot(kind='line', marker='o')

plt.title("System Activity by Hour")
plt.xlabel("Hour")
plt.ylabel("Requests")
plt.show()