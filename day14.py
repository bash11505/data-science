import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {

    "patient_name": [
        "Ravi",
        "Anjali",
        "Kiran",
        "Sneha",
        "Arjun",
        "Meena",
        "Rahul"
    ],

    "department": [
        "Cardiology",
        "Neurology",
        "Orthopedic",
        "Cardiology",
        "Neurology",
        "Orthopedic",
        "Cardiology"
    ],

    "days_admitted": [
        5,
        3,
        7,
        10,
        2,
        8,
        6
    ],

    "daily_charge": [
        5000,
        7000,
        4000,
        5000,
        7000,
        4000,
        5000
    ],

    "health_score": [
        45,
        80,
        60,
        30,
        90,
        55,
        40
    ]
}

df = pd.DataFrame(data)


df["total_bill"] = (
    df["days_admitted"] * df["daily_charge"]
)


department_bill = (
    df.groupby("department")["total_bill"].sum()
)

print("DEPARTMENT TOTAL BILL")
print(department_bill)


top_department = (
    department_bill.idxmax()
)

print("\nTOP DEPARTMENT")
print(top_department)


critical_patients = (
    df[df["health_score"] < 50]
)

print("\nCRITICAL PATIENTS")
print(
    critical_patients[
        ["patient_name", "health_score"]
    ]
)

print("\nAVERAGE BILL")
print(np.mean(df["total_bill"]))

print("\nMAXIMUM BILL")
print(np.max(df["total_bill"]))

print("\nMINIMUM BILL")
print(np.min(df["total_bill"]))


sns.barplot(
    x="department",
    y="total_bill",
    data=df
)

plt.show()