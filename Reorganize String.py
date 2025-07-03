from collections import Counter
class Solution:
    def reorganizeString(self,s):

        prev=None
        res=[]
        count= Counter(s)
        print(count)
        
        while count:    
            maxValue=0
            maxKey=None
            for key,value in count.items():
                if value>maxValue and key != prev:
                    maxValue=value
                    maxKey=key
            
            if maxKey is None:
                return ""

            if count[key]>0:
                res.append(maxKey)
                prev=maxKey
                count[maxKey]-= 1

                
            if count[maxKey] == 0:
                del count[maxKey]

        print(res)
        return "".join(res)
    

if __name__== "__main__":
    s=Solution()
    s1= "abaa"
    print(s.reorganizeString(s1))

