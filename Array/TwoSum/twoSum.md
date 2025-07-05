# Two Sum

**Problem Link**: [LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

## Example

Input: nums = [2,7,11,15], target = 9  
Output: [0,1]

## Approach

- Use a hash map to store the complement.
- Iterate through the array and check if the complement is already in the map.

## Time & Space Complexity

- Time: O(n)
- Space: O(n)
