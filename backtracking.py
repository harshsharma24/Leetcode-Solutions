
def subsets(nums):
    
    subset=[]
    res=[]
    def dfs(i):
        if i>=len(nums):
            res.append(subset.copy)
            return
        
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)

        # decision to not include nums[i]
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res
        
if __name__ == "__main__":
    arr = [1, 2, 3]
    res = subsets(arr)

    