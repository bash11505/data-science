import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {

    "employee_name": [
        "Rahul",
        "Sneha",
        "Kiran",
        "Anjali",
        "Arjun",
        "Meena",
        "Vijay"
    ],

    "department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "HR",
        "Finance",
        "IT"
    ],

    "salary": [
        50000,
        45000,
        60000,
        55000,
        40000,
        65000,
        70000
    ],

    "performance_score": [
        85,
        70,
        92,
        88,
        60,
        95,
        98
    ]
}

df = pd.DataFrame(data)


df["bonus"] = (
    df["salary"] * 0.10
)


department_salary = (
    df.groupby("department")["salary"].sum()
)

print("DEPARTMENT SALARY")
print(department_salary)


top_department = (
    department_salary.idxmax()
)

print("\nTOP DEPARTMENT")
print(top_department)


low_performers = (
    df[df["performance_score"] < 75]
)

print("\nLOW PERFORMERS")
print(
    low_performers[
        ["employee_name", "performance_score"]
    ]
)


print("\nAVERAGE SALARY")
print(np.mean(df["salary"]))

print("\nMAXIMUM PERFORMANCE")
print(np.max(df["performance_score"]))

print("\nMINIMUM PERFORMANCE")
print(np.min(df["performance_score"]))


sns.barplot(
    x="employee_name",
    y="performance_score",
    data=df
)

plt.show()