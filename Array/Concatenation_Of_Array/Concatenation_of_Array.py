class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums.copy()            
        for i in range(len(nums)):      # brute force 
            ans.append(nums[i])
        return ans

      ---------------------------------------
        return nums+nums      # fast code
