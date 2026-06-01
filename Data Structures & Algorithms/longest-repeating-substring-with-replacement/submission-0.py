class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_count = defaultdict(int)
        longest = 0
        for r in range(len(s)):
            char_count[s[r]]+=1
            while l<=r and (((r-l)+1 - max(char_count.values())) > k):
                char_count[s[l]]-=1
                l+=1
            longest = max(longest, r-l+1)
        return longest
