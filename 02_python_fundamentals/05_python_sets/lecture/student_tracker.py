student_info = ("Alice", "S001", 20)
student_name, student_id, student_age = student_info
grades = [85, 92, 78, 95, 88, 91]
alice_subjects = {"Math", "English", "Science", "History"}
bob_subjects = {"Math", "Art", "Science", "PE"}

# Add a new subject
alice_subjects.add("Music")

# Subjects both students share
shared = alice_subjects & bob_subjects

# Subjects only alice takes
only_alice = alice_subjects - bob_subjects

# All subjects across both students
all_subjects = alice_subjects | bob_subjects

print("name:", student_name)
print("id:", student_id)
print("age:", student_age)
print("grades:", grades)
print("shared with bob:", shared)
print("only alice:", only_alice)
print("total unique subjects:", all_subjects)
