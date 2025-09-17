
class solution:
    def threesum(self, nums):
        # Brute Force

        # final_arr=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0 and i!= j and j!=k and k!= i:
        #                 final_arr.add(tuple(sorted([nums[i],nums[j], nums[k]])))
        # return [list(t) for t in final_arr]

        # Optimal Solution

        res=[]
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue

            l,r= i+1, len(nums)-1
            while l<r:
                threesum= a+ nums[l] + nums[r]
                if threesum>0:
                    l+=1
                elif threesum<0:
                    r-=1
                else:
                    res.append([a.nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] ==nums[l-1]:
                        l+=1
        return res


s= solution()
arr= [-1,0,1,2,-1,-4]
print(s.threesum(arr))