class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                i = board[r][c]
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r // 3, c // 3]):
                    return False
                rows[r].add(i)
                cols[c].add(i)
                squares[r // 3, c // 3].add(i)
        return True