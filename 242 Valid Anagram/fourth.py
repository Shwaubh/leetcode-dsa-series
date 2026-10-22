class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        data1, data2 = defaultdict(int), defaultdict(int)
        for i, j in zip(s, t):
            data1[i] += 1
            data2[j] += 1

        return data1 == data2
