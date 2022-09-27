class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Destructor
    def __del__(self):
        print("Destructor called")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Magic methods -> customise classes additions
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"X: {self.x} Y: {self.y}"
    def __len__(self):
        return 10 
    def __call__(self):
        print("Hello I'm the callback")


# Vectors
v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2

print(v3)
print(len(v3))

# p = Person("Mike", 25)
# del p