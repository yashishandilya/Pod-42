class Solution:

  def romanToInt(self, s: str) -> int:
    #  I 1 V 5 X 10 L 50 C 100 D 500 M 1000
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    sum = 0

    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    # 5, it is 4 = SUBTRACTION: 1
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    # 50, it maKES IT 40, SUBTRATION OF 10
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    # 500, it makes it 400, SUBTRACTION OF 100
    print(s)
    for char in s:
      sum += map[char]
    return sum


# O(15)
print(Solution().romanToInt("MMMCMXCIX"))
