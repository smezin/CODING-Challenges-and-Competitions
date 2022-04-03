class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(1)
n2 = TreeNode(1)

print (n1 == n2)