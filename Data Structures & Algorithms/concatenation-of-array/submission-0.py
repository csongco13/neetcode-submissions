class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.copy()
        ans= nums + nums.copy()
        return ans

        