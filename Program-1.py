class Calculator:
    #defining class where there would be 2 operands of float and one operation in str.
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    #add calculations here. convert the operation to lowercase if ADD in operation str it is converted to add.
    def calculate(self):
        if self.operation == "add":
            return self.a + self.b

        elif self.operation == "subtract":
            return self.a - self.b

        elif self.operation == "multiply":
            return self.a * self.b

        elif self.operation == "divide":
            if self.b == 0:
                return "Error: Division by zero!"
            return self.a / self.b

        else:
            return "Invalid operation!"