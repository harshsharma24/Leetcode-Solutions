# Problem (Two Sum):
# You’re given an array of integers nums and an integer target.
# Find any two distinct indices i and j such that nums[i] + nums[j] == target.

# Return the pair of indices [i, j]. You may return them in any order.

# How would you clarify requirements or constraints?

# Walk me through your high-level approach and its time/space complexity.

# Could you write out the code?

# How would you test your solution, and what edge cases would you consider?”


# nums=[2,7,5,8], target=9

# {
#     "2": 0
#     "7": 1
#     "5": 2
#     "8": 3

# }

# 2

# {
#     "2": 0
# }

# 7

def twoSum(nums,target):
    map={}

    for index,value in enumerate(nums):
        complement= target-value
        if complement in map:
            return [map[complement],index]
        else:
            map[value]= index

    return None


print(twoSum([1,2,7,8],9))

#I would ask what to do if the array is empty or there is no soln
# Time complexity- O(n) space also O(n)
