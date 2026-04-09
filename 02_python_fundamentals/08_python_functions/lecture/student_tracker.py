def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)


def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "F"


def print_report(student_id, info):
    avg = calculate_average(info["grades"])
    letter = get_letter_grade(avg)
    status = "pass" if avg >= 60 else "fail"
    print(f"{student_id} - {info['name']}: avg={avg}, grade={letter}, status={status}")


students = {
    "S001": {"name": "Alice", "grades": [85, 92, 78, 95, 88, 91]},
    "S002": {"name": "Bob", "grades": [70, 75, 80, 68, 90]},
    "S003": {"name": "Charlie", "grades": [95, 98, 92, 97]},
}


for student_id, info in students.items():
    print_report(student_id, info)
