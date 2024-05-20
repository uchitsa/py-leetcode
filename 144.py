class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ress = []
        self.preorder(root, ress)
        return ress

    def preorder(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)
