from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Use sets to keep track of seen numbers
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Calculate which 3x3 box we are in (0 to 8)
                box_id = (r // 3) * 3 + (c // 3)
                
                # If we've already seen this number in the row, col, or box, it's invalid
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_id]):
                    return False
                
                # Add the number to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)
                
        return True