class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show_details(self):
        print(f"Name  : {self.name}\nMarks : {self.marks}")
    def grade(self):
        if self.marks>=90:
            print(f"Grade A\n")
        elif self.marks>=75:
            print("Grade B\n")
        elif self.marks>=50:
            print("Grade C\n")
        else:
            print("Fail\n")
std1=Student("Ravi",95)
std2=Student("Arjun",47)
std3=Student("candy",70)
students=[std1,std2,std3]
for student in students:
     student.show_details()
     student.grade()

