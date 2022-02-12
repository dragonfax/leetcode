from typing import Optional, List

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
  a = Solution().lengthOfLongestSubstring(s)
  print(f"{s}=> {a} == {a == e}")

test("abcabcbb",3)
test("bbbbbbbb",1)
test("pwwkew",3)
test("aab",2)

