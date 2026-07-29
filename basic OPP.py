class Student:
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


s1 = Student("Omkar", 101)
s1.display()

'''
Name: Omkar
Roll No: 101
'''