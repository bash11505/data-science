import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data = {
    "user_id": range(1, 16),

    "user_name": [
        "Rahul", "Sneha", "Kiran", "Anjali", "Arjun",
        "Rahul", "Sneha", "Kiran", "Anjali", "Arjun",
        "Rahul", "Sneha", "Kiran", "Anjali", "Arjun"
    ],

    "genre": [
        "Action", "Comedy", "Drama", "Action", "Sci-Fi",
        "Drama", "Comedy", "Action", "Sci-Fi", "Drama",
        "Comedy", "Action", "Drama", "Sci-Fi", "Comedy"
    ],

    "watch_time_hours": [
        12, 8, 15, 20, 5,
        10, 18, 25, 7, 14,
        9, 22, 16, 6, 11
    ],

    "subscription_price": [
        499, 499, 699, 699, 499,
        699, 499, 999, 499, 699,
        499, 999, 699, 499, 499
    ],

    "month": [
        "Jan", "Jan", "Feb", "Feb", "Mar",
        "Mar", "Apr", "Apr", "May", "May",
        "Jun", "Jun", "Jul", "Jul", "Aug"
    ]
}
df = pd.DataFrame(data)
df = pd.DataFrame(data)


total_revenue = df["subscription_price"].sum()

print("TOTAL SUBSCRIPTION REVENUE")
print(total_revenue)


genre_watch = df.groupby("genre")["watch_time_hours"].sum()

print("\nWATCH TIME BY GENRE")
print(genre_watch)


top_genre = genre_watch.idxmax()

print("\nMOST POPULAR GENRE")
print(top_genre)



inactive_users = df[df["watch_time_hours"] < 8]

print("\nINACTIVE USERS")
print(inactive_users[["user_name", "watch_time_hours"]])


monthly_watch = df.groupby("month")["watch_time_hours"].sum()

print("\nMONTHLY WATCH TIME")
print(monthly_watch)


print("\nPLATFORM STATISTICS")

print("Average Watch Time:",
    np.mean(df["watch_time_hours"]))

print("Maximum Watch Time:",
    np.max(df["watch_time_hours"]))

print("Minimum Watch Time:",
    np.min(df["watch_time_hours"]))

print("Standard Deviation:",
np.std(df["watch_time_hours"]))
monthly_watch.plot(kind='bar')
plt.title("Monthly Watch Time")
plt.xlabel("Month")
plt.ylabel("Watch Hours")
plt.grid(axis='y')
plt.show()
