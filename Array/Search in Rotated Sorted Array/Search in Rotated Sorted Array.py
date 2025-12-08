class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(arr,start,end,target):
            while start <= end:
                mid = (start + end) // 2

                if arr[mid] == target:
                    return mid
                elif target < arr[mid] :
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        def pivit(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return i
            return 0
        Pivit = pivit(nums)

        arr1 = nums[:Pivit + 1]
        arr2 = nums[Pivit + 1:]

        val1 = BS(arr1, 0, len(arr1) - 1, target)
        val2 = BS(arr2, 0, len(arr2) - 1, target)

        if val1 != -1:
            return val1
        elif val2 != -1:
            return (Pivit + 1) + val2
        elif val1 == val2 == -1:
            return -1


