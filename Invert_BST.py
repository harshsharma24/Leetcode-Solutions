# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Base case: if node is None, return None
        if not root:
            return None
        
        # Swap left and right children
        temp=root.left 
        root.left=root.right  
        root.right= temp
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

def main():
    solution = Solution()
    
    # Create a simple binary tree:
    #       4
    #      / \
    #     2   7  

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    
    print("Original tree:")

    
    # Invert the tree
    inverted_root = solution.invertTree(root)
    

if __name__ == "__main__":
    main()