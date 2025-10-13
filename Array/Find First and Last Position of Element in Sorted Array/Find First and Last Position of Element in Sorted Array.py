class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f = -1
        l = -1
        srt = 0
        end = len(nums) -1

        #for first 
        while srt <= end:
            mid = int(srt + (end - srt)/2)
            
            if target == nums[mid]:
                f = mid
                end = mid -1
            elif target > nums[mid]:
                srt = mid + 1
            else:
                end = mid - 1

        # for sencond
        srt = 0
        end = len(nums) -1
        
        while srt <= end:
            mid = int(srt + (end - srt)/2)

            if target == nums[mid]:
                l = mid
                srt = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                srt = mid + 1

        return [ f, l]

  
