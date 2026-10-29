#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
Input: nums = [1,2,3,1]
Output: true
Explanation:
    The element 1 occurs at the indices 0 and 3
"""

def contain_duplicate(nums):
    my_dict = {}
    for item in nums:
        if item in my_dict:
            return True
        my_dict[item] = True
    return False
nums = [1,2,3,4]
res = contain_duplicate(nums)
print('➡ List/Contain_duplicate.py:16 res:', res)
