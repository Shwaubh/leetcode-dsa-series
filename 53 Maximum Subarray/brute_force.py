class Solution:
    def maxSubArray(self, nums):
        maxN = max(nums)
        if maxN < 0:
            return maxN
            
        res = 0
        n = len(nums)

        for i in range(n):
            temp = 0
            for j in range(i, n):
                temp = temp + nums[j]
                res = max(res, temp)
        
        return res