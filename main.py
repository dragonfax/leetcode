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
    def isValidBST(self, root: Optional[TreeNode], minimum: Optional[int] = None, maximum: Optional[int] = None) -> bool:
      if not root:
        return True

      if minimum and root.val <= minimum:
        return False

      if maximum and root.val >= maximum:
        return False

      if root.left:
        if root.left.val >= root.val:
          return False
          
        if not self.isValidBST(root.left, minimum=minimum, maximum=root.val):
          return False

      if root.right:

        if root.right.val <= root.val:
          return False
          
        if not self.isValidBST(root.right, minimum=root.val, maximum=maximum):
          return False

      return True



Solution().sortedArrayToBST([-10,-3,0,5,9]).dump()