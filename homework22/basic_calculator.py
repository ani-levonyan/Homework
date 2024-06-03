# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.
class BasicCalculator:
    def __init__(self, num_1, num_2):
        if not isinstance(num_1, int) or not isinstance(num_2, int):
            raise TypeError("Only numbers are allowed")
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        return self.num_1 + self.num_2

    def subtract(self):
        return self.num_1 - self.num_2

    def multiply(self):
        return self.num_1 * self.num_2

    def divide(self):
        if self.num_2 == 0:
            raise ValueError("Division by zero is not allowed")
        return self.num_1 / self.num_2


calculator = BasicCalculator(4, 5)

print(calculator.multiply())
