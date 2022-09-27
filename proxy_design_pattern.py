from abc import ABCMeta, abstractclassmethod


class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """ Inteface Method"""


class Person(IPerson):
    def person_method(self):
        print("I am a person!")
    

# proxy
class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()
    def person_method(self):
        print("I am the proxy functionality!")
        self.person.person_method()

p1 = Person()
p1.person_method()


p2 = ProxyPerson()
p2.person_method()