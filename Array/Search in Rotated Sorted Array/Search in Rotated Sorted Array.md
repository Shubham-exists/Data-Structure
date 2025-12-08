# Search in Rotated Sorted Array

**Problem Link**: [LeetCode - Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)

## Problem Statement

There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

## Example

Input: nums = [4,5,6,7,0,1,2], target = 0  
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3  
Output: -1

## Approach
- **1. Linear Search:**  
The simplest way is to iterate through the entire array and check if the target matches any element. This is straightforward but inefficient for large arrays.<br>  
- **Time Complexity**: O(n) —> We traverse the array once.<br>  
- **Space Complexity**: O(1) —> No extra space used.

- **2. Modified Binary Search:**  
Since the array is rotated but originally sorted, we can use binary search with modifications. We compare the middle element with the target and decide which half to search based on the sorted portions. If the left half is sorted, check if target is in that range; otherwise, search the right half.<br>  
- **Time Complexity**: O(log n) —> Binary search reduces the search space by half each time.<br>  
- **Space Complexity**: O(1) —> No extra space used.

## Time & Space Complexity

- Time: O(log n)
- Space: O(1)
