class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == curr:
                    return True
        
        return False