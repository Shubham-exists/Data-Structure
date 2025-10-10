# 🧩 K-th Symbol in Grammar (LeetCode 779)

## 🧠 Problem Description

We are given two integers **n** and **k**, representing the row and the position (1-indexed) in a grammar sequence.

The grammar sequence is built using these rules:

- Row 1: `0`
- To generate the next row:
  - Replace every **0** with **01**
  - Replace every **1** with **10**

We need to **return the k-th symbol in the n-th row**.

---

## 🧾 Example Pattern

| Row | Grammar |
|-----|----------|
| 1 | 0 |
| 2 | 01 |
| 3 | 0110 |
| 4 | 01101001 |
| 5 | 0110100110010110 |

---

## 🧩 Recursive Approach (Conceptual)

The naive recursive approach is based on how each row is formed from the previous one.
as we have done in the code in the .py file 
