# Group Anagrams

**Problem Link**: [LeetCode - Group Anagrams](https://leetcode.com/problems/group-anagrams)

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

Two strings are anagrams if they contain the **same characters**, just rearranged (e.g., `"eat"` and `"tea"` are anagrams).

## Example

Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`  
Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`

## Approach

- **1. Brute Force:**  
  Compare every pair of words to check if they are anagrams. Group them accordingly. This is inefficient for large inputs.  
  - **Time Complexity**: O(n² * k log k), where `n` is the number of strings and `k` is the average string length.  
  - **Space Complexity**: O(n)

- **2. Sorting-Based Hashing (Optimal):**  
  Use a dictionary (hashmap) where the key is the **sorted version** of the word, and the value is a list of anagrams.  
  - For example, `"eat"`, `"tea"`, and `"ate"` all become `"aet"` when sorted.  
  - **Time Complexity**: O(n * k log k)  
    - Sorting each string takes O(k log k), done for all `n` strings.  
  - **Space Complexity**: O(n * k)  
    - Extra space for storing grouped anagrams.

## Time & Space Complexity

- **Time**: O(n * k log k)  
- **Space**: O(n * k)

