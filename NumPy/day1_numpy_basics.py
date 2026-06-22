import numpy as np

# 1. Create Arrays

print("1. Creating Arrays")
arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(arr2)
print()

# 2. Array Attributes

print("2. Array Attributes")
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)
print()

# 3. Special Arrays

print("3. Special Arrays")
zeros_arr = np.zeros((3, 3))
print("Zeros Array:")
print(zeros_arr)
ones_arr = np.ones((3, 3))
print("Ones Array:")
print(ones_arr)
full_arr = np.full((2, 2), 7)
print("Full Array:")
print(full_arr)
identity_arr = np.eye(4)
print("Identity Matrix:")
print(identity_arr)
print()

# 4. Sequence Arrays

print("4. Sequence Arrays")
arange_arr = np.arange(1, 11)
print("Arange:", arange_arr)
linspace_arr = np.linspace(1, 10, 5)
print("Linspace:", linspace_arr)
print()

# 5. Indexing

print("5. Indexing")
arr = np.array([10, 20, 30, 40, 50])
print("First Element:", arr[0])
print("Third Element:", arr[2])
print("Last Element:", arr[-1])
print()

# 6. Slicing

print("6. Slicing")
print("Elements 1 to 3:", arr[1:4])
print("First Three:", arr[:3])
print("From Index 2:", arr[2:])
print()

# 7. 2D Array Indexing

print("7. 2D Array Indexing")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix)
print("Element [0,1]:", matrix[0, 1])
print("Element [1,2]:", matrix[1, 2])
print()

# 8. Updating Elements

print("8. Updating Elements")
arr_update = np.array([10, 20, 30, 40])
print("Before Update:", arr_update)
arr_update[1] = 100
print("After Update:", arr_update)
print()

# 9. Practice Example

print("9. Student Marks Example")
marks = np.array([75, 80, 65, 90, 85])
print("Marks:", marks)
print("First Student:", marks[0])
print("Last Student:", marks[-1])
print("Top 3 Students:", marks[:3])
print()

# 10. Mini Exercise

print("10. Mini Exercise")
numbers = np.arange(1, 21)
print("Numbers:", numbers)
print("Even Numbers:", numbers[numbers % 2 == 0])
print("Odd Numbers:", numbers[numbers % 2 != 0])
print()