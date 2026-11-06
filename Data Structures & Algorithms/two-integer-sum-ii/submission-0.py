class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem asks for 1-indexed indices
                return [left + 1, right + 1]
            elif current_sum < target:
                # We need a larger sum, move left pointer right
                left += 1
            else:
                # We need a smaller sum, move right pointer left
                right -= 1
                
        return [] # This line won't be reached based on constraints