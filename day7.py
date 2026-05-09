import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    "employee": ["John", "Sara", "Mike", "Anna", "Tom"],
    "days_present": [22, 18, 25, 20, 15],
    "total_working_days": [25, 25, 25, 25, 25]
}

df = pd.DataFrame(data)


df["attendance_percentage"] = (
    df["days_present"] / df["total_working_days"]
) * 100


good_attendance = df[df["attendance_percentage"] > 80]

print("Employees with Good Attendance:")
print(good_attendance)


average_attendance = np.mean(df["attendance_percentage"])

print("\nAverage Attendance:")
print(average_attendance)

plt.plot(df["employee"], df["attendance_percentage"])

plt.title("Employee Attendance Percentage")
plt.xlabel("Employee")
plt.ylabel("Attendance %")

plt.grid(axis='y')

plt.show()