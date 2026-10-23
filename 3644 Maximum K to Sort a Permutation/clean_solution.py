class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        res = -1

        for i, n in enumerate(nums):
            if i != n:
                res = res & n
        return max(res, 0)
