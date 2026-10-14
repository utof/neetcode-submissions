class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        if len(slist) > len(tlist):
            return False
        if not s:
            return True
        i = 0
        while i < len(tlist):
            if tlist[i] == slist[0]:
                subsec_index = 0 
                ko = 0 
                while subsec_index < len(slist) and subsec_index+i+ko < len(tlist):
                    t_at_curr_pos = tlist[subsec_index+i+ko]
                    s_at_curr_pos = slist[subsec_index]
                    if t_at_curr_pos == s_at_curr_pos:
                        subsec_index +=1
                    else:
                        ko+=1
                if subsec_index == len(slist):
                    return True
                
                return False
            i+=1
        return False