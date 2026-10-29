# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def dfs(p,i):
            if not p or not i:
                return None
            root=TreeNode(p[0])
            m=i.index(p[0])
            root.left=dfs(p[1:m+1],i[:m])
            root.right=dfs(p[m+1:],i[m+1:])
            return root
        return dfs(preorder,inorder)