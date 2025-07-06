class Solution():
    def checkSubarraySum(self,nums,target):
        sum=0
        i,j = 0 ,0
        while j < len(nums):
            sum= nums[j]

            if sum>target:
                i+=1
                j=i

            elif sum< target:
                j+=1
            
            elif sum == target:
                return True

        return False
            
if __name__ =="__main__":
    s=Solution()
    nums=[23,2,4,6,7]
    target=6
    print(s.checkSubarraySum(nums,target))

        