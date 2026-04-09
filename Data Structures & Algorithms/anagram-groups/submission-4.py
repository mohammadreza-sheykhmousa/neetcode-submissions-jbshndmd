class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sig = ''.join(sorted(s))

            anagram_map[sig].append(s)
        return list(anagram_map.values())