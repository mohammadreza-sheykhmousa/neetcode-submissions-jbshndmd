class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            freq = ''.join(sorted(s))
            anagram_map[freq].append(s)
        return list(anagram_map.values())

        