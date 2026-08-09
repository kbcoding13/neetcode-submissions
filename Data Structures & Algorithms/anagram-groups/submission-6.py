class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            string = ''.join(sorted(s))
            if string not in map:
                map[string] = [s]
            else:
                map[string].append(s)
        
        return [map[key] for key in map]