class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            string = ''.join(sorted(s))
            if string not in anagram_map:
                anagram_map[string] =  [s]
            else:
                anagram_map[string].append(s)
        
        return [anagram_map[key] for key in anagram_map]
