# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            size = len(q)
            current = []
            for i in range(size):
                temp = q.popleft()
                if temp:
                    current.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if current:
                result.append(current)
        return result


        