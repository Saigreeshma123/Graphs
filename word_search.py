class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n=len(board[0])
        l = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if len(word) > m * n:
            return False
        def search(path, word):
            if not word:
                return True
            for i in l:
                x, y = path[-1]
                x, y = x + i[0], y + i[1]
                if 0 <= x < m and 0 <= y < n and (x, y) not in path and board[x][y] == word[0]:
                    if search(path + [(x, y)], word[1:]):
                        return True
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    path = [(i, j)]
                    if search(path, word[1:]):
                        return True
        return False      