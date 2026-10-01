class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPali(inp_str):
            
            formatted_input = "".join(filter(str.isalpha, s.lower()))
            left = 0 
            right = len(formatted_input) - 1
            while left < right:
                if formatted_input[left] != formatted_input[right]:
                    return False
                left += 1
                right -= 1
            return True
        return isPali(s)