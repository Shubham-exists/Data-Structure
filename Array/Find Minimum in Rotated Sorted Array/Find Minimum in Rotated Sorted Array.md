# Find Minimum in Rotated Sorted Array

## Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

### Examples

- **Input:** `nums = [3,4,5,1,2]`  
  **Output:** `1`  
  **Explanation:** The original array was `[1,2,3,4,5]` rotated 3 times.

- **Input:** `nums = [4,5,6,7,0,1,2]`  
  **Output:** `0`  
  **Explanation:** The original array was `[0,1,2,4,5,6,7]` rotated 4 times.

- **Input:** `nums = [11,13,15,17]`  
  **Output:** `11`  
  **Explanation:** The original array was already sorted, so the minimum is `nums[0]`.

### Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique.
- `nums` is sorted and rotated between 1 and n times.

## Approach

This is a classic problem that can be solved using a modified binary search. The key insight is that in a rotated sorted array, the minimum element is the point where the array "breaks" – i.e., where the sequence decreases.

We can use binary search to find the pivot point:

1. Initialize `left = 0` and `right = len(nums) - 1`.
2. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] > nums[right]`, the minimum is in the right half, so set `left = mid + 1`.
   - Otherwise, the minimum is in the left half (including mid), so set `right = mid`.
3. When the loop ends, `left` (or `right`) will point to the minimum element.

This works because the array is sorted except for the rotation, so the minimum is where the increasing order breaks.

### Time Complexity
- O(log n) due to binary search.

### Space Complexity
- O(1), as we use only a few variables.



