from collections import Counter
class Solution(object):
    # O(k.n) solution
    # def topKFrequent(self, nums, k):
    #     count_map= Counter(nums)
    #     print(count_map)
 
    #     res=[]

    #     maxValue=0
    #     maxKey=None

    #     for _ in range(k):
    #         maxValue=0
    #         maxKey=None

    #         for key,value in count_map.items():
    #             if value>maxValue:
    #                 maxValue=value
    #                 maxKey=key
                
    #         print(maxKey) 
    #         res.append(maxKey)
    #         del count_map[maxKey]

    #         print(count_map)
    #     print(res)
    #     return res

    def topKFrequent(self, nums, k):
        bucket=[[] for _ in range(len(nums)+1)]
        count={}
        res=[]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for key,value in count.items():
            bucket[value].append(key)
        

        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    print(res)
                    return res
                    

if __name__=="__main__":
    nums= [1]
    k=1
    s=Solution()
    s.topKFrequent(nums,k)