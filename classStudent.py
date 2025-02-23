class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
student_obj = Student("Alice", 20, "A")
student_obj.display_info()
print(f"Type of Student class: {type(Student)}")
print(f"Attribute keys of Student class: {Student.__dict__}")
print(f"Value of __module__ attribute: {Student.__module__}")
