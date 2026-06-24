import numpy as np

# Student Marks Dataset

marks = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 91],
    [65, 70, 68],
    [88, 86, 90]
])
print("Student Marks Dataset")
print(marks)
print()

# 1. Boolean Masking

print("1. Boolean Masking")
high_scores = marks > 85
print(high_scores)
print()

# 2. Filtering Data

print("2. Filtering Data")
filtered = marks[marks > 85]
print(filtered)
print()

# 3. Conditional Selection

print("3. Conditional Selection")
result = np.where(marks >= 80, "Pass", "Fail")
print(result)
print()

# 4. Copy vs View

print("4. Copy vs View")
original = np.array([10, 20, 30, 40])
view_arr = original.view()
copy_arr = original.copy()
original[0] = 100
print("Original:", original)
print("View:", view_arr)
print("Copy:", copy_arr)
print()

# 5. Broadcasting

print("5. Broadcasting")
arr = np.array([1, 2, 3, 4, 5])
print(arr + 10)
print()

# 6. Iterating Arrays

print("6. Iterating Arrays")
for row in marks:
    print(row)
print()

# 7. Iterate Each Element

print("7. Iterate Elements")
for element in np.nditer(marks):
    print(element, end=" ")
print("\n")

# 8. Save Array

print("8. Save Array")
np.save("student_marks.npy", marks)
print("File Saved Successfully")
print()

# 9. Load Array

print("9. Load Array")
loaded = np.load("student_marks.npy")
print(loaded)
print()

# MINI PROJECT

print("STUDENT MARKS ANALYSIS")

# Total Marks

total_marks = np.sum(marks, axis=1)
print("Total Marks")
print(total_marks)
print()

# Average Marks

average_marks = np.mean(marks, axis=1)
print("Average Marks")
print(average_marks)
print()

# Highest Scorer

highest_student = np.argmax(total_marks)
print("Highest Scorer Index:", highest_student)
print("Marks:", total_marks[highest_student])
print()

# Lowest Scorer

lowest_student = np.argmin(total_marks)
print("Lowest Scorer Index:", lowest_student)
print("Marks:", total_marks[lowest_student])
print()

# Subject Wise Average

subject_average = np.mean(marks, axis=0)
print("Subject Wise Average")
print(subject_average)
print()

# Students Above 80 Average

print("Students Above 80 Average")
top_students = average_marks > 80
print(top_students)
print()

# Ranking Students

print("Student Rankings")
ranking = np.argsort(total_marks)[::-1]
print(ranking)
print()

# Final Report

print("FINAL REPORT")
for i in range(len(total_marks)):
    print(
        f"Student {i+1}: "
        f"Total={total_marks[i]}, "
        f"Average={average_marks[i]:.2f}"
    )