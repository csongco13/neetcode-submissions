class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_char1 = ''.join(sorted(s))
        sort_char2 = ''.join(sorted(t))

        return sort_char1 == sort_char2
        