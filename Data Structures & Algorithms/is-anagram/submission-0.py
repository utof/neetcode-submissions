class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        if not lens == lent:
            return False
        dic_s = {}
        dic_t = {}
        for i in range(lens):
            dic_s[i] += 1
            dic_t[i] += 1
        for i in dic_s.items:
            print(i)
        