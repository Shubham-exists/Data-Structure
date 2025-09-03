# Find Closest Number to Zero

**Problem Link**: [LeetCode - Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero)

## Problem Statement

Given an integer array `nums` of size `n`, return the number with the value closest to `0` in `nums`.  
If there are multiple answers (e.g., `-x` and `x`), return the positive one.

---

## Example

Input: nums = [-4, -2, 1, 4, 8]  
Output: 1  

Input: nums = [2, -2]  
Output: 2  

Input: nums = [0, 5, -7]  
Output: 0  

---

## Approach

- **1. Brute Force (Sort + Compare):**  
  Sort the array by absolute value, then return the element with smallest absolute distance to zero.  
  If there’s a tie, return the positive one.  
  - **Time Complexity**: O(n log n)  
  - **Space Complexity**: O(1)  

- **2. One-Pass Scan (Optimized):**  
  Track a variable `best`. For each number `x`:  
  - If `abs(x) < abs(best)`, update `best = x`.  
  - If `abs(x) == abs(best)`, pick the **positive** one (`best = max(best, x)`).  
  - Return `best` at the end.  
  - **Time Complexity**: O(n)  
  - **Space Complexity**: O(1)  

---

## Time & Space Complexity

- Time: O(n) (Optimized approach)  
- Space: O(1)  
