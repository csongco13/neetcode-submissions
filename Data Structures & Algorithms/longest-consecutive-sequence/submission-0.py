class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        res =0

        for i in nums:
            seen.add(i)

        for i in nums:
            if i in seen and (i-1) not in seen:
                curr = i 
                count = 0 
                while curr in seen:
                    curr +=1
                    count +=1
                res = max(res,count)
        return res
        