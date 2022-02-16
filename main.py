from typing import Optional, List
from time import perf_counter
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

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


def test(s, e):
  sl = toList(s)
  start = perf_counter()
  al = Solution().swapPairs(sl)
  end = perf_counter()
  a = fromList(al)
  print(f"{s}=> {a} == {a == e} {end - start}")


test([1,2,3,4],[2,1,4,3])
test([],[])
test([1], [1])

