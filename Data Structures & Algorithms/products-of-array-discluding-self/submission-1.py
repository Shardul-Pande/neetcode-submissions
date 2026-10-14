class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Initialize result array with 1s

        # First pass: Compute left cumulative product
        l_mult = 1
        for i in range(n):
            result[i] = l_mult  # Store left product in result
            l_mult *= nums[i]  # Update left cumulative product

        # Second pass: Compute right cumulative product and update result
        r_mult = 1
        for i in range(n - 1, -1, -1):  # Traverse right to left
            result[i] *= r_mult  # Multiply with right product
            r_mult *= nums[i]  # Update right cumulative product

        return result  
