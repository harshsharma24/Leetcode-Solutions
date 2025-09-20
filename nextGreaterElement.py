class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # Brute Force
        # res=[]

        # for i in range(len(nums1)):
        #     flag=False
        #     greaterNum=-1
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             flag=True
        #         elif nums1[i] < nums2[j] and flag:
        #             greaterNum=nums2[j]
        #             break
            
        #     res.append(greaterNum)

        # return res

        #Optimised using Stack
        stack=[]
        next_greater= {}
        res=[]

        for num in nums2:
            while stack and num > stack[-1]:
                prev_idx= stack.pop()
                next_greater[prev_idx]= num

            stack.append(num)
        
        for num in stack:
            next_greater[num]= -1
        
        for num in nums1:
            r=next_greater[num]
            res.append(r)
        
        return res 

s=Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
# [-1,3,-1]
print(s.nextGreaterElement(nums1,nums2))