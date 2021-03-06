

# memory O(n)
# 2 pointers left and right and move to center
# set up alphaNum and call using self.alphaNum
class Solution:
  def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
    #move pointers to skip over nonalphanum chars
    while l < r and not self.alphaNum(s[l]):
      l += 1
    while l < r and not self.alphaNum(s[r]):
    r -= 1

    # check if pointers are equal, if not return false
    if s[l].lower() != s[r].lower():
      return False

    # move pointers toward the middle
    l += 1
    r -= 1

  return True

  def alphaNum(self, c):
     return (ord('A') <= ord(c) <= ('Z') or
      ord('a') <= ord(c) <= ('z') or
      ord('0') <= ord(c) <= ('9'))





#practice

class Solution:
  def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
      # skip c if nonalpha
      while l < r and not self.isalphaNum(s[l]):
        l += 1
      while r > l and not self.isalphaNum(s[r]):
        r -= 1

      if s[l].lower() != s[r].lower():
        return False

      l, r = l + 1, r - 1

    return True

  def isalphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
    ord('a') <= ord(c) <= ord('z') or
    ord('0') <= ord(c) <= ord('9') )





# this has space deficiencies
class Solution:
  def isPalindrome(self, s: str) -> bool:
    result = '' # uses extra memory

    for c in s:
      if c.isalnum():
        #lower case the string and concatenate if alphanumeric char
        result += c.lower()
      return result == result[::-1] # new string reversal uses extra memory
