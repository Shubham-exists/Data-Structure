# Concatenation of Array

**Problem Link**: [LeetCode - Concatenation of Array](https://leetcode.com/problems/concatenation-of-array)

## Problem Statement

Given an integer array `nums`, return an array `ans` of length `2n` such that:

- `ans[i] = nums[i]` for `0 <= i < n`
- `ans[i] = nums[i - n]` for `n <= i < 2n`

In short, the new array is the concatenation of `nums` with itself.

## Example

Input: nums = [1, 2, 1]  
Output: [1, 2, 1, 1, 2, 1]

## Approach

- **1. Brute Force (Simple Append):**  
  Create a new array and add all elements of `nums` twice using a loop.  
  - **Time Complexity**: O(n)  
  - **Space Complexity**: O(n)

- **2. Preallocate and Fill (Optimized):**  
   Buy using [ ] + [ ]
  - **Time Complexity**: O(n)  
  - **Space Complexity**: O(n)

## Time & Space Complexity

- Time: O(n)  
- Space: O(n)

