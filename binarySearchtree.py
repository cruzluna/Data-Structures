# Tree Data Structure




''' Script to understand Binary Search Trees
 Binary tree -> at most two children per parent node
 Root node ->  the start of tree, no parent, and nothing precedes it
Binary Search Tree ->
    Left Child < Parent, Right Child > Parent  '''

class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    '''
    Adds Node to correct position within BST
    Time complexity-> log2(N)
    '''
    def add(self, current, value)->None:
        #check if there is a root node
        if not self.root:
            self.root = Node(value) #construct new node
        else:
            #recursive method to Add in correct order
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                else:
                    self.add(current.left, value)
            else:
                # greather than or the same 
                if not current.right:
                    current.right = Node(value)
                else:
                    self.add(current.right, value)
                    

    def visit(self, node):
        print(node.value)
    
    def preorder(self,root):
        return [root.value] + self.preorder(root.left) + self.preorder(root.right) if root else []
    
    def inorder(self,root):
        return   self.inorder(root.left) + [root.value]+ self.inorder(root.right) if root else []
    
    def postorder(self,root):
        return   self.postorder(root.left) + self.postorder(root.right) + [root.value] if root else []
        
    
        