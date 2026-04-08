students = {
    "S001": {"name": "Alice", "grades": [85, 92, 78, 95, 88, 91]},
    "S002": {"name": "Bob", "grades": [70, 75, 80, 68, 90]},
    "S003": {"name": "Charlie", "grades": [95, 98, 92, 97]},
}

while True:
    student_id = input("\nEnter student ID to look up (or 'quit' to exit): ")
    if student_id == "quit":
        break
    if student_id in students:
        info = students[student_id]
        avg = sum(info["grades"]) / len(info["grades"])
        if avg >= 90:
            letter = "A"
        elif avg >= 80:
            letter = "B"
        elif avg >= 70:
            letter = "C"
        else:
            letter = "F"
        status = "pass" if avg >= 60 else "fail"
        print(
            f"Found: {info['name']}: avg={round(avg, 2)}, grade={letter}, status={status}"
        )
    else:
        print("Student not found, try again")
