class Solution:
    def encode(self, strs: List[str]) -> str:
        returned_str = ""
        for strin in strs:
            str_mod = str(len(strin)) + "," + strin
            returned_str += str_mod
        return returned_str

    def decode(self, s: str) -> List[str]:
        final_array = []
        index = 0
        while index < len(s):
            str_len_arr = []
            while s[index] != ',':
                str_len_arr.append(s[index])
                index += 1
                continue
            str_len = int("".join(str_len_arr))
            final_array.append(s[index + 1 : index + str_len + 1])
            index += str_len + 1
        return final_array
