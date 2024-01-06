class Calculator:

    # create addNumbers static method
    @staticmethod
    def addNumbers(x, y, z):
        return x + y / z

print('Product:', Calculator.addNumbers(145, 115, 5))