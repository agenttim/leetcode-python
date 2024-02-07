from typing import List


class Solution:
    nums = [3, 2, 4]
    target = 6

    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

    print(twoSum(nums, target))

    # i=0 h={} c=6-3=3
    # i=1 h={3:0} c=6-2=4
    # i=2 h={3:0, 2:1} c=6-4=2 if true 2, 1
