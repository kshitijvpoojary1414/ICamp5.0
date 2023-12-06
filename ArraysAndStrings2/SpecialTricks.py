class SpecialTricks :
  def longestPalinfromicSubstring(self, s) :
    result = 0
    for i in range(len(s)-1) :
      result = max(result, maxPalindrome(i,i), maxPalindrome(i,i+1))
    return result
  
  def maxPalindrome(self, s, i, j) :
    while i >= 0 and j < len(s) :
      if s[i] != s[j] :
        return False 

    return True 