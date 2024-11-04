class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  
        self.left = left  
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def print(self):
        if self.is_leaf():
            return str(self.value)
        return f'({self.left.print()} {self.value} {self.right.print()})'
    
    def sum(x, y):
        return x + y

    def sub(x, y):
        return x - y
    
    def mul(x, y):
        return x * y

    def protected_division(x, y):
        if y == 0:
            return 0
        return x / y

    operators = {
        '+': sum,
        '-': sub,
        '*': mul,
        '/': protected_division
    }
