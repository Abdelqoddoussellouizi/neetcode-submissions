class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Only start counting if this number is the beginning of a sequence
            # (i.e., the number before it is NOT in the set)
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Keep checking for the next consecutive numbers
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # Update the max streak found so far
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak