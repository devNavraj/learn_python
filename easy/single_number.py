'''
Given a non-empty array of integers nums, every element appears twice 
except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use 
only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element 
which appears only once.
'''
class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for num in nums:
      result ^= num

    return result

    # # hash
    # dict = {}
    # for num in nums:
    #   try:
    #     dict[num] += 1
    #   except KeyError:
    #     dict[num] = 1

    # for num in nums:
    #   if dict[num] == 1:
    #     return num


if __name__ == "__main__":
  # begin
  s = Solution()
  
  print(s.singleNumber([2, 2, 1]))
  print(s.singleNumber([4, 1, 2, 1, 2]))
  print(s.singleNumber([1]))
    