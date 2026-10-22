class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if self.isSorted(nums):
            return 0
        
        if not self.possible(nums):
            return -1

        n = len(nums)
        last = nums.index(n-1)
        return min(last + 1, n - last + 1)      


    def possible(self, nums) -> bool:
        n = len(nums)
        for i in range(1, n):
            diff = abs(nums[i] - nums[i-1])
            if diff != 1 and diff != n-1:
                return False
       
        return True   


    def isSorted(self, nums) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True
