"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation:
    The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.
"""
#broute force approaches
class Solution:
    def two_sum(self,nums,t):
        n = len(nums) #4
        print('➡ List/Two_Sum1.py:11 n:', n)
        for i in range(n):  # 0 , 1 , 2 , 3
            for j in range(i+1,n): #1, 2 , 3
                if nums[i] + nums[j] == t:
                    return [i,j]
        return []


    def two_sum_opt(self,nums,t):
        point = {}
        for key,item in enumerate(nums):
            des = t - item
            if des in point:
                print(point)
                return [point[des],key]
            point[item] = key
        return []

nums = [2,7,11,15]
target = 17
obj1 = Solution()
print(obj1.two_sum(nums, target)) #(O(n^2))
print(obj1.two_sum_opt(nums, target)) #Time complexity: (O(n))
