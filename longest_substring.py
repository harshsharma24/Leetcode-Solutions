# Problem :
# You’re given a string s. Find the length of the longest substring without repeating characters and return that length.
# What clarifying questions would you ask before jumping in?

# Describe your high-level approach and its time/space complexity.

# Could you walk me through how your algorithm would work on the input s = "abcabcbb"?

# Finally, how would you implement this in code? Which edge cases would you test?”

# Go ahead and take us through your thought process.

# def longest_substring(s):
#     charSet=set()
#     l=0
#     maxLen=0
#     for r in range(len(s)):
#         while s[r] in charSet:
#             charSet.remove(s[l])
#             l+=1
#         charSet.add(s[r])
#         maxLen=max(maxLen,r-l+1)
    
#     return maxLen

# print(longest_substring('abbcdee'))




def longest_substring(s):
    char_set=set()
    maxLen=0
    l=0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l+=1
        char_set.add(s[r])
        maxLen=max(maxLen, r-l+1)

    return maxLen

print(longest_substring('pwwkew'))


    


            




    

