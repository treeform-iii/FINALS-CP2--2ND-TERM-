#Peter Jorai M. Barraquias . . . Finals 2ND TERM . . . CS103 - 2 . . . Sir Maynard . . .
# 1. Vehicle and School Bus: abstraction , inheritance, polymorphism
class Vehicle:     
    def __init__(self, brand, model):       
        self.brand = brand
        self.model = model

    def engine_start(self):  # Abstract method 
        pass

class SchoolBus(Vehicle):   # Inherits Vehicle class
    def __init__(self, brand, model, capacity):     # Polymorphism, overrides the constructor
        super().__init__(brand, model)              # super() accesses attributes of parent "Vehicle" class
        self.capacity = capacity                    
        
    def engine_start(self):
        return f"The school bus {self.brand} {self.model} engine is starting."      # Polymorphism, overrides the engine_start method
    
    
 # 2. Employee with Multiple Constructors: encapsulation, polymorphism
class Employee:                                 
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod                                                        # polymorphis, this method overrides the constructor, using string format
    def EmployeeByString(cls, employee_info):                           # constructor to initialize employee from a string format --->  "Name-Position"
        name, position = employee_info.split('-')
        return cls(name, position)

    @classmethod                                                        # polymorphism, this method overrides the constructor, using dictionary format
    def EmployeeByDict(cls, employee_info):                             # constructor to initialize employee from a dictionary format ---> {"name": "Pedro", "position": "CEO"}
        return cls(employee_info['name'], employee_info['position'])

# 3. FirstSchool and SecondSchool: encapsulation , inheritance , composition
class Student:                                                          
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):                                                     
        return sum(self.grades) / len(self.grades)

class School:
    def __init__(self, name):
        self.name = name
        self.students = []             # Composition, uses a list of "Student" object without inheriting from "Student" class

    def add_student(self, student):     
        self.students.append(student)      # adds student object to the "self.students" which is the empty list

    def avg_grade(self):
        return sum(s.average() for s in self.students) / len(self.students)     # sums all student's average / count of students

class FirstSchool(School): pass                   # FirstSchool inherits from School
class SecondSchool(School): pass                  # SecondSchool inherits from School

# 4. Vector with Operator Overloading: Dunder methods (arithmethic functions; Double UNDERscore methods)
class Vector:
    def __init__(self, x, y):                   
        self.x = x
        self.y = y

    def __add__(self, other):                               # Dunder method used for "+"
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):                                     # Dunder method used for readability
        return f"Vector({self.x}, {self.y})"

# 5. Book and Author: composition
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author                                # Composition; uses author object in author class 

    def details(self):
        return f"'{self.title}' by {self.author.name} ({self.author.nationality})"      

#  - - - OUTPUT - - - 

# 1. Vehicle/SchoolBus
bus = SchoolBus("Ashok Leyland", "STAG", 40)
print("< - - - Vehicle/School Bus - - - >")
print("Instance CHECKER using isinstance(); Result =", isinstance(bus, Vehicle))
print(bus.engine_start(),"\n")

# 2. Employee
e1 = Employee("Linus", "Developer")
e2 = Employee.EmployeeByString("MarkleeBrownWee-Designer")
e3 = Employee.EmployeeByDict({"name": "Karen", "position": "Manager"})

print("< - - - Employee - - - >")
print(f"Employee1 ---> regular constructor):   | Name = {e1.name}, Position = {e1.position}")
print(f"Employee2 ---> string constructor):    | Name = {e2.name}, Position = {e2.position}")
print(f"Employee3 ---> dictionary constructor):| Name = {e3.name}, Position = {e3.position}\n")

# 3. Schools
s1 = FirstSchool("Shadow School")
s1.add_student(Student("John Smith", [90, 80]))
s1.add_student(Student("Mundane Mann", [80, 80]))

print("< - - - Schools - - - >")
print(s1.name, "| GPA =", s1.avg_grade())

s2 = SecondSchool("FairyTail School")
s2.add_student(Student("Mark", [90, 92]))
s2.add_student(Student("Liza", [78, 84]))
print(s2.name, "| GPA =", s2.avg_grade(),"\n")

# 4. Vector
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print("< - - - Vectors - - - >")
print("v1 (1, 2) + v2 (3, 4)")
print("Resultant Vector =", v3,"\n")

# 5. Book & Author
auth = Author("Rick Riordan", "American")                   # create author object first named auth
book = Book("The Lost Hero", auth)                          # then transfer that  author object to book 

print("< - - - Book & Author - - - >")
print(book.details())
