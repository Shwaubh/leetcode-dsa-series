from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            temp = [0]*26
            for c in s:
                temp[ord(c)-97] += 1
            temp = tuple(temp)
            res[temp].append(s)
        return list(res.values())