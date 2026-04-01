student_info = ("Alice", "S001", 20)
student_name, student_id, student_age = student_info
grades = [85, 92, 78, 95, 88, 91]

average = sum(grades) / len(grades)

print("name:", student_name)
print("id:", student_id)
print("age:", student_age)
print("grades:", grades)
print("average:", round(average, 2))

# Swap two grades
grades[0], grades[-1] = grades[-1], grades[0]
print("grades after swap:", grades)

# Actual sorting
grades = [85, 92, 78, 95, 88, 91]

grades.sort()  # ascending
print(grades)

grades.sort(reverse=True)  # descending
print(grades)

sorted_grades = sorted(grades)  # returns new list, original unchanged
