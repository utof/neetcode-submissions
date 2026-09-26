class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # def count_dict(word):
        #     dic = {}
        #     for i in word:
        #         dic[i] = dic.get(i, 0) + 1
        #     return dic
        
        # def is_anagram(word1, word2):
        #     dic1 = count_dict(word1)
        #     dic2 = count_dict(word2)
        #     return dic1 == dic2
        final_dic = {}
        for i in strs:
            key = "".join(sorted(i))
            final_dic[key] = final_dic.get(key, []) + [i]
        final_arr = []
        for key in final_dic:
            final_arr.append(final_dic[key])
        return final_arr
