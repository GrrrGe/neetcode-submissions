class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "❌"
        encoded_str = "😀".join(strs)
        return encoded_str
    
    def decode(self, s: str) -> List[str]:
        if s == "❌":
            return []
        strs = s.split("😀")
        return strs