'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity 
and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
 
Constraints
1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''
class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # bitmask
    ones = 0 # ones as a bitmask to represent the ith bit had appeared once.
    twos = 0 # twos as a bitmask to represent the ith bit had appeared twice.
    common_bit_mask = 0 # common_bit_mask as a bitmask to represent the ith bit had appeared three times.

    for num in nums:
      # one & arr[i]" gives the bits that are there in both 'ones' and new
      # element from arr[]. We add these bits to 'twos' using bitwise XOR
      twos ^= (ones & num)

      ones ^= num

      # The common bits are those bits which appear third time. So these
      # bits should not be there in both 'ones' and 'twos'. common_bit_mask
      # contains all these bits as 0, so that the bits can be removed from
      # 'ones' and 'twos'
      common_bit_mask = ~(ones & twos)
         
      # Remove common bits (the bits that appear third time) from 'ones'
      ones &= common_bit_mask
         
      # Remove common bits (the bits that appear third time) from 'twos'
      twos &= common_bit_mask

    return ones

if __name__ == "__main__":
  # begin
  s = Solution()
  
  print(s.singleNumber([2, 2, 3, 2]))
  print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
  print(s.singleNumber([1]))