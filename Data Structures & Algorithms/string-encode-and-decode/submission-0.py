class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Add the length of the string, a '#' delimiter, and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Read the number (length) until we hit the '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the integer length
            length = int(s[i:j])
            
            # Move 'i' to the start of the actual string
            i = j + 1
            
            # Extract the string based on the length
            word = s[i : i + length]
            res.append(word)
            
            # Move 'i' past the current word to the start of the next length
            i += length
            
        return res