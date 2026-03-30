class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if i in memo:
                return memo[i]
            memo[i] = helper(i + 1) + helper(i + 2)

            return memo[i]
        
        return helper(0)
        