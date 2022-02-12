from typing import Optional, List
from time import perf_counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      largestSubLen = 0

      sub = {}
      for i in range(0,len(s)):
        a = s[i]
        if a not in sub:
          sub[a] = i
          subLen = len(sub)
          if subLen > largestSubLen:
            largestSubLen = subLen
        else:
          # remove that element, and all the ones before it. continue
          ai = sub[a]
          sub[a] = i
          for b in list(sub):
            bi = sub[b]
            if bi < ai:
              del sub[b]

      return largestSubLen

def test(s, e):
  start = perf_counter()
  a = Solution().lengthOfLongestSubstring(s)
  end = perf_counter()
  print(f"{s}=> {a} == {a == e} {end - start}")

test("abcabcbb",3)
test("bbbbbbbb",1)
test("pwwkew",3)
test("aab",2)

test("abcdefghijklmnopqrstufwxyz0123456789abcdefghijklmnopqrstufwxyz0123456789abcdefghijklmnopqrstufwxyz0123456789abcdefghijklmnopqrstufwxyz0123456789",35)
