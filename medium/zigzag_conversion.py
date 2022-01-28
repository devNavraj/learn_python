class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
      return s

    result = ["" for _ in range(numRows)]
    row, down = 0, -1
    for char in s:
      result[row] += char

      if row == 0 or row == numRows - 1:
        down *= -1
      row += down

      # if row == numRows - 1:
      #   down = 0
      # if row == 0:
      #   down = 1

      # if down:
      #   row += 1
      # else:
      #   row -= 1

    final_string = ""
    for str in result:
      final_string += str

    return final_string

if __name__ == "__main__":
  # begin
  s = Solution()
  
  print(s.convert("PAYPALISHIRING", 3))
  print(s.convert("PAYPALISHIRING", 4))
