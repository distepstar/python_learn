# Encapsulation

class Person:
    def __init__(self, name, age, gender):
        # two underscroll are private values -> __name
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value

    @staticmethod
    def mymethod():
        print("Hello World!")

Person.mymethod()

p1 = Person("Mike", 20, "M")
print(p1.Name)


p1.Name = "Bob"
print(p1.Name)