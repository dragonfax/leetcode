from typing import Optional, List, Tuple
from time import perf_counter
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

  def deviation(self, nums: List[int]) -> int:
    return max(nums) - min(nums)

  def median(self, nums: List[int]) -> int:
    return sum(nums) / len(nums)

  def isEven(self, num: int) -> bool:
    return num % 2 == 0

  def indexOfLargest(self, nums: List[int]) -> int:
    largestNum = nums[0]
    largestIndex = 0
    for i in range(len(nums)):
      if nums[i] > largestNum:
        largestNum = nums[i]
        largestIndex = i
    return largestIndex

  def indexOfSmallest(self, nums: List[int]) -> int:
    smallestNum = nums[0]
    smallestIndex = 0
    for i in range(len(nums)):
      if nums[i] < smallestNum:
        smallestNum = nums[i]
        smallestIndex = i
    return smallestIndex

  def minimumDeviation(self, nums: List[int]) -> int:
    print("")
    print(f"{nums} {self.deviation(nums)} start")
    previousDev = None
    newNums, dev = self.minimumDeviationRound(nums)
    while previousDev is None or dev < previousDev:
      previousDev = dev
      newNums, dev = self.minimumDeviationRound(newNums)
    return int(min(dev,previousDev))
  
  def minimumDeviationRound(self, nums: List[int]) -> Tuple[List[int],int]:
    nums = nums.copy()
    
    lowest = self.deviation(nums)

    median = self.median(nums)
    deviations = [ max(median,x) - min(median,x) for x in nums]
    largestDeviationIndex = self.indexOfLargest(deviations)

    num = nums[largestDeviationIndex]
    if num > median:
      # decrease num, or increase others
      if self.isEven(num):
        nums[largestDeviationIndex] = int(nums[largestDeviationIndex] / 2)
      else:
        # find the lowest, can we multiply it?
        smallestIndex = self.indexOfSmallest(nums)
        smallestNum = nums[smallestIndex]
        if not self.isEven(smallestNum):
          nums[smallestIndex] = int(nums[smallestIndex] * 2)
    else:
      # increase num or decrease others
      if not self.isEven(num):
        nums[largestDeviationIndex] = int(nums[largestDeviationIndex] * 2)
      else:
        largestIndex = self.indexOfLargest(nums)
        largestNum = nums[largestIndex]
        if self.isEven(largestNum):
          nums[largestIndex] = int(nums[largestIndex] / 2)

    print(f"{nums} {self.deviation(nums)}")

    return (nums,self.deviation(nums))

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
  
def test(s, e):
  start = perf_counter()
  a = Solution().minimumDeviation(s)
  end = perf_counter()
  print(f"{s[:10]}=> {a} == {a == e} {end - start}")

test([1,2,3,4],1)
test([4,1,5,20,3],3)
test([2,10,8],3)
test([3,5],1)
test([2,8,6,1,6],1)

 