class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numSet=set(nums)
        for i in numSet:
            if i-1 not in numSet:
                curr_length=1
                num=i
                while num+1 in numSet:
                    num+=1
                    curr_length+=1
                longest=max(longest,curr_length)
        return longest

        