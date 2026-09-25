class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        if not lens == lent:
            return False
        def count(a):
            dic = {}
            for i in a:
                dic[i] = dic.get(i, 0) + 1
            return dic
        return count(s) == count(t)
        