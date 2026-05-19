import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {

    "product": [
        "Rice",
        "Milk",
        "Soap",
        "Rice",
        "Milk",
        "Shampoo",
        "Soap",
        "Rice",
        "Shampoo",
        "Milk"
    ],

    "category": [
        "Grocery",
        "Dairy",
        "Personal Care",
        "Grocery",
        "Dairy",
        "Personal Care",
        "Personal Care",
        "Grocery",
        "Personal Care",
        "Dairy"
    ],

    "units_sold": [
        20,
        30,
        15,
        25,
        18,
        10,
        12,
        22,
        8,
        35
    ],

    "price": [
        50,
        25,
        40,
        50,
        25,
        120,
        40,
        50,
        120,
        25
    ]
}

df = pd.DataFrame(data)


df["sales_amount"] = (
    df["units_sold"] * df["price"]
)


category_sales = (
    df.groupby("category")["sales_amount"].sum()
)

print("CATEGORY SALES")
print(category_sales)


top_category = (
    category_sales.idxmax()
)

print("\nTOP CATEGORY")
print(top_category)


low_products = (
    df[df["units_sold"] < 12]
)

print("\nLOW SELLING PRODUCTS")
print(
    low_products[
        ["product", "units_sold"]
    ]
)


print("\nAVERAGE SALES")
print(np.mean(df["sales_amount"]))

print("\nMAXIMUM SALES")
print(np.max(df["sales_amount"]))

print("\nMINIMUM SALES")
print(np.min(df["sales_amount"]))


sns.lineplot(
    x="category",
    y="sales_amount",
    data=df,
    color="Green"
)

plt.show()