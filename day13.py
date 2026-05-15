import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "brand": [
        "Samsung",
        "Apple",
        "OnePlus",
        "Samsung",
        "Apple",
        "OnePlus",
        "Samsung"
    ],

    "units_sold": [
        20,
        15,
        10,
        18,
        12,
        8,
        25
    ],

    "price": [
        30000,
        70000,
        40000,
        32000,
        72000,
        41000,
        31000
    ]
}

df = pd.DataFrame(data)


df["revenue"] = (
    df["units_sold"] * df["price"]
)


brand_revenue = (
    df.groupby("brand")["revenue"].sum()
)

print("BRAND REVENUE")
print(brand_revenue)


top_brand = brand_revenue.idxmax()

print("\nTOP BRAND")
print(top_brand)


low_sales = df[df["units_sold"] < 10]

print("\nLOW SALES PRODUCTS")
print(low_sales)


print("\nAVERAGE REVENUE")
print(np.mean(df["revenue"]))

print("\nMAXIMUM REVENUE")
print(np.max(df["revenue"]))

sns.barplot(
    x="brand",
    y="revenue",
    data=df
)

plt.show()