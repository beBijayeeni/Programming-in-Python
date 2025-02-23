class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def display_student_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Class:", self.student_class)
student1 = Student(1, "John Doe")
student1.student_class = "Grade 10" 
student1.display_student_info()
