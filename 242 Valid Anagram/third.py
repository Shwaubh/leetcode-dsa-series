class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        data1, data2 = dict(), dict()
        for i, j in zip(s, t):
            if i in data1:
                data1[i] += 1
            else:
                data1[i] = 1
            if j in data2:
                data2[j] += 1
            else:
                data2[j] = 1


        return data1 == data2
