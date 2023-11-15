#Home work
#1
dog = {}
#2
dog = {
    "name": "Valy",
    "age": 4,
    "color": "brown",
    "breed": "Akita"
}
#3
student = {
    "name":"Era",
    "lname":"Esteuov",
    "floor":"man",
    "age": 15,
    "country":"Kazakhstan",
    "marital_status":"good",
    "city":"Almaty",
    "skills": ["eat food", "reading book", "to run", "sit"]
}
print(student)
#4
print(len(student))
#5
print(student ["skills"])print(student ["skills"])
# 6
student["skills"].append("Lie down")
print(student)
student_keys = student.keys()
print(student_keys)
# 8
student_value = student.values()
print(student_value)
# 9
student_lists = student.items()
print(student_lists)
# 10
print(student.pop("city"))
# 11
del student
print(student)