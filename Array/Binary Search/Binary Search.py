class Solution:
    def search(self, nums: List[int], target: int) -> int:
        srt = 0
        end = len(nums) -1
        while srt <= end:
            
            mid = int(srt + (end - srt)/2)

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                srt = mid + 1
        return -1
