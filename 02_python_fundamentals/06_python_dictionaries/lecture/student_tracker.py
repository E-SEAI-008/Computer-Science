students = {
    "S001": {
        "name": "Alice",
        "age": 20,
        "grades": [85, 92, 78, 95, 88, 91],
        "subjects": {"Math", "English", "Science"},
    },
    "S002": {
        "name": "Bob",
        "age": 22,
        "grades": [70, 75, 80, 68, 90],
        "subjects": {"Math", "Art", "PE"},
    },
}

# Add a new student
students["S003"] = {
    "name": "Charlie",
    "age": 21,
    "grades": [95, 98, 92, 97],
    "subjects": {"Science", "History", "Music"},
}

# Print all students with their averages
for student_id, student_info in students.items():
    avg = sum(student_info["grades"]) / len(student_info["grades"])
    print(
        f"{student_id} - {student_info['name']}: avg={round(avg, 2)}, subjects={student_info['subjects']}"
    )
