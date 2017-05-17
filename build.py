class Tree:
    def __init__(self,cargo,left = None,right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.cargo)

tree2 = Tree("+", Tree(1), Tree(("*"),Tree(2), Tree(3)))
# Prefix
def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

#Postfix
def print_tree_postfix(tree):
    if tree is None: return
    print_tree_postfix(tree.left)
    print_tree_postfix(tree.right)
    print(tree.cargo, end=" ")

#infix
def print_tree_infix(tree):
    if tree is None: return
    print_tree_infix(tree.left)
    print(tree.cargo, end=" ")
    print_tree_infix(tree.right)
    
    
print("Prefix: ")    
print_tree(tree2)
print("Postfix: ")
print_tree_postfix(tree2)
print("Infix: ")
print_tree_infix(tree2)

