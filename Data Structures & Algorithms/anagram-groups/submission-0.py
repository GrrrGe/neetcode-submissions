class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams_dict = defaultdict(list)
        for s in strs:
            grouped_anagrams_dict["".join(sorted(s))].append(s)
        grouped_anagrams = []
        for values in grouped_anagrams_dict.values():
            grouped_anagrams.append(values)
        return grouped_anagrams


        