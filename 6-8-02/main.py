def helper(n):
  # base case
  if n == 1:
    return 0
  
  if n % 2 == 0:
    return 1 + helper(n/2)
  else:
    return min( 1 + helper(n+1), 1 + helper(n-1))


class Solution:
  def integerReplacement(self, n: int):
    # keep count of num of operations
    return helper(n)

print(Solution().integerReplacement(4))


  
