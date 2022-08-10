from typing import Optional, List, Tuple
from time import perf_counter
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dump(self):
      stack = [self]
      while stack:
        print([ n.val for n in stack if n ])
        newStack = []
        for n in stack:
          if n.left:
            newStack.append(n.left)
          if n.right:
            newStack.append(n.right)
        stack = newStack
        
      
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

      if not nums:
        return None

      if len(nums) == 1:
        return TreeNode(nums[0])
      
      from math import floor
      rootIndex = floor(len(nums)/2)

      rootValue = nums[rootIndex]

      leftNode = None
      rightNode = None

      if rootIndex > 0:
        leftNode = self.sortedArrayToBST(nums[0:rootIndex])
      if rootIndex + 1 < len(nums):
        rightNode = self.sortedArrayToBST(nums[rootIndex + 1: len(nums)])
      
      root = TreeNode(rootValue, leftNode, rightNode)
      
      return root



Solution().sortedArrayToBST([-10,-3,0,5,9]).dump()