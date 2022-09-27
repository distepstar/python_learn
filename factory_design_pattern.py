# Factory Design Pattern
# Abstract Class
from abc import  ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """ Interface Method """
        # blueprint only but doesn't have action inside



# Abstract class cannot instantiate -> Error
# p1 = IPerson()
class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"
    def person_method(self):
        print("I am student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"
    def person_method(self):
        print("I am teacher")

# Derived abstract class can instantiate
# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        # Exception
        return -1

# main section
if __name__ == "__main__":
    choice = input("What type of person do you wan to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()

