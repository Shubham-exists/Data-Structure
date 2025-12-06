# Check if Array Is Sorted and Rotated

**Problem Link**: [LeetCode - Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated)

## Problem Statement

Given an array of integers `nums`, return `true` if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return `false`.

A rotation means moving elements from the end to the front. For example:
- Original: [1, 2, 3, 4, 5]
- Rotated: [3, 4, 5, 1, 2]

### Constraints
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`

## Example

Input: nums = [3, 4, 5, 1, 2]  
Output: true

Explanation: The array is a rotation of the sorted array [1, 2, 3, 4, 5].

## Approach

- **1. Single Pass Check:**  
  Iterate through the array and count the number of times a number is greater than the next (wrapping around). If there is more than one such violation, return false.  
  - **Time Complexity**: O(n)  
  - **Space Complexity**: O(1)

## Time & Space Complexity

- Time: O(n)  
- Space: O(1)
