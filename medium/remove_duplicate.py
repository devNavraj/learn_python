'''
Given a string s, remove duplicate letters so that every letter 
appears once and only once. You must make sure your result is the 
smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
'''
class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    stack = []
    for index, char in enumerate(s):
      if not stack:
        stack.append(char)
      elif char in stack:
        continue
      else:
        while stack and (char < stack[-1]):
          if stack[-1] in s[index + 1]:
            _ = stack.pop()
          else:
            break
        stack.append(char)
    return "".join(stack)

if __name__ == "__main__":
  # begin
  s = Solution()

  print("The lexicographically smallest subsequence of s is", s.removeDuplicateLetters("bcabc"))
  print("The lexicographically smallest subsequence of s is", s.removeDuplicateLetters("cbacdcbc"))