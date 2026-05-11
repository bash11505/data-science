import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data ={
    "transaction_id": range(1001, 1016),

    "customer": [
        "Ravi", "Anjali", "Kiran", "Sneha", "Arjun",
        "Ravi", "Anjali", "Kiran", "Sneha", "Arjun",
        "Ravi", "Anjali", "Kiran", "Sneha", "Arjun"
    ],

    "branch": [
        "Hyderabad", "Chennai", "Bangalore",
        "Hyderabad", "Chennai",
        "Bangalore", "Hyderabad", "Chennai",
        "Bangalore", "Hyderabad",
        "Chennai", "Bangalore", "Hyderabad",
        "Chennai", "Bangalore"
    ],

    "transaction_type": [
        "Deposit", "Withdrawal", "Deposit",
        "Withdrawal", "Deposit",
        "Deposit", "Withdrawal", "Deposit",
        "Withdrawal", "Deposit",
        "Deposit", "Withdrawal", "Deposit",
        "Withdrawal", "Deposit"
    ],

    "amount": [
        5000, 12000, 8000, 15000, 20000,
        7000, 18000, 25000, 30000, 10000,
        22000, 27000, 35000, 40000, 15000
    ]
}
df =pd.DataFrame(data)

total_amount = df["amount"].sum()

print("TOTAL TRANSACTION AMOUNT")
print(total_amount)

branch_amount = df.groupby("branch")["amount"].sum()

print("\nBRANCH-WISE TRANSACTIONS")
print(branch_amount)


top_branch = branch_amount.idxmax()
print(f"\nHIGHEST PERFORMING BRANCH: {top_branch}")

suspicious_transactions = df[df["amount"] > 25000]
print("\nSUSPICIOUS TRANSACTIONS")
print(suspicious_transactions[["customer", "amount"]])


customer_amount = df.groupby("customer")["amount"].sum()

print("\nCUSTOMER-WISE TRANSACTIONS")
print(customer_amount)

print("\nBANK STATISTICS")
print("average transaction amount:",np.mean(df["amount"]))
print("median transaction amount:",np.median(df["amount"]))
print("maximum transaction amount:",np.max(df["amount"]))
print("SD",np.std(df["amount"]))
branch_amount.plot(kind="bar")
plt.title("Branch-wise Transaction Amount")
plt.xlabel("Branch")
plt.ylabel("Transaction Amount")
plt.grid(axis='y')
plt.show()