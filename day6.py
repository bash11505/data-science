import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create company sales dataset
data = {
    "order_id": range(1, 16),

    "category": [
        "Electronics", "Clothing", "Electronics",
        "Home", "Clothing", "Electronics",
        "Home", "Clothing", "Electronics",
        "Home", "Clothing", "Electronics",
        "Home", "Clothing", "Electronics"
    ],

    "product": [
        "Laptop", "T-Shirt", "Mobile",
        "Chair", "Jeans", "Tablet",
        "Table", "Jacket", "Camera",
        "Sofa", "Shirt", "Monitor",
        "Bed", "Shoes", "Speaker"
    ],

    "units_sold": [5, 20, 10, 7, 15, 8, 6, 9, 4, 3, 11, 5, 2, 13, 7],

    "price": [50000, 1000, 20000, 7000, 1500, 25000,
              12000, 3000, 40000, 35000, 1200, 15000,
              45000, 2500, 8000],

    "month": [
        "Jan", "Jan", "Feb", "Feb", "Mar",
        "Mar", "Apr", "Apr", "May", "May",
        "Jun", "Jun", "Jul", "Jul", "Aug"
    ]
}

df = pd.DataFrame(data)

# Step 2: Create revenue column
df["revenue"] = df["units_sold"] * df["price"]

# Step 3: Total company revenue
total_revenue = df["revenue"].sum()

print("TOTAL COMPANY REVENUE")
print(total_revenue)

# Step 4: Revenue by category
category_revenue = df.groupby("category")["revenue"].sum()

print("\nREVENUE BY CATEGORY")
print(category_revenue)

# Step 5: Find top-selling category
top_category = category_revenue.idxmax()

print("\nTOP CATEGORY")
print(top_category)

# Step 6: Find low-performing products
low_products = df[df["units_sold"] < 5]

print("\nLOW PERFORMING PRODUCTS")
print(low_products[["product", "units_sold"]])

# Step 7: Monthly revenue trend
monthly_revenue = df.groupby("month")["revenue"].sum()

print("\nMONTHLY REVENUE")
print(monthly_revenue)

# Step 8: NumPy business statistics
print("\nBUSINESS STATISTICS")

print("Average Revenue:",
      np.mean(df["revenue"]))

print("Maximum Revenue:",
      np.max(df["revenue"]))

print("Minimum Revenue:",
      np.min(df["revenue"]))

# Step 9: Visualization
monthly_revenue.plot(kind='bar')

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(axis='y')

plt.show()