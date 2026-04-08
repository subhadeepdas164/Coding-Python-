# Write a class for node and creat a tree and traverse it in preorder, inorder and postorder
class node:
    def __init__ (self,data):
        self.data = data
        self.left_node = None
        self.right_node = None
def insert(root, value):
    if(root is None):
        return node(value)
    else:
        if value <= root.data:
            root.left_node = insert(root.left_node,value)
        else:
            root.right_node = insert(root.right_node,value)
    return root
def inorder(root):
    if root:
        inorder(root.left_node)
        print(root.data, end = " ")
        inorder(root.right_node)    
def preorder(root):
    if root:
        print(root.data, end = " ")
        preorder(root.left_node)
        preorder(root.right_node)
def postorder(root):
    if root:
        postorder(root.left_node)
        postorder(root.right_node)
        print(root.data, end = " ")
add = node(10)
add = insert(add,5)     
add = insert(add,15)
add = insert(add,3) 
add = insert(add,7)

postorder(add)
print()
preorder(add)
print()
inorder(add)
