# 📅 Day 39: Search in a Row-wise Sorted Matrix
## 🔍 Problem Statement:
Given a row-wise sorted 2D matrix mat[][] of size n x m and an integer x, the task is to check whether x exists in the matrix.

A row-wise sorted matrix means each row is individually sorted in increasing order.

## 🧠 Approach:
- ✅ Iterate through each row

- ✅ For every row, check if the element x could lie between the first and last element

- ✅ If yes, apply Binary Search on that row to search for x

- ✅ If found, return True; else continue checking next row

## 💡 Why This Works:
- We leverage the fact that each row is sorted. So we can:

- Skip rows where x cannot exist (optimization)

- Use Binary Search for fast lookup within a row (O(log m))

## 🔁 Algorithm:
1. Loop over each row

2. If x is between the first and last element of the row:

- Apply Binary Search in that row

3. If x is found, return True

4. If not found in any row, return False

## 📊 Complexity:
- Time: O(n × log m)

- Space: O(1)

## 🧠 Key Concepts:
- Binary Search

- Matrix Traversal

- Conditional optimization



