def student_data(student_id,student_name=None,student_class=None):
    print(f"Student ID:{student_id}")
    if student_name is not None:
        print(f"Student Name:{student_name}")
    if student_class is not None:
        print(f"Student Class:{student_class}")
s_id=input("Enter the student ID: ")
s_name=input("Enter the student name (optional): ")
s_class= input("Enter the student class (optional): ")
student_data(s_id,s_name,s_class)