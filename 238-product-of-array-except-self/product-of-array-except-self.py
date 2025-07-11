class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array=[1]*len(nums)
        right_array=[1]*len(nums)
        output=[1]*len(nums)

        for i in range(1, len(nums)):
            left_array[i]=nums[i-1]*left_array[i-1]
        
        print(left_array)

        for i in range(len(nums)-2,-1,-1):
            right_array[i]=nums[i+1]*right_array[i+1]
        print(right_array)

        for i in range(len(nums)):
            output[i]=right_array[i]*left_array[i]
        return output
