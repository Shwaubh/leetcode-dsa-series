class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        data = [ 0 ] * 26

        for i, j in zip(s, t):
            data[ ord(i) - 97 ] += 1
            data[ ord(j) - 97 ] -= 1

        for d in data:
            if d!=0:
                return False
        
        return True
