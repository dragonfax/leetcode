from typing import Optional, List, Tuple
from time import perf_counter
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
      if k == 0:
        return num

      best_new_num = num
      for i in range(len(num)):
        new_num = num[0:i] + num[i+1:]
        new_num = new_num if new_num else "0"
        k2 = k - 1
        best = self.removeKdigits(new_num, k2)
        if int(best) < int(best_new_num):
          best_new_num = best

      return str(int(best_new_num))
          


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
  a = Solution().removeKdigits(s, t)
  end = perf_counter()
  print(f"{s}=> {a} == {a == e} {end - start}")

test("1432219",3,"1219")
test("10200",1,"200")
test("10",2,"0")


