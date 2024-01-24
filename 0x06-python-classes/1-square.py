#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is less than 0.
        """
        self.__size = size

    def get_size(self):
        """Get the size of the square."""
        return self.__size

    def set_size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If value is less than 0.
        """
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

# Test the getter and setter
print("Size:", my_square.get_size())
my_square.set_size(5)
print("New size:", my_square.get_size())

