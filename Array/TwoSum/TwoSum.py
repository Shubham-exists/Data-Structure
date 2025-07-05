class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            num=nums[i]
            y=target-num
            if y in d:
                return [d[y],i]
            d[num]=i

        return []
