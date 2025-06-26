class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hmap:
                return [hmap[diff],i]
            else:
                hmap[nums[i]]=i
        