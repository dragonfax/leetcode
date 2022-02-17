from typing import Optional, List, Tuple
from time import perf_counter
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      s = self.combination(candidates, target)
      return [list(t) for t in s]

    def combination(self, candidates, target): #  -> set[Tuple]:
      answers = set()
      x = len(candidates)-1
      while x >= 0:
        i = candidates[x]
        new_target = target - i
        if new_target == 0:
          answers.add((i,))
        if new_target > 0:
          s = self.combination(candidates, new_target)
          if s:
            for t in s:
              t = (i,) + t
              answers.add(t)
        candidates = candidates[0:x]
        x -= 1
        
      return answers


def toList(s):
  root = None
  prev = None
  for v in s:
    n = ListNode(val=v)
    if prev:
      prev.next = n
    else:
      root = n
    prev = n

  return root
    
l = toList([3,2,1])
assert l.val == 3
assert l.next.val == 2

def fromList(n):
  l = []
  while n:
    l.append(n.val)
    n = n.next
  return l

l = fromList(ListNode(val=4,next=ListNode(val=5))) 
assert l == [4,5],l


def testList(s, e):
  sl = toList(s)
  start = perf_counter()
  al = Solution().swapPairs(sl)
  end = perf_counter()
  a = fromList(al)
  print(f"{s}=> {a} == {a == e} {end - start}")
  
def test(s, t, e):
  start = perf_counter()
  a = Solution().combinationSum(s, t)
  end = perf_counter()
  print(f"{s}=> {a} == {a == e} {end - start}")

test([2,3,6,7], 7, [[2,2,3],[7]])


