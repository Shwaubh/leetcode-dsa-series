class Solution:
    def minOperations(self, s: str) -> int:
        if self.isSorted(s):
            return 0
        if len(s) == 2 and not self.isSorted(s):
            return -1
        mx = max(s)
        mn = min(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        
        if mn not in s[:-1] and mx not in s[1:-1]:
            return 3
        
        return 2
    
    def isSorted(self, s) -> bool:
        init = s[0]
        for c in s[1:]:
            if c < init:
                return False
            init = c

        return True
