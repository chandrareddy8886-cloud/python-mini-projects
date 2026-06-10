'''mylist=(input("Enter a list of items: "))
print(mylist)'''
# >>>>>>>>>>>>>>>>>>>>>>>>
"""n=[1,6,3,4,6,5,6,6,9,10,]
n.count(6)
print(n.count(6))"""
# >>>>>>>>>>>>>>>>>>>>>>>
"""x=(input("Enter marks of 6 students: "))
y= x.split()
y.sort()
print(y) """
# >>>>>>>>>>>>>>>>>>>>>>>>
# tuple
'''tuple=input("Enter a tuple of items: ")
print{tuple}'''
# >>>>>>>>>>>>>>>>>>>>>>>
'''list = [1,2,3,4,5,70,80]
x=sum(list)
print(x)'''
# >>>>>>>>>>>>>>>>>>>>>>>
'''a=[7,0,8,0,0,9]
print(a.count(0))'''
# >>>>>>>>>>>>>>>>>>>>>>>
'''list=[1,2,3,4,5]
y=len(list)
print(y)'''
# >>>>>>>>>>>>>>>>>>>>>>>
'''a=[1,3,4,3,5,3,6]
print(a.count(3))'''
# >>>>>>>>>>>>>>>>>>>>>>>split and max
'''a=input("enter the values")
x=a.split()
print(max(x))'''
# >>>>>>>>>>>>>>>>>>>>>>>split and min
'''a=input("enter the values")
x=a.split()
print(min(x))'''
# create a tuple
'''t=(1,2,3,4,5)'''
# lengh of tuple
'''t=(1,2,3,4,5)
len(t)
print(len(t))'''
# set
# >>>>>>>>>>>>>>>> pop()
'''s={45,67,9,54,7,5,9}
s.pop()
print(s)'''
# >>>>>>>>>>>>>>>>>>>>>>> len() in set
'''s={45,67,9,54,7,5,9}
len(s)
print(len(s))'''
# >>>>>>>>>>>>>>>>>>>>>>> add() in set
'''s={45,67,9,54,7,5,9}
s.add(66)
print(s)'''
# >>>>>>>>>>>>>>>>>>>>>>> remove() in set
'''s={45,67,9,54,7,5,9}
s.remove(7)
print(s)'''
# >>>>>>>>>>>>>>>>>>>>>>> clear() in set
'''s={45,67,9,54,7,5,9}
s.clear()
print(s)'''
# >>>>>>>>>>>>>>>>>>>>>>> union() in set
'''s={45,67,9,54,7,5,9}
s1={45,3,76,12,39,9,}
s2=s.union(s1)
print(s2)'''
# >>>>>>>>>>>>>>>>>>>>>>> intersection() in set
'''s={34,90,59,42,60}
s1={50,90,42,60,80}
s2=s.intersection(s1)
print(s2)'''
# >>>>>>>>>>>>>>>>>>>>>>> difference() in set
'''s={34,90,59,42,60}
s1={50,90,42,60,80}
s2=s.difference(s1)
print(s2)'''
# dictionary
# >>>>>>>>>>>>>>>>>>>>>>>> items() in dictionary
'''d={"name":"apple","age":"22","gender":"male"}
print(d.items())'''
# >>>>>>>>>>>>>>>>>>>>>>> keys() in dictionary
'''d={"name":"apple","age":"22","gender":"male"}
print(d.keys())'''
# >>>>>>>>>>>>>>>>>>>>>>> values() in dictionar
'''d={"name":"apple","age":"22","gender":"male"}
print(d.values())'''
# >>>>>>>>>>>>>>>>>>>>>>> get() in dictionary
'''d={"name":"apple","age":"22","gender":"male"}
print(d.get("age"))'''
# >>>>>>>>>>>>>>>>>>>>>>> update() in dictionary
'''d={"name":"apple",
   "age":"22",
   "gender":"male"}
d1=d.update({"caste":"reddy"})
print(d1)'''
# practice
# 1)
'''s=input("enter the values")

d={"paani":"water",
   "panka":"fan",
   'chaaval':"rice",
   "udna":"fly",}

print(d.get(s))'''
# 2)
'''s=input("enter the values")
s1=(s.split())
s2=set(s1)
print(s2)'''
# 3)
'''s={'18',18}
print(s)'''
'''4)What will be the length of following Set 6:
s=Set()
s.add (20)
s.add (20.0)
s.add ("20")'''
'''s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))'''
# 5)s={} what is the type of s?
'''s={}
print(type(s))'''
# 6)
'''s = {}

name1 = input("Enter the name1: ")
language1 = input("Enter the language: ")
s[name1] =language1

name2 = input("Enter the name2: ")
language2 = input("Enter the language: ")
s[name2] =language2

name3 = input("Enter the name3: ")
language3 = input("Enter the language: ")
s[name3] =language3

name4 = input("Enter the name4: ")
language4 = input("Enter the language: ")
s[name4] =language4
print(s)'''
# 7)names are same
'''s = {}

name1 = input("Enter the name1: ")
language1 = input("Enter the language: ")
s[name1] =language1

name2 = input("Enter the name2: ")
language2 = input("Enter the language: ")
s[name2] =language2
print(s)'''
# 8)names are same but language is different
'''s= {}

name1 = input("Enter the name1: ")
language1 = input("Enter the language: ")
s[name1] =language1

name2 = input("Enter the name2: ")
language2 = input("Enter the language: ")
s[name2] =language2
print(s)'''
# conditional statements
# 1)
'''a=int(input("enter the age:"))
if a >= 18:
    print("you are eligible for voting")
else:
     print("not eligible for voting")'''
