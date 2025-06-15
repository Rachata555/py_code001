class Student:
    student_count = 0
    def __init__(self, firstname,lastname, age, courses,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.courses = courses
        self.money = 0
        self.salary = salary
        Student.student_count = 0
        
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def display_info(self):
        print("Name:", self.get_fullname())
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("money", self.money)
        print("salary", self.salary)
        print("-" * 20)


student1 = Student("Alice", "Boder", 20, ["Math", "English"],15000)
student2 = Student("Bob","Ba", 22, ["Physics", "History"],20000)

student1.display_info()
student2.display_info()
print(student1.get_fullname())