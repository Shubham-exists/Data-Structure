class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        var = 0
        
        for i in range(1,n):
            if nums[i] < nums[i -1]:
                var += 1
        if nums[0] < nums[n - 1]:
            var += 1
        
        return var <= 1
# different approach 
      
        s = sorted(nums)
        n = len(nums)
        for i in range(n):
            cs= []
            for i in range( i ,n):
                cs.append(nums[i])
            for i in range(i):
                cs.append(nums[i])
            if cs == s:
                return  True
        return False 



