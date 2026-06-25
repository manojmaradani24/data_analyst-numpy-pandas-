import pandas as pd

# 1. Create Series

print("1. Create Series")
series = pd.Series([10, 20, 30, 40, 50])
print(series)
print()

# 2. Create DataFrame using Dictionary

print("2. Create DataFrame")
student = {
    "ID":[101,102,103,104,105],
    "Name":["Rahul","Sneha","Amit","Priya","Ravi"],
    "Age":[20,21,19,22,20],
    "Marks":[85,91,78,88,95]
}
df = pd.DataFrame(student)
print(df)
print()

# 3. Head

print("3. First Five Records")
print(df.head())
print()

# 4. Tail

print("4. Last Five Records")
print(df.tail())
print()

# 5. Shape

print("5. Shape")
print(df.shape)
print()

# 6. Columns

print("6. Columns")
print(df.columns)
print()

# 7. Data Types

print("7. Data Types")
print(df.dtypes)
print()

# 8. Information

print("8. Information")
print(df.info())
print()

# 9. Describe

print("9. Statistical Summary")
print(df.describe())
print()

# 10. Selecting Single Column

print("10. Name Column")
print(df["Name"])
print()

# 11. Selecting Multiple Columns

print("11. Name and Marks")
print(df[["Name","Marks"]])
print()

# 12. iloc

print("12. iloc")
print(df.iloc[2])
print()

# 13. loc

print("13. loc")
print(df.loc[2])
print()

# 14. Access Specific Cell

print("14. Specific Cell")
print(df.loc[3,"Marks"])
print()

# 15. Add New Column

print("15. Add Grade Column")
df["Grade"]=["B","A","C","B","A"]
print(df)
print()

# 16. Update Value

print("16. Update Marks")
df.loc[0,"Marks"]=90
print(df)
print()

# 17. Drop Column

print("17. Drop Age")
new_df=df.drop(columns=["Age"])
print(new_df)
print()

# 18. Read CSV File

print("18. Read CSV")
sales=pd.read_csv("datasets/sales_data.csv")
print(sales.head())
print()

# 19. Shape of CSV

print("19. CSV Shape")
print(sales.shape)
print()

# 20. CSV Columns

print("20. CSV Columns")
print(sales.columns)
print()

# 21. CSV Information

print("21. CSV Info")
print(sales.info())
print()

# 22. CSV Summary

print("22. CSV Summary")
print(sales.describe())
print()

# 23. First Three Rows

print("23. First Three Rows")
print(sales.head(3))
print()

# 24. Last Two Rows

print("24. Last Two Rows")
print(sales.tail(2))
print()

# 25. Practice

print("25. Practice")
print("Average Price :",sales["Price"].mean())
print("Maximum Price :",sales["Price"].max())
print("Minimum Price :",sales["Price"].min())
print()