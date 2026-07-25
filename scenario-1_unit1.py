# Student Management System using OOP

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print(f"Roll Number : {self.roll_no}")
        print(f"Name        : {self.name}")
        print(f"Marks       : {self.marks}")
        print(f"Grade       : {self.get_grade()}")
        print("-" * 30)


class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n----- Student Details -----")
        for student in self.students:
            student.display()


# Main Program
college = College()

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")
    roll_no = input("Roll Number: ")
    name = input("Name: ")
    marks = float(input("Marks: "))

    student = Student(roll_no, name, marks)
    college.add_student(student)

college.display_students()
