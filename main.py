from typing import Optional, List
from time import perf_counter
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      pair = head
      prev = None
      head2 = None
      while pair:
        newhead, prev, pair = self.swapPair(prev,pair)
        if not head2:
          head2 = newhead
      return head2

    def swapPair(self,prev,pair):
      if not pair:
        return None, None, None
      
      a = pair
      b = a.next
      if not b:
        return a, None, None

      tmp = b.next
      b.next = a
      a.next = tmp
      if prev:
        prev.next = b

      return b, a,a.next


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
test([1,2,3,4,5,6,7,8,9], [2, 1, 4, 3, 6, 5, 8, 7, 9])
test([1,2],[2,1])
test([],[])
test([1], [1])

