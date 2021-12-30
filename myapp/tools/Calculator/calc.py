import operations


class Calculator:
    SUMA = operations.OperationType.ADD
    RESTA = operations.OperationType.SUBSTRACT
    MULTI = operations.OperationType.MULTIPLY
    DIVISION = operations.OperationType.DIVISION

    def calc(self, op, a, b):
        if op == self.SUMA:
            return operations.add(a, b)
        elif op == self.RESTA:
            return operations.sub(a, b)
        elif op == self.MULTI:
            return operations.mul(a, b)
        elif op == self.DIVISION:
            return operations.div(a, b)


if __name__ == "__main__":
    my_calc = Calculator()
    print(my_calc.calc(my_calc.SUMA, 1, 2))
