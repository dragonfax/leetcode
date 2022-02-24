from typing import Optional, List, Tuple
from time import perf_counter
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
  
class Solution:

    def swap(self, previous, a):
      if a.next is None:
        return a
        
      b = a.next
      rest = b.next

      if previous:
        previous.next = b
      a.next = rest
      b.next = a

      return b

      
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

      didWork = True
      while didWork:

        curr = head
        prev = None
        first = True
        didWork = False
        while curr:
  
          b = curr.next
          if b is None:
            break
  
          if b.val < curr.val:
            curr = self.swap(prev, curr)
            if first:
              head = curr
            didWork = True
  
          first = False
  
          prev = curr
          curr = curr.next


      return head

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
  al = Solution().sortList(sl)
  end = perf_counter()
  a = fromList(al)
  print(f"{s}=> {a} == {a == e} {end - start}")
  
def test(s, e):
  start = perf_counter()
  a = Solution().minimumDeviation(s)
  end = perf_counter()
  print(f"{str(s)[:20]} => {a} == {e} {a == e}")

answer = fromList(Solution().swap(None,toList([0,1])))
assert answer == [1,0], answer

testList([5,4,3,2,1,0,-1],[-1,0,1,2,3,4,5])
testList([],[])
testList([0,1,2,3],[0,1,2,3])