class Solution:
    def dailyTemperatures(self, temperatures):
        # res=[]
        # for i in range(len(temperatures)):
        #     count=0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             count= j-i
        #             res.append(count)
        #             break
        #     res.append(count)
        # return res

        res=[0] * len(temperatures)
        stack=[]
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]] :
                prev_idx= stack.pop()
                res[prev_idx] = i- prev_idx
            stack.append(i)
        return res
                


solution=Solution()
print(solution.dailyTemperatures([30,38,30,36,35,40,28]))
        
                