'''
Create a program using any programming languages to find 
the distinct characters in a string.
'''
class Solution(object):
  def find_distinct_char(self, s):
    """
    :type s: str
    :rtype: arr
    """
    # stack = []
    # for index, char in enumerate(s):
    #   if not stack:
    #     stack.append(char)
    #   elif char in stack:
    #     continue
    #   else:
    #     while stack and (char < stack[-1]):
    #       if stack[-1] in s[index + 1]:
    #         _ = stack.pop()
    #       else:
    #         break
    #     stack.append(char)
    # return "".join(stack)
    n = len(s)
    result = ""
    for i in range(0, n):
      flag = 0
      for j in range(0, i):
        if s[i] == s[j]:
          flag = 1
          break

      if flag == 0:
        result += s[i]
    return result

if __name__ == "__main__":
  # begin
  s = Solution()

  print("The distinct characters in the string is", s.find_distinct_char("cricket"))
  print("The distinct characters in the string is", s.find_distinct_char("developer"))