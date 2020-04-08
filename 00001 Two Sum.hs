-- Given an array of integers, return indices of the two numbers such that they add up to a specific target.
-- You may assume that each input would have exactly one solution, and you may not use the same element twice.
-- Example:
--    Given nums = [2, 7, 11, 15], target = 9,
--    Because nums[0] + nums[1] = 2 + 7 = 9,
--    return [0, 1].
-- 
-- FROM: https://leetcode.com/problems/two-sum/

twoSum :: [Integer] -> Integer -> [Integer]
twoSum (x:xt) t
        | elem y xt = [0, ((index y xt)+1)]
        | otherwise = listPlus (twoSum xt t) [1, 1]
        where y = t - x

index :: Integer -> [Integer] -> Integer
index y (x:xt)
        | y == x    = 0
        | otherwise = 1 + index y xt

listPlus :: [Integer] -> [Integer] -> [Integer]
listPlus [x] [y] = [ (x+y) ]
listPlus (x:xt) (y:yt) = [ (x+y) ] ++ listPlus xt yt