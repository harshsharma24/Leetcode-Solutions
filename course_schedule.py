class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap={}
        for i in range(numCourses):
            preMap[i]=[]
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        print(preMap)
    
        visitSet=set()
        def dfs(crs):
            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)

            for pre in preMap[crs]:
                result= dfs(pre) 
                if result == False:
                    return False
            
            visitSet.remove(crs)
            preMap[crs]= []  
            return True  
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


if __name__=="__main__":
    solution = Solution()
    
    # Test case 2: Cannot finish - has cycle
    numCourses2 = 5
    prerequisites2 = [[1, 0], [0, 2], [1, 3], [1, 4],[3,4]]  # Course 1 needs 0, Course 0 needs 1 (cycle!)
    result2 = solution.canFinish(numCourses2, prerequisites2)
    print(f"\nTest 2: {numCourses2} courses, prereqs {prerequisites2}")
    print(f"Can finish: {result2}")