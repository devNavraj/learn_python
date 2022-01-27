'''
	There are two sorted arrays nums1 and nums2 of size m and n 
  respectively. Find the median of the two sorted arrays. 
  The overall run time complexity should be O(log (m+n)).

	Example 1:
	nums1 = [1, 3]
	nums2 = [2]
	The median is 2.0

	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]
	The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # if len(nums1) > len(nums2):
    #   nums1, nums2 = nums2, nums1

    # m, n = len(nums1), len(nums2)
    # low, high = 0, m

    # while low <= high:
    #   partition1 = (low + high) // 2
    #   partition2 = (m + n + 1) // 2 - partition1

    #   if partition1 == 0:
    #     max_left1 = float('-inf')
    #   else:
    #     max_left1 = nums1[partition1 - 1]

    #   if partition1 == m:
    #     min_right1 = float('inf')
    #   else:
    #     min_right1 = nums1[partition1]

    #   if partition2 == 0:
    #     max_left2 = float('-inf')
    #   else:
    #     max_left2 = nums2[partition2 - 1]

    #   if partition2 == n:
    #     min_right2 = float('inf')
    #   else:
    #     min_right2 = nums2[partition2]

    #   if max_left1 <= min_right2 and max_left2 <= min_right1:
    #     if((m + n) % 2 == 0):
    #       return (max(max_left1, max_left2) + min(min_right1, min_right2) / 2.0)
    #     else:
    #       return max(max_left2, max_left1)

    #   elif max_left1 > min_right2:
    #     high = partition1 - 1

    #   else:
    #     low = partition1 + 1
    i = j = 0
    m, n = len(nums1), len(nums2)
    all_nums = []
    median = 0.0

    while i < m and j < n:
      if nums1[i] < nums2[j]:
        all_nums.append(nums1[i])
        i += 1
      else:
        all_nums.append(nums2[j])
        j += 1

    if i < m:
      while i < m:
        all_nums.append(nums1[i])
        i += 1

    if j < n:
      while j < n:
        all_nums.append(nums2[j])
        j += 1

    if (m + n) % 2 == 1:
      median = all_nums[(m + n) // 2]
    else:
      median = 1.0 * (all_nums[(m + n) // 2] + all_nums[(m + n) // 2 - 1]) / 2

    return median
    

if __name__ == '__main__':
  # begin
  s = Solution()
  
  print(s.findMedianSortedArrays([1, 2], [3, 4]))
  print(s.findMedianSortedArrays([1, 3], [2]))
