# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,val):
            if not root:
                return 0
            if root.val>=val:
                res=1
            else:
                res=0
            val=max(val,root.val)
            return res+dfs(root.left,val)+dfs(root.right,val)
        return dfs(root,root.val)

        