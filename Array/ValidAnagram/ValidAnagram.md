# Valid Anagram

## Problem Link
[LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.


Example
nput: s = "anagram", t = "nagaram"
Output: true

## Approach
This method counts the characters in string s, then subtracts the counts while iterating through string t. If any character in t doesn't match the expected count, it's not an anagram.


##Time & Space Complexity
- Time: O(n)
- Space: O(1)
