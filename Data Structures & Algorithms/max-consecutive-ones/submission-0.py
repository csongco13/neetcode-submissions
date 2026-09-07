class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_streak = 0 
        max_streak = 0
        for i in nums:
            if i == 1:
                curr_streak +=1
                max_streak = max(max_streak,curr_streak)
            elif i == 0:
                curr_streak = 0
        return max_streak
        


            
            
        