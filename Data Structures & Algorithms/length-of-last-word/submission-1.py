class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        if s[i] == " ":
            while s[i] == " ":
                i -= 1
        while s[i] != " " and i >= 0:
            count+=1
            i-=1
        return count