class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.insert(22)


#root.PrintTree()

number = 23
#print(root.left.data)


#Checking the closest match. Here we are bascially making a variable closMatch. It is a node, imaginary one, whose value is equal to infinty. We are making it infinity because we want the closeMatch to be the root node value in first iteraction. Afterwards 

closeMatch = 10000

def checkClose(root,number,closeMatch):
    if root is not None and number < root.data:
        if abs(closeMatch - number) > abs(number - root.data):
            closeMatch = root.data
        print(root.data,number,closeMatch)
        checkClose(root.left,number,closeMatch);
    elif root is not None and number > root.data:
        if abs(closeMatch - number) > abs(number - root.data):
            closeMatch = root.data
        print(root.data,number,closeMatch)
        checkClose(root.right,number,closeMatch);
    else:
        print(closeMatch)
        return (closeMatch
        
    
closeMatch2 = checkClose(root,number,closeMatch)

print(closeMatch2)
