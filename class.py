'''
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        print(f"This is a class method. Class variable: {cls.class_variable}")

# Creating an instance of MyClass
obj = MyClass("I am an instance variable")

# Calling the class method on the class itself
MyClass.class_method()
'''
class Shape:
    @classmethod
    def create(cls, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Invalid shape type")

class Circle:
    def __init__(self):
        print("Creating a circle")

class Square:
    def __init__(self):
        print("Creating a square")

# Example usage:
circle_instance = Shape.create("circle")
square_instance = Shape.create("square")

