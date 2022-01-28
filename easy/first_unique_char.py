'''
Given a string s, find the first non-repeating character in it 
and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 
Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
'''

class Solution(object):
  def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = ""
    count_dict = {}
    for char in s:
      if char in count_dict:
        count_dict[char] += 1
      else:
        count_dict[char] = 1

    for i, char in enumerate(s):
      if count_dict[char] == 1:
        return i
    return -1

if __name__ == "__main__":
  # begin
  s = Solution()

  print("The first non-repeating character index is", s.firstUniqChar("leetcode"))
  print("The first non-repeating character index is", s.firstUniqChar("loveleetcode"))
  print("The first non-repeating character index is", s.firstUniqChar("aabb"))
