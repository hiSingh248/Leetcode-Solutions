# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        def bfs(root):
            res=[]
            queue=[root]            
            while queue:
                res.append([node.val for node in queue])
                n_q = []
                for node in queue:                                
                    if node.left:                   
                        n_q.append(node.left)
                    if node.right:
                        n_q.append(node.right)
                queue = n_q  
            return res
        fin=bfs(root)
        return fin
