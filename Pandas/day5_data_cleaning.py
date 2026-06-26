import pandas as pd
import numpy as np

# 1. Read CSV File
print("1. Read CSV File")
df = pd.read_csv("datasets/sales_data.csv")
print(df)
print()

# 2. Check Missing Values
print("2. Missing Values")
print(df.isnull())
print()
print(df.isnull().sum())
print()

# 3. Create Sample Data with Missing Values
print("3. Sample Dataset")
student = {
    "Name": ["Rahul", "Sneha", None, "Priya", "Ravi"],
    "Age": [20, 21, np.nan, 22, 20],
    "Marks": [85, np.nan, 78, 88, 95]
}
students = pd.DataFrame(student)
print(students)
print()

# 4. Fill Missing Values
print("4. Fill Missing Values")
filled = students.fillna(0)
print(filled)
print()

# 5. Fill Missing Names
print("5. Fill Missing Names")
students["Name"] = students["Name"].fillna("Unknown")
print(students)
print()

# 6. Fill Missing Marks with Mean
print("6. Fill Marks with Mean")
mean_marks = students["Marks"].mean()
students["Marks"] = students["Marks"].fillna(mean_marks)
print(students)
print()

# 7. Fill Missing Age
print("7. Fill Age with Mean")
mean_age = students["Age"].mean()
students["Age"] = students["Age"].fillna(mean_age)
print(students)
print()

# 8. Drop Missing Rows
print("8. Drop Missing Rows")
sample = pd.DataFrame({
    "A":[1,2,None],
    "B":[5,None,7]
})
print(sample)
print()
print(sample.dropna())
print()

# 9. Duplicate Values
print("9. Duplicate Values")
duplicate = pd.DataFrame({
    "ID":[101,102,102,103,104,104],
    "Name":["A","B","B","C","D","D"]
})
print(duplicate)
print()
print("Duplicates")
print(duplicate.duplicated())
print()

# 10. Remove Duplicates
print("10. Remove Duplicates")
duplicate = duplicate.drop_duplicates()
print(duplicate)
print()

# 11. Rename Columns
print("11. Rename Columns")
new_df = df.rename(columns={
    "Product":"Item",
    "Price":"Cost"
})
print(new_df.columns)
print()

# 12. Change Data Type
print("12. Data Types")
print(df.dtypes)
print()
df["Quantity"] = df["Quantity"].astype(float)
print(df.dtypes)
print()

# 13. Filtering
print("13. Filter Quantity > 2")
print(df[df["Quantity"] > 2])
print()

# 14. Multiple Conditions
print("14. Multiple Conditions")
print(df[(df["Quantity"] > 2) & (df["Price"] > 1000)])
print()

# 15. Sorting
print("15. Sort by Price")
print(df.sort_values(by="Price"))
print()

# 16. Descending Sort
print("16. Descending")
print(df.sort_values(by="Price", ascending=False))
print()

# 17. Reset Index
print("17. Reset Index")
sorted_df = df.sort_values(by="Price")
print(sorted_df.reset_index(drop=True))
print()

# 18. Unique Values
print("18. Unique Categories")
print(df["Category"].unique())
print()

# 19. Value Counts
print("19. Category Count")
print(df["Category"].value_counts())
print()

# 20. Apply Function
print("20. Discount Price")
df["Discount Price"] = df["Price"] * 0.90
print(df)
print()

# 21. Insert Column
print("21. Profit Column")
df["Profit"] = df["Price"] * 0.20
print(df)
print()

# 22. Delete Column
print("22. Delete Profit")
df = df.drop(columns=["Profit"])
print(df)
print()

# 23. Export Cleaned Data
print("23. Export CSV")
df.to_csv("datasets/cleaned_sales_data.csv", index=False)
print("Cleaned CSV Saved")
print()