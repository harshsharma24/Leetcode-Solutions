class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

def main():
    solution = Solution()
    
    # Test a few values
    print(solution.climbStairs(5))

if __name__ == "__main__":
    main()