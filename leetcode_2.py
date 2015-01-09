class BinaryTreeNode:
    def __init__(self,root):
        self.key = root
        self.left_child = None 
        self.right_child = None
        
    def insert_left(self,new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self,new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t


def preorder(tree):
    if tree:
        print "#{tree.key}"
        preorder(tree.left_child)
        preorder(tree.right_child)
        
        
def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print "#{tree.key}"
        

#
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.
def max_depth(root):
    """ @return an integer
    param root, a tree node
    """
    if root == None:
        return 0
    ldepth = max_depth(root.left_node)    
    rdepth = max_depth(root.right_node)
    return max(ldepth,rdepth) + 1 
        
    
    
    
    
            
 
 
 
        
                        
                



                
                        
        
          
                
             
    
    