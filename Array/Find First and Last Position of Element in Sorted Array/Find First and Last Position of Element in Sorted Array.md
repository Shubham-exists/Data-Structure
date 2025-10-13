# Find First and Last Position of Element in Sorted Array

**Problem Link**: [LeetCode - Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)

## Problem Statement

Given an array of integers `nums` sorted in non-decreasing order, and an integer `target`,  
find the **starting** and **ending** position of the given `target` value.

If the `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Example

Input: nums = [5, 7, 7, 8, 8, 10], target = 8  
Output: [3, 4]

Input: nums = [5, 7, 7, 8, 8, 10], target = 6  
Output: [-1, -1]

Input: nums = [], target = 0  
Output: [-1, -1]

---

## Approach

- **1. Binary Search for the First Occurrence:**  
  Use binary search to find the **first index** where `target` appears.  
  If `nums[mid] == target`, move the `end` pointer to `mid - 1` to continue searching in the left half.

- **2. Binary Search for the Last Occurrence:**  
  Use binary search again to find the **last index** where `target` appears.  
  If `nums[mid] == target`, move the `start` pointer to `mid + 1` to continue searching in the right half.

Both searches ensure the overall time complexity remains **O(log n)**.

---

## Time & Space Complexity

- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)
