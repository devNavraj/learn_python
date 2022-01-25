'''
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0
'''

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class LinkList:
  def __init__(self):
    self.head = None
  
  def init_list(self, data):
    # creating head node
    self.head = ListNode(data[0])
    r = self.head
    p = self.head
    for i in data[1:]:
      node = ListNode(i)
      p.next = node
      p = p.next
    return r

  def print_list(self, head):
    if head == None: return
    node = head
    while node != None:
      print(node.val, end=' ')
      node = node.next

class Solution(object):
  def getDecimalValue(self, head):
      """
      :type head: ListNode
      :rtype: int
      """
      # result = ''

      # if not head:
      #   return 0

      # while head:
      #   result += str(head.val)
      #   head = head.next

      # return int(result, 2)

      result = 0
      while head:
        result = result*2 + head.val
        head = head.next

      return result

      # t, node_n=head, 0
      # while(t):
      #   node_n+=1
      #   t=t.next
      # sum_n=0
      # for i in range(node_n):
      #   x=head.val
      #   sum_n+=x*2**(node_n-1-i)
      #   head=head.next
      # return sum_n

if __name__ == '__main__':
  # begin
  s = Solution()
  ob = LinkList()
  # creating an empty array
  arr = []

  # number of elements as input
  n = int(input('Enter the number of elements in the array: '))

  # iterating till the range
  for i in range(0, n):
    element = int(input('Enter the elements of input array: '))
    arr.append(element) # adding the element
  print(arr)

  # making the linked list
  head = ob.init_list(arr)
  print(head)

  print('The equivalent decimal value of the numbers in the linked list is', s.getDecimalValue(head))