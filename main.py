from typing import Optional, List
from time import perf_counter
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      a = {}
      for n in nums:
        if n in a:
          del a[n]
        else:
          a[n] = True
      return list(a.keys())[0]



def test(s, e):
  start = perf_counter()
  a = Solution().singleNumber(s)
  end = perf_counter()
  print(f"{s}=> {a} == {a == e} {end - start}")

test([2,2,1],1)
test([4,1,2,1,2],4)
test([1],1)

