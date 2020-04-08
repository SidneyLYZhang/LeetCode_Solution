# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
#    Given nums = [2, 7, 11, 15], target = 9,
#    Because nums[0] + nums[1] = 2 + 7 = 9,
#    return [0, 1].
# 
# FROM: https://leetcode.com/problems/two-sum/

def twoSum(nums: list, target: int) -> list :
    for x in nums :
        if (y := (target - x)) in nums :
            if x == y and nums.count(y) == 1 :
                continue
            else :
                result = [nums.index(x),nums.index(y)]
                result.sort()
                break
    return result