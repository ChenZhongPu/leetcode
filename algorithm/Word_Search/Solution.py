class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) <= 0 or len(word) <=0:
            return false;
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.DFS(i, j, 1, board, word):
                        return True
        return False

    def DFS(self, i, j, idx, board, word):
        if idx == len(word):
            return True
        c = board[i][j]
        board[i][j] = '#'
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for d in direction:
            x = d[0] + i
            y = d[1] + j
            if x >= 0 and y >= 0 and x < len(board) and y < len(board[0]) and board[x][y] == word[idx]:
                if self.DFS(x, y, idx + 1, board, word):
                    return True
        board[i][j] = c
        return  False
