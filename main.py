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

  def unique(self, nums: List[int]) -> List[int]:
    return list({x : True for x in nums})

  def minimumDeviation(self, nums: List[int]) -> int:
    print("")
    print(f"{str(nums)[:20]} {self.deviation(nums)} start")
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
        for i in range(len(nums)):
          if not self.isEven(nums[i]) and nums[i] * 2 <= num:          
            nums[i] = int(nums[i] * 2)
    else:
      # increase num or decrease others
      if not self.isEven(num):
        nums[largestDeviationIndex] = int(nums[largestDeviationIndex] * 2)
      else:
        for i in range(len(nums)):
          if self.isEven(nums[i]) and nums[i] / 2 >= num:
            nums[i] = int(nums[i] / 2)

    print(f"{str(nums)[:20]} {self.deviation(nums)}")

    return (self.unique(nums),self.deviation(nums))

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
  print(f"{str(s)[:20]} => {a} == {a == e} {end - start}")

test([1,2,3,4],1)
test([4,1,5,20,3],3)
test([2,10,8],3)
test([3,5],1)
test([2,8,6,1,6],1)
test([139502287,127662367,182874278,195316256,158258043,128106398,165570519,161630895,197087073,177018029,142241150,189463437,114131106,180827841,140563651,140631914,127439843,117651449,108277946,148148621,198133057,173477124,180664549,119749615,192791912,171503536,146780066,146619923,180198468,132326257,129079222,142091904,115753487,178875891,171861205,165113533,105888611,148201456,114722931,111227228,139403775,192371264,112237013,173895760,188650252,109366482,174511822,108640913,191279346,127663274,180400034,179515445,109423556,191502543,108986309,163189619,168756945,177284541,114642866,136718954,146122849,186435019,108451832,162317887,137725843,138164718,170588551,159632836,139405555,105243015,187461591,156505003,163176045,107100346,124266013,198186644,160653221,157330716,188843428,130131460,136191103,120065496,143836292,194312999,108470642,166356073,192320235,101600108,170925551,197600861,149364536,158492279,166594704,141871659,197119385,187931161,141314732,124536617,102505057,142054441,142144983,139492998,114061225,172915905,186326112,101258267,176016355,117310304,134565576,175774728,115461652,173657901,150872767,127024993,164739980,199913646,140093586,140579776,115345543,115718199,111611931,189004451,117768984,160145942,103569746,150336410,166224862,129187299,147130259,158224131,167485119,115017904,104014213,149432483,102127258,199320902,193569603,157552714,113431868,165365010,162721361,169993800,130956004,123456024,157811076,167771287,103114996,183508477,171322947,103516387,118407455,111055030,161774593,106983428,187953441,186774576,106113788,124972645,140254982,102498490,186169756,112171085,181140323,127509228,139727086,170141845,102263907,125782453,198344152,132630801,135853494,171044990,143562844,128452102,166392273,154488151,125841090,155342972,118665099,183467485,105245785,173770396,182229265,102072773,137044502,148387216,139608067,141567001,150810789,114476348,163267954,164259991,165425337,152560087,193558089,180008386,154925409,153149280,144881521,161927809,103701602,124355592,199332316,164457368,184521526,176380601,132487910,136872491,124394249,178518694,129959078,168807287,165621480,142432287,186679088,142687756,149852668,137400257,130710611,177159816,143972099,179566227,139405172,125527818,138882615,192825874,115915326,176351775,149859250,196724440,188496780,102484169,138858670,135845950,187121403,165486776,143305183,167154441,171152787,178418731,155915678,138488715,176113588,133032247,135266151,150545120,193146386,100587965,105628049,127805067,100092626,119758139,174858873,145984705,192910027,181173340,138042671,122308978,160770301,130394674,166492711,161910843,119184450,109853721,170848534,121342141,100838796,198131866,156427959,176020777,184930698,117558856,113507815,153587163,123588933,120472984,198163856,107901250,182464664,128964739,138765154,197553755,190480953,169538709,105129765,143353678,199607036,144583353,199403460,195738467,124778611,186233414,168628878,101977678,160897452,195801072,186941874,177230274,179583881,133909934,175430770,158050009,141158921,159321118,192978346,153948939,147725900,128959020,152949311,173602535,195643978,120013972,142084051,136108423,121580658,145565683,156257215,199766954,187813699,171156531,162645972,100216855,139697220,182202999,147699018,110023818,176058211,185321487,176811279,100190707,135798617,116045000,140572589,172900728,116145251,140651548,165834418,116121994,186652919,103162165,164716217,117471904,155970321,113282879,105493962,103599601,188489301,155340595,136108503,127347508,194267446],98683701)
 
 