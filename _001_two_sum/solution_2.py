from typing import List


class Solution:
    nums = [3, 2, 4]
    target = 6

    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    print(twoSum(nums, target))
