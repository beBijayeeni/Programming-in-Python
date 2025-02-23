class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def modify_attributes(self, new_name, new_marks):
        self.student_name = new_name
        self.marks = new_marks

    def print_attributes(self):
        print(f"Student Name: {self.student_name}")
        print(f"Marks: {self.marks}")
student1 = Student("John", 85)
print("Original values:")
student1.print_attributes()
student1.modify_attributes("Alice", 92)
print("Modified values:")
student1.print_attributes()
