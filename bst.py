class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.ins(self.root, new_val)
            
    def ins(self, current, new_val):
        if new_val < current.value:
            if current.right:
                self.ins(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.ins(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.sch(self.root, find_val)
        
    def sch(self, current, find_val):
        if current.value == find_val:
            return True
        
        if current.value < find_val and current.left:
            self.sch(current.left, find_val)
        elif current.right:
            self.sch(current.right, find_val)
        
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)