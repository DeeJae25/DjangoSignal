'''

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class
When an instance of the Rectangle class is iterated over,
we first get its length in the format:
{'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

'''


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = int(length)
        self.width = int(width)

        # Check if length is greater than width
        if self.length <= self.width:
            raise ValueError("Length must be greater than width")

    # Define the __iter__ method to make the class iterable
    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])

x, y = input("Enter two values (length width): ").split()
rect = Rectangle(x, y)

# Iterate over the Rectangle object
for item in rect:
    print(item)