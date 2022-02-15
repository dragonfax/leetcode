from typing import Optional, List
from time import perf_counter
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> str:
      longest = ""
      i = 0
      while i < len(s):
        # find the longest palindrome with this center
        p = self.findPalindrome(s,i, i)
        if p:
          if len(p) > len(longest):
            longest = p

        if i < len(s)-1 and s[i] == s[i+1]:
          # see if there is a longer paindrom with this as both center
          p = self.findPalindrome(s,i, i+1)
          if p:
            if len(p) > len(longest):
              longest = p
        i += 1
      return longest

    def findPalindrome(self, s: str, i: int, j: int) -> str:
      prev = s[i:j+1]
      while i > 0 and j < len(s)-1:
        i -= 1
        j += 1
        if s[i] != s[j]:
          break
        prev = s[i:j+1]
      return prev


def test(s, e):
  start = perf_counter()
  a = Solution().longestPalindrome(s)
  end = perf_counter()
  print(f"{s}=> {a} == {a == e} {end - start}")

test("babad","bab")
test("cbbd","bb")

