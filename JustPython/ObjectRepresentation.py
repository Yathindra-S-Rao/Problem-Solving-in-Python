# @author: Yathindra S.
# Program to print the objects using Object Representation __repr__


class Student:
    
    def __init__(self, name, age):
        self.student_name = name
        self.student_age = age
    
    def __repr__(self):
        return (f'Student(student_name = {self.student_name}, student_age = {self.student_age})')
    
if __name__=='__main__':
    student_info = Student('Arun', '15')
    print(student_info)
