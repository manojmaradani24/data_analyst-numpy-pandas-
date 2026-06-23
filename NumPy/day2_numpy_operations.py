import numpy as np

# 1. Reshape Arrays

print("1. Reshape Arrays")
arr = np.arange(1, 13)
print("Original Array:")
print(arr)
reshaped = arr.reshape(3, 4)
print("\nReshaped (3x4):")
print(reshaped)
print()

# 2. Flatten Arrays

print("2. Flatten Arrays")
flat = reshaped.flatten()
print(flat)
print()

# 3. Ravel Arrays

print("3. Ravel Arrays")
ravel_arr = reshaped.ravel()
print(ravel_arr)
print()

# 4. Addition

print("4. Addition")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)
print()

# 5. Subtraction

print("5. Subtraction")
print(a - b)
print()

# 6. Multiplication

print("6. Multiplication")
print(a * b)
print()

# 7. Division

print("7. Division")
print(a / b)
print()

# 8. Power

print("8. Power")
print(a ** 2)
print()

# 9. Square Root

print("9. Square Root")
arr = np.array([4, 9, 16, 25])
print(np.sqrt(arr))
print()

# 10. Sum

print("10. Sum")
marks = np.array([75, 80, 65, 90, 85])
print("Total:", np.sum(marks))
print()

# 11. Mean

print("11. Mean")
print("Average:", np.mean(marks))
print()

# 12. Median

print("12. Median")
print("Median:", np.median(marks))
print()

# 13. Standard Deviation

print("13. Standard Deviation")
print("Std:", np.std(marks))
print()

# 14. Variance

print("14. Variance")
print("Variance:", np.var(marks))
print()

# 15. Maximum

print("15. Maximum")
print("Max:", np.max(marks))
print()

# 16. Minimum

print("16. Minimum")
print("Min:", np.min(marks))
print()

# 17. Sorting

print("17. Sorting")
numbers = np.array([50, 10, 40, 20, 30])
print("Before Sort:", numbers)
print("After Sort:", np.sort(numbers))
print()

# 18. Argsort

print("18. Argsort")
print(np.argsort(numbers))
print()

# 19. Horizontal Stack

print("19. Horizontal Stack")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.hstack((a, b)))
print()

# 20. Vertical Stack

print("20. Vertical Stack")
print(np.vstack((a, b)))
print()

# 21. Concatenate

print("21. Concatenate")
print(np.concatenate((a, b)))
print()

# 22. Split Arrays

print("22. Split Arrays")
arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(arr, 3)
print(parts)
print()

# 23. Random Numbers

print("23. Random Numbers")
print(np.random.rand(5))
print()

# 24. Random Integers

print("24. Random Integers")
print(np.random.randint(1, 100, 10))
print()

# 25. Random Choice

print("25. Random Choice")
choices = ["Laptop", "Mobile", "Tablet"]
print(np.random.choice(choices))
print()

# 26. Mini Practice Project

print("26. Student Marks Analysis")
marks = np.array([75, 80, 65, 90, 85])
print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Sorted:", np.sort(marks))