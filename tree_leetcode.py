# class TreeNode:
#     def __init__(self,val,left,right):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


def dfs(node):
    if node == None:
        return
    dfs(node.left)
    dfs(node.right)
    return

def preorder_dfs(node):
    if not node:
        return
    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)
    return

def inorder_dfs(node):
    if not node:
        return
    inorder_dfs(node.left)
    print(node.val)
    inorder_dfs(node.right)
    return

def postorder_dfs(node):
    if not node:
        return
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val)
    return
# The name of each traversal is describing when the current node's logic is performed
# Pre -> before children
# In -> in the middle of children
# Post -> after children
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)

root.left = one
root.right = two

# print(root.left.val)
# print(root.right.val)
# Example 1: 104. Maximum Depth of Binary Tree
#
# Given the root of a binary tree, find the length of the longest path from the root to a leaf.
# Optional[TreeNode] 表示该参数可以是 TreeNode 类型的对象，也可以是 None（空值）
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1


class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If root is None, the tree is empty, so the depth is 0
        if not root:
            return 0

        # Create a stack to store nodes and their depths
        stack = [(root, 1)]

        # Initialize the maximum depth to 0
        ans = 0

        # Process nodes in the stack until it becomes empty
        while stack:
            # Pop a node and its depth from the stack
            node, depth = stack.pop()

            # Update the maximum depth if the current depth is larger
            ans = max(ans, depth)

            # Add the left child to the stack with depth incremented by 1
            if node.left:
                stack.append((node.left, depth + 1))

            # Add the right child to the stack with depth incremented by 1
            if node.right:
                stack.append((node.right, depth + 1))

        # Return the maximum depth of the binary tree
        return ans


def generate_test_data():
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    # Example 2
    root2 = TreeNode(1)

    # Example 3
    root3 = TreeNode(5)
    root3.left = TreeNode(3)
    root3.right = TreeNode(8)

    return [root1, root2, root3]


# Test the generated data
test_data = generate_test_data()
for i, root in enumerate(test_data, 1):
    solution = Solution1()
    depth = solution.maxDepth(root)
    print(f"Example {i}: Depth = {depth}")
