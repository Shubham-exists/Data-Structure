#my solution:

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for i in nums:
            if abs(i)< abs(closest) or (abs(i) == abs(closest) and i>closest):
                closest = i
        return closest


# other solutions:

#1. fastest one:
    def findClosestNumber(self, nums: List[int]) -> int:
        

        closest = nums[0]

        for x in nums :
            if abs(x) < abs(closest):
                closest = x 

        
        if closest < 0 and abs(closest) in nums :
            return abs(closest)
        
        else :
            return closest


