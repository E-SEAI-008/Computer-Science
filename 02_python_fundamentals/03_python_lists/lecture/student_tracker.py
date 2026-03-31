student_name = "Alice"
student_id = "S001"
student_age = 20
grades = [85, 92, 78, 95, 88]

# Add a new grade
grades.append(91)

# Calculate average
average = sum(grades) / len(grades)

print("name:", student_name)
print("id:", student_id)
print("age:", student_age)
print("grades:", grades)
print("highest:", max(grades))
print("lowest:", min(grades))
print("average:", round(average, 2))
