# # Input: strs = ["flower","flow","flight"]
# # Output: "fl"

# solution = ""
# def longestPref(strs):
#   solution = ""

#   # sorting:
#   # sorting the array: sorted(strs)
#   # strs = ["flow", "flight", "flower"]
  

#   # for loop: 


# '''
# # find the min length 
# min_str=min(strs, key=len)
# for i in range(len(min_str)):
#     for w in strs:
#         if w[i] != min_str[i]:
#             return min_str[:i]
# return ""
      
# curr=flow as min_str
# f l i g h t with f l o w =>
# '''

words = ["flow", "flower", "flight"]
sorted_words = sorted(words)
print(sorted_words)
