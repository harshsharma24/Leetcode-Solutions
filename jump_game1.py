# 2 3 1 1 4
# stack= [0]
# visited=(0, 2, 3)
# stack= [1 2]
# stack=[1 3]
# stack[1 4]

def jump_game(nums):
    stack= [0]
    n=len(nums)
    visited=set()
    
    while stack:
        i= stack.pop()
        if i == n-1:
            return True
        if i in visited:
            continue
        visited.add(i)

        for step in range(1, nums[i] + 1):
            next_idx= nums[i] + step
            stack.append(next_idx)
            if next_idx<n:
                stack.append(next_idx)
        
    return False

if __name__== "__main__":
    nums=[2,3,1,1,4]
    print(jump_game(nums))





