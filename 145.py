# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ress = []
        self.postorder(root, ress)
        return ress

    def postorder(self, root, arr):
        if not root:
            return
    
        self.postorder(root.left, arr)
        self.postorder(root.right, arr)
        arr.append(root.val)