# 2) find greatest number
'''a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
d=int(input("enter the 4rth number:"))

if  a>b and a>c and a>d:
     print(a,"is greater")

elif b>a and b>c and b>d:
     print(b,"is greater")
elif c>b and c>a and c>d:
     print(c,"is greater")
else :
     print(d,"is greater")
     '''
# 3)
'''a=int(input("enter first subject marks"))
b=int(input("enther the 2nd subject marks"))
c=int(input("enthe 3rd subject marks"))

if (a>33 and b>33 and c>33):
   (a+b+c/300)*100 >40
   print("pass")
else:
   print("fail")'''
# 4)
'''a=input(" give your comment")
if "click here" in a:
   print("spam detected")
elif "subscribe now" in a:
   print("spam detected")
elif "make money" in a:
   print("spam detected")
else:
   print("no spams") '''
# 5)
'''a=input("enther username")
if len(a)<10:
   print("length of characters are under 10")
else:
   print("username exceeds 10 characters")'''
# 6)
'''list=["chandra","nishanth","ramu","imran"]
a=input("enter name:")
if a in list:
    print("name exists in server")
else:
    print("no match")'''
# 7)
'''marks=int(input("enter the marks:"))
if 90<marks>100:
    print("EX grade")
elif 80<marks>90:
    print("A Grade")
elif 70<marks>80:
    print("B Grade")
elif 60<marks>70:
    print("c Grade")
elif 50<marks>60:
    print("D Grade")
else:
    print("fail")'''
# 8)
'''s=input("give the post:")
if "harry" in s.lower():
    print("talking about harry")
else:
    print("post not about harry")
    '''
# Loops>>>>>>>>>>>>>>>>>>>>>>>>>>
'''i=1
while i<=50:
    print(i)
    i=i+1
'''
# 1)
'''i=1
while i<=10:
    print(i)
    i=i+1'''
# 2)
'''i=10
while i>=1:
    print(i)
    i=i-1
#3)'''
'''i=2
while i<=20:
    print(i)
    i=i+2'''
# 4)
'''i=1
while i<=20:
    print(i)
    i=i+2'''
# 5)
'''i=5
while i<=50:
    print(i)
    i=i+5'''
# 6)
'''i=0
for i in range(1,100,10):
    print(i)'''
# 7)
'''i=20
for i in range(20,1,-2):
    print(i)'''
# 8)
'''i=1
for i in range(1,10,):
     print(i**2)'''
# 9)
i = 1
'''for i in range(1,31):
    if i%3==0:
       print(i)

'''
# 10)
i = 1
'''for i in range(1,51):
    if i%2==0 or i%5==0:
      print(i)'''
# 11)
'''i=0
for i in range(1,10):
    if i==6:
     continue
    print(i)'''
# 13)
"""i=0
for i in range (1,100):
    if i==9:
        break
    print(i)"""
# 14)sum patterns
'''sum=0
for i in range(1,11):
    sum=sum+i

print(sum)'''
# 15)
'''sum=0
for i in range(1,20):
    if i%2==0:
      sum=sum+i

print(sum)
#16)'''
'''sum=0
for i in range(1,20):
    if i%2!=0:
        sum=sum+i
print(sum)'''
# 17)
'''a=int(input("enter number:"))
for i in range(1,11):
    print(a*i)'''
# 18)
'''a=int(input("enter input:"))
for i in range(1,a):
    print(i+1)'''
# 19)
'''a=int(input("enter input"))
for i in range(a,1,-1):
    print(i-1)'''
# 20)
'''a=int(input("enter number"))
fact=1
for i in range(a,0,-1):
    if i*a:
        fact=fact*i
print(fact)'''
# 21)
'''a=input("enter  string :")
for i in a:
   print(i)'''
# 22)
'''a=[23,56,454,67,54,322]
big = a[0]
for i in a:
   if i>big:
      big=i
print(big)   '''
# 23)
'''a=[66,34,56,44,56,7,512]
min=a[0]
for i in a:
    if i<min:
        min=i
print(min)
'''
# 24)
'''list=[6,5,3,4,5,7,43,3,5,0,5,5]
count=0
for i in list:
    if i==5:
        count=count+1
print(count)'''
# 25)
'''a=[45,5,12,63,48,32,56]
sum=0
for i in a:
    sum=sum+i
print(sum)'''
# 26)
'''a=("enter string")
for i in a:
    print(i)

'''
# 27)
'''x=input("enter string :")
v=("a","e","i","o","u")
count=0
for i in x:
    if i in v:
     count = count+1
print(count)'''
# loops
'''a=0
for i in range(1,10,1):
    print(i)
'''
# 2)
'''a=int(input("enter number:"))
for i in range(1,11):
     print(a*i)'''
# 3)
'''list=["harry","sunny","sachin","ramu"]
for i in list:
    if i[0]=="s":
       print(i) '''
# 4)
'''i=0
while i<=10:
    print(i)
    i=i+1'''
# 5)
"""a=int(input("enter number"))
for i in range(2,a):
       if a%i==0:
          print("not a prime")
          break
else:
   print("prime number")"""
# 6)
'''a=int(input("enter input"))
i=1
total=0
while i<=a:
    total=total+i
    i=i+1
print(total)
    '''
# 7)
"""a=int(input('enter number'))
x=1
for i in range(a,0,-1):
    x=x*i
print(x)"""
# 8)

'''a=int(input("enter input"))
for i in range(1,a +1):
    star= "*"*i
    space= " " * (a-i)
    print(star+space)'''
# 9)
'''a=int(input("enter number :"))
for i in range(1,a+1):
    stars= "*"*(a-i)
    space= " "*(i)
    print(stars+space)'''
# 10)
'''a=0
for i in range(1,5+1):
    spaces="  "*(a-i)
    star="*"*(i)
    print(spaces+star)
for j in range(1,5):
     hash="#"*(i)
     print(hash)
     break
'''
# 11)
"""a=int(input("enter number :"))
for i in range(1,a+1):
    if i==a:
        print("#"*a)
    else:
        star ="*"*(a-i)
        space =" "*i
    print(space+star)
    """
# functions
# 1)
'''def greet():
    print("welcome to python programing")
greet()
greet()
greet()'''
# 2)
'''def inspire():
    print("im not in danger , im the danger:-pandu")
    print("pandu you are stoic")

inspire()'''

# 3) PARAMETERS
"""def show_age(name,age):
    print(name, "is", age, "old")
show_age("nishant",21)
show_age("pandu",22)
show_age("surya",25)"""
# 3)
"""def add_numbers(a,b):
    sum=a+b
    diff=a-b
    print("sum=" ,sum ,"diff=",diff)
add_numbers(7,6)
add_numbers(60,45)"""

# 4)
'''def fav_food(food):
        print("soumya allows",food)
fav_food("laddu")
fav_food("biryani")'''

# 5)  RETURN STATEMENT
'''

def multiply(a=5, b=10):
    return a*b


print(multiply())'''

# 6)
'''def square(num):
    return num**2
print(square(9))'''
# 7)


'''def countvowconso(userinput):
    countvowel = 0
    countconso = 0
    vowels = "aeiouAEIOU"
    for eachchar in userinput:
        if eachchar.isalpha():
            if eachchar in vowels:
                countvowel = countvowel+1
    else:
        countconso = countconso+1

    return  countvowel,countconso
countvowconso("chandra sekhar")
print(countvowconso("userinput"))'''

# file handling

# 1) read file and finding words are present or not

'''poem=open("twinkle.txt","r")

text=poem.read().lower()
textt=text.split()
user = input("enter the word : ")
if user.lower() in textt:
    print("found")
else:
    print("Not Found")
poem.close()
'''

# 2) update the new highscore in a file

'''x = int(input("enter new score : "))
print("current score = ", x)
a = open("highscore.txt", "r")
score = int(a.read())
# newhigh.close()

if x > score:
    # newhigh.write()
    with open("highscore.txt", "w") as f:
        f.write(str(x))
        print("New High Score =", x)
else:
    print(score, " is still high score")'''

# 3)create a folder of files containing tables 2 to 20

'''import os
if not os.path.exists("Tables"):
    os.mkdir("Tables")
for a in range(2, 21):
        with open(f"Tables/tables{a}.txt", "w") as f:
            for i in range(1, 11):
                tables = f"{a} X {i}= {a*i}\n"
                f.write(tables) '''

# 4)
"""with open("donkey.txt", "r") as f:
    donkey= f.read().lower()
    new = str(donkey).replace("donkey","######")
    with open("donkey.txt", "w")as f:
        f.write(new)
    print(new)
"""
# OOPS in python
# 1) create class and print two objects


'''class dog:
    def __init__(self, name):
        self.name = name


dog1 = dog("lucy")
dog2 = dog("tommy")
print(dog1.name)
print(dog2.name)'''

# 2)


'''class student:
    college="abc college"

s1 = student()
s2 = student()
s1.college="st marys"
s2.college="spec"
print(s1.college)
print(s2.college)'''

# 3)
'''class student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
s1=student("ravi",22,599)
s2=student("chandu",21,590)
s3=student("pani",21,567)
print(s1.name,s1.age,s1.rollno)
print(s2.name,s2.age,s2.rollno)
print(s3.name,s3.age,s3.rollno)
'''


"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("ravi\n", 58)
s2 = Student("daamu\n", 87)
s3 = Student("fahan\n", 94)
print(f"Name :{s1.name}Marks :{s1.marks}\n")
print(f"Name :{s2.name}Marks :{s2.marks}\n")
print(f"Name :{s3.name}Marks :{s3.marks}\n")"""

# 4)


'''class Programers:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary


employee1 = Programers("sunny", "analyst", "5 lpa",)
employee2 = Programers("ravi", "coder", "6 lpa")
employee3 = Programers("tillu", "tester", "5.5 lpa")'''

# 5)


'''class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(self.num**2)

    def cube(self):
        print(self.num**3)

    def squareroot(self):
        print(self.num**0.5)


num = int(input("enter number"))
cl = Calculator(num)
cl.square()
cl.cube()
cl.squareroot()'''

# 6)
'''class test:
    a=5
obj=test()
obj.a=0
print(test.a)'''

# 7)
'''class Calculator:
    @staticmethod
    def greet():
        print("hello")
Calculator.greet()'''
# 8)


"""class Train:
    a = "Indian Railways"

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"{self.seats}seats are available")

    def fare_info(self):
        print(f"Fare is ₹{self.fare}/-")

    def book(self):
        print("booking confirm")
        self.seats -= 1
train1 = Train("rajadhaani express", 500, 50)
train1.book()
train1.get_status()
train1.fare_info()
"""
# 1)
"""class car:
    brand="skoda"
    color="black"
    def show_detail():
        print(f"Brand : {car.brand}\ncolour : {car.color}")
car.show_detail()
"""
# 2)


'''class Student:
    def __init__(self, name, marks, result):
        self.name = name
        self.marks = marks
        self.result = result

    def show_details(self):
        print(f"Name : {self.name}\nMarks : {self.marks}")

    def is_pass(self):
        if (self.marks) >= 35:
            print("Pass")
        else:
            print("Fail")
student1 = Student("ravi",97,"")

student1.show_details()
student1.is_pass()'''

# INHERITENCE
# 1)


"""class Animal:
    def behave(self):
        print("animals eat and sleep")

class Dog(Animal):
    def dog(self):
        print("dog can bark")

d1 = Dog()
d1.behave()
d1.dog()
"""
# OOP


"""class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print(f"Brand : {self.brand}\nSpeed : {self.speed}")


car1 = Car("BMW", 320)
car2 = Car("Porsche", 400)
car1.show_details()
car2.show_details()"""

# 2)


'''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length*self.width)


rec1 = Rectangle(30, 15)
rec2 = Rectangle(50, 25)
print(rec1.area())
print(rec2.area())'''

# Inheritance
# 1)


'''class Person:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name is {self.name}\nAge is {self.age}")


class Student(Person):
    def study(self):
        return "studies for exam"


std1 = Student("Ravi", 22)
std2 = Student("hari", 21)
std1.introduce()
print(std1.study())
std2.introduce()
print(std2.study())'''

# overiding
#1)
'''class Vehicle:
    def start(self):
        print("vehicle started")
class Car(Vehicle):
    def start(self):
        super().start()
        print("car started")
car1=Car()
car1.start()'''

# Medium OOP
# BankAccount


'''class Bank:
    def __init__(self, name, balance):
        self.__balance = balance
        self.name = name

    def deposit(self, money):
        self.__balance+= money
        print(f"deposit amount ={money}/-")

    def withdraw(self, amount):
        print(f"withdraw ammount ={amount}/-")
        if amount > self.__balance:
                print("insufficient balance")
        if amount <= self.__balance:
            self.__balance -= amount
    def show_balance(self,):
        print(f"Account Balance ={self.__balance}/-")
acc = Bank("ravi", 4500)
acc.show_balance()
acc.deposit(549)
acc.show_balance()
acc.withdraw(7000)
acc.show_balance()'''

# 2)OOP

"""class Library:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        self.available=False
        print(f"Book1 borrowed")

    def return_book(self):
        self.available=True
        print(f"book3 is Returned ")

    def show_status(self):
        if self.available == True:
         print("available books :")
        else:
            print("Book is Not available")


book1 = Library("maths", "Ravi", True)
book2 = Library("physics", "Ram", False)
book3 = Library("chemistry", "chandu", True)
book1.borrow()
book2.show_status()
book3.return_book()"""

# OOP
# Inhertance


'''class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"\nEmployee name:{self.name}\nSalary:{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"Department :{self.department}")


employee1 = Manager("ravi", 12000, "IT")
employee2 = Manager("Candy", 18000, "HR")
employee1.show_details()
employee2.show_details()
'''
#OOP
#Animal Zoo

"""class Animal:
    def sound(self):
        print("Animals Make sounds")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("woof!")
class Cat(Animal):
    def sound(self):
        print("Meows!")
class Lion(Animal):
    def sound(self):
        print("Roars!")
dog=Dog()
cat=Cat()
lion=Lion()
dog.sound()
cat.sound()
lion.sound()"""