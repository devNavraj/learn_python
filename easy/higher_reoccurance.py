'''
Given an integer array of size n, find all elements that 
appear more than ⌊n/3⌋ times.
'''
class Solution(object):
  def higher_reoccurance(self, nums):
    '''
    :type nums: List[int]
    :rtype: List[int]
    '''
    result = []
    # hash
    dict = {}
    n = len(nums)
    for num in nums:
      if num in dict:
        dict[num] += 1
      else:
        dict[num] = 1

    for num in sorted(nums):
      if dict[num] > (n // 3):
        result.append(num)

    return set(result)

if __name__ == "__main__":
  # begin
  s = Solution()

  print("Elements that appear more than ⌊ n/3 ⌋ times are", s.higher_reoccurance([1,1,1,1,1,2,2,2,2,2,3,3,3]))
  print("Elements that appear more than ⌊ n/3 ⌋ times are", s.higher_reoccurance([2,2,3,2]))
  print("Elements that appear more than ⌊ n/3 ⌋ times are", s.higher_reoccurance([ 2, 2, 3, 1, 3, 2, 1, 1]))

