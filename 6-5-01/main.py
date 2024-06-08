# edge case: empty string is substr of all str

# both input strings are the same
# len(str1) < len(str2)

# approach to solve: sliding window 

# is str2 is substring of str1
def is_substr(large_str, small_str):
  # get the length of both strs
  big_len = len(large_str)
  small_len = len(small_str)
  
  # edge case: small string is empty string : always results true
  if(small_len == 0) :
    return True
    
  if small_len > big_len:
    return False
    
  # for loop: sliding window
  # CATTTTTTTUT
  # TUT
  # range = 3: CAT with TUT (first iteration of i)
  # range = 3: TUT with TUT (first iteration of i)
  for i in range(big_len - small_len):
    for j in range(small_len):
      if(large_str[i+j] == small_str[j]):
        if(j == (small_len - 1)):
          return True

  return False
  