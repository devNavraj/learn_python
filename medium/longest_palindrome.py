'''
	Given a string s, find the longest palindromic substring in s. 
  You may assume that the maximum length of s is 1000.

	Example 1:
	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.

	Example 2:
	Input: "cbbd"
	Output: "bb"
'''

class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    # table[i][j] will be false if substring
    # s[i..j] is not palindrome. Else
    # table[i][j] will be true
    table = [[0 for _ in range(len(s))] for _ in range(len(s))]
    # All substrings of length 1 are palindromes
    max_len = 1
    result = ''

    for i in range(len(s)):
      table[i][i] = 1
      result = s[i]

    length = 2

    while length <= len(s):
      # Fix the starting index
      i = 0
      while i < len(s) - length + 1:
        # Get the ending index of substring from starting index i 
        # and length
        j = i + length - 1

        # check for sub-string of length 2
        if length == 2 and s[i] == s[j]:
          table[i][j] = 1
          max_len = max(max_len, 2)
          result = s[i:j+1]
        # checking for sub-string from ith index to jth index iff
        # s[i + 1] to s(j-1)] is a palindrome
        elif s[i] == s[j] and table[i+1][j-1]:
          table[i][j] = 1
          if length > max_len:
            max_len = length
            result = s[i:j+1]
        i += 1
      length += 1
    return result

if __name__ == '__main__':
  # begin
  s = Solution()
  
  print(s.longestPalindrome('babad'))
  print(s.longestPalindrome('cbbd'))


    
