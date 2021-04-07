# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBSTusingLevelOrderTraversal(self, root: TreeNode, low: int, high: int) -> int:
        """
        TC: O(N)
        SC: O(N)
        Status: Accepted
        """
        #do level order traversal concept and count result 
        rangeSum = 0
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            if node.val >= low and node.val <= high:
                rangeSum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return rangeSum
            




if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(10,TreeNode(5,TreeNode(3),TreeNode(7)),TreeNode(15,right=TreeNode(18)))
    print(obj.rangeSumBSTusingLevelOrderTraversal(root,7,15))
        