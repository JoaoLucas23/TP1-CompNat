class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  
        self.left = left  
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def get_all_nodes(self):
        nodes = [self]
        if self.left:
            nodes.extend(self.left.get_all_nodes())
        if self.right:
            nodes.extend(self.right.get_all_nodes())
        return nodes
    
    def view(self):
        if self.is_leaf():
            return str(self.value)
        else:
            left_str = self.left.view()
            right_str = self.right.view()
            return f'({left_str} {self.value} {right_str})'
        
    def depth(self):
        if self.is_leaf():
            return 1
        else:
            return 1 + max(self.left.depth(), self.right.depth())
    
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
