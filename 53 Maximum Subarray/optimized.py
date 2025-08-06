class Solution:
    def maxSubArray(self, nums):
        maxN = max(nums)
        if maxN < 0:
            return maxN

        res, curr = 0, 0
        for n in nums:
            if curr + n > 0:
                curr = curr + n
            else:
                curr = 0
            res = max(res, curr)

        return res