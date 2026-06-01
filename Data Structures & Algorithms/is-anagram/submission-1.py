class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char,0) + 1
        for char in t:
            char_count[char] = char_count.get(char,0) - 1
        for k,v in char_count.items():
            if v != 0:
                return False
        return True

        