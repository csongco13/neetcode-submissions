class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = {}
        for s in strs:
            sort_char = ''.join(sorted(s))
            if sort_char in new:
                new[sort_char].append(s)
            else:
                new[sort_char]=[s]
        return list(new.values())

        