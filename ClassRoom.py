
class ClassRoom:
    total_count = 0
    def __init__(self,name,rollno,dept):
        self.name = name
        self.rollno =rollno
        self.dept = dept
        ClassRoom.total_count += 1
    @classmethod
    def no_of_students(cls):
        print(f"Total_student :{cls.total_count}")


class Student(ClassRoom):
    def __init__(self,name,rollno,dept,regNo):
        super().__init__(name,rollno,dept)
        self.regNo = regNo

    def student_details(self):
        print(f"Name : {self.name}")
        print(f"Roll no : {self.rollno}")
        print(f"Department : {self.dept}")
        print(f"Register NO : {self.regNo}")

    def Name(self):
        print(f"This is {self.name}")



s1 = Student("Deepak",304,"CSE",72282304)
s2 = Student("raj",222,"ECE",72282222)
s1.student_details()
s2.student_details()
Student.no_of_students()


lst = [Student("Deepak",304,"CSE",72282304)
, Student("raj",222,"ECE",72282222)]

for i in lst:
    print(i.student_details())

Student.no_of_students()

