class Solution :
    def twoSum (self, nums , target):
        seen = {}

        for i , num in enumerate (nums):
            missing_piece = target - num

            if missing_piece in seen :
                return [seen[missing_piece], i]

            seen[num] = i

