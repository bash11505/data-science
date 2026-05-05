import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data = {
    "date":pd.date_range(start="2024-01-01",periods=10),
    "product":["A","B","C","A","B","C","A","B","C","A"],
    "units_sold":[10,15,8,60,90,57,86,58,78,47],
    "price":[100,200,300,400,200,180,150,253,300,124]
}
df=pd.DataFrame(data)
df["revenue"]=df["units_sold"]*df["price"]
product_sales=df.groupby("product")["revenue"].sum()
print("total revenue by product:")
print(product_sales)
df.groupby("date")["revenue"].sum().plot(kind='bar')
df.groupby("date")["revenue"].sum().plot(kind='line')
plt.title("daily revenue trend")
plt.xlabel("date")
plt.ylabel("revenue")
plt.grid(False)
plt.show()