class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # Initialize the output array with 1s
        output = [1] * n
        
        # 1. Left Pass: Calculate prefix products
        # output[i] will contain the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
            
        # 2. Right Pass: Calculate suffix products and multiply
        # We use a running 'suffix' variable to avoid creating a second array
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output