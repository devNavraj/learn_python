'''
	Given an array of integers, return indices of the two numbers such that 
  they add up to a specific target.
	You may assume that each input would have exactly one solution, and you 
  may not use the same element twice.
	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    self.nums = nums
    self.target = target
    lookup = {}

    for index, num in enumerate(self.nums):
      diff = self.target - num
      if diff in lookup:
        return [lookup[self.target-num], index]
      lookup[num] = index

if __name__ == '__main__':
  # begin
  s = Solution()
  
  print(s.twoSum([2, 7, 11, 15], 9))
  print(s.twoSum([3, 2, 4], 6))
  print(s.twoSum([3, 3], 6))
