# instance attributes takes over class attributes during assignemnet and retrival

class Student:
    year = "TY"
    age = 20  # class attribute

student = Student()
student.name = "Vaishnavi"
student.age = 19    # instance attribute
print(student.name,student.age,student.year)

