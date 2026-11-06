class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Clean up the string. 
        # We only keep letters and numbers, and make everything lowercase.
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()
                
        # Step 2: Check if it's a palindrome using two pointers.
        left = 0
        right = len(clean_s) - 1
        
        while left < right:
            # If the characters don't match, it's not a palindrome
            if clean_s[left] != clean_s[right]:
                return False
            
            # Move the pointers closer to the middle
            left += 1
            right -= 1
            
        # If we made it through the whole loop without mismatches, it's a palindrome!
        return True