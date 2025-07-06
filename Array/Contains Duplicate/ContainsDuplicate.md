# Contains Duplicate

**Problem Link**: [LeetCode - Contains Duplicate](https://leetcode.com/problems/contains-duplicate)

## Problem Statement

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Example

Input: nums = [1,2,3,1]
Output: true

## Approach
- **1. Brute Force:**  
The simplest but inefficient way is to compare each element with all the other elements in the array. This would give a time complexity of O(n²).<br>  
- **Time Complexity**: O(n²) —> Due to the nested loop.<br>  
- **Space Complexity**: O(1) —> No extra space used.

- **2. Using a Set:**  
This approach is optimal and involves using a hash set to keep track of elements we have already seen. As we iterate through the array, we check if the current element is in the set.<br>  
- **Time Complexity**: O(n) —> Each lookup and insertion in a hash set takes O(1) time on average.<br>  
- **Space Complexity**: O(n) —> A set is used to store unique elements.


## Time & Space Complexity

- Time: O(n)
- Space: O(n)
