import pandas as pd

print("========== DAY 6 : SALES DATA ANALYSIS PROJECT ==========\n")

# 1. Read CSV
print("1. Read CSV File")

df = pd.read_csv("datasets/sales_data.csv")

print(df)
print()

# 2. Dataset Information
print("2. Dataset Information")

print(df.info())
print()

# 3. Statistical Summary
print("3. Statistical Summary")

print(df.describe())
print()

# 4. Total Sales Amount
print("4. Total Sales Amount")

df["Total Sales"] = df["Quantity"] * df["Price"]

print(df[["Product", "Quantity", "Price", "Total Sales"]])
print()

# 5. Overall Revenue
print("5. Overall Revenue")

print(df["Total Sales"].sum())
print()

# 6. Product Wise Revenue
print("6. Product Wise Revenue")

product_sales = df.groupby("Product")["Total Sales"].sum()

print(product_sales)
print()

# 7. Category Wise Revenue
print("7. Category Wise Revenue")

category_sales = df.groupby("Category")["Total Sales"].sum()

print(category_sales)
print()

# 8. Region Wise Revenue
print("8. Region Wise Revenue")

region_sales = df.groupby("Region")["Total Sales"].sum()

print(region_sales)
print()

# 9. Average Price
print("9. Average Price")

print(df["Price"].mean())
print()

# 10. Maximum Price
print("10. Maximum Price")

print(df["Price"].max())
print()

# 11. Minimum Price
print("11. Minimum Price")

print(df["Price"].min())
print()

# 12. Highest Revenue Product
print("12. Highest Revenue Product")

print(product_sales.idxmax())
print()

# 13. Lowest Revenue Product
print("13. Lowest Revenue Product")

print(product_sales.idxmin())
print()

# 14. Sort by Revenue
print("14. Sort by Revenue")

print(df.sort_values(by="Total Sales", ascending=False))
print()

# 15. Pivot Table
print("15. Pivot Table")

pivot = pd.pivot_table(
    df,
    values="Total Sales",
    index="Region",
    columns="Category",
    aggfunc="sum"
)

print(pivot)
print()

# 16. Top 5 Expensive Products
print("16. Top 5 Expensive Products")

print(df.nlargest(5, "Price"))
print()

# 17. Cheapest Products
print("17. Cheapest Products")

print(df.nsmallest(5, "Price"))
print()

# 18. Region Wise Average Sales
print("18. Region Wise Average Sales")

print(df.groupby("Region")["Total Sales"].mean())
print()

# 19. Product Count
print("19. Product Count")

print(df["Product"].value_counts())
print()

# 20. Business Insights
print("20. Business Insights")

print("Overall Revenue :", df["Total Sales"].sum())
print("Average Price :", df["Price"].mean())
print("Most Sold Product :", df["Product"].mode()[0])
print("Highest Revenue Product :", product_sales.idxmax())
print("Best Performing Region :", region_sales.idxmax())
print()

# 21. Save Final Report
print("21. Save Report")

df.to_csv("datasets/final_sales_report.csv", index=False)

print("Report Saved Successfully")
print()

print("========== DAY 6 COMPLETED ==========")
