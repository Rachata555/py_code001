class Student:
    def __init__(self, firstname,lastname, age, courses,money):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.courses = courses
        self.money = money
        


    def display_info(self):
        print("Name:", self.firstname , self.lastname)
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("money", self.money)
        print("-" * 20)


student1 = Student("Alice", "Boder", 20, ["Math", "English"],90)
student2 = Student("Bob","Ba", 22, ["Physics", "History"],10)

student1.display_info()
student2.display_info()