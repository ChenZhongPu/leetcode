public class Solution {
    public boolean exist(char[][] board, String word) {
      if (board.length <= 0 || word.length() <= 0) return false;
      for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[0].length; j++) {
          if (board[i][j] == word.charAt(0)) {
            if (DFS(i, j, 0, board, word)) return true;
          }
        }
      }
      return false;
    }

    public boolean DFS(int i, int j, int idx, char[][] board, String word) {
      if (idx == word.length()) return true;
      if (i < 0 || j < 0 || i >= board.length || j >= board[0].length) return false;
      if (board[i][j] != word.charAt(idx)) return false;
      char c = board[i][j];
      board[i][j] = '#';
      boolean exist = DFS(i - 1, j, idx + 1, board, word) ||
        DFS(i + 1, j, idx + 1, board, word) ||
        DFS(i, j - 1, idx + 1, board, word) ||
        DFS(i, j + 1, idx + 1, board, word);

      board[i][j] = c;
      return exist;
    }
}
