"""
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
Explanation:
    The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
    def twoSum(self,nums,target):
        print("first method call")
        points = {}
        for key, val in enumerate(nums):
            dif = target - val
            if dif in points:
                return [points[dif]+1,key+1]
            points[val] = key
        return []

    def twoSum_(self, numbers: list[int], target: int) -> list[int]:
        print("second method call")
        records = {}
        for idx, val in enumerate(numbers):
            if numbers[idx] + numbers[-1] < target:
                continue
            comp = target - val
            if comp in records:
                return [records[comp] + 1, idx + 1]
            elif val in records:
                continue
            records[val] = idx
        else:
            return []

nums = [2,7,11,15]
target = 17
obj1 = Solution()
print(obj1.twoSum(nums, target))
print(obj1.twoSum_(nums, target))
