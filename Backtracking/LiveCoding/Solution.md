## Generate Parentheses

https://leetcode.com/problems/generate-parentheses/

```
class Solution {
    // Time complexity: O(N*2^(2N))
    // Space complexity: O(N)
    List<String> res = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        dfs(0, n*2, 0, new StringBuilder());
        return res;
    }

    private void dfs(int idx, int len, int openCount, StringBuilder sb) {
        if (idx >= len) {
            res.add(sb.toString());
            return;
        }

        int rem = len - idx;
        // Choose "("
        if (openCount < rem) {
            sb.append("(");
            dfs(idx+1, len, openCount+1, sb);
            sb.deleteCharAt(sb.length() - 1);
        }

        // Choose ")"
        if (openCount > 0) {
            sb.append(')');
            dfs(idx+1, len, openCount-1, sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
```

## Permutations

https://leetcode.com/problems/permutations/

```
class Solution {
    // Time complexity: O(N*N!)
    // Space complexity: O(N)
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        boolean[] vis = new boolean[n];
        dfs(0, n, vis, nums, new ArrayList<>());
        return res;
    }

    private void dfs(int idx, int n, boolean[] vis, int[] nums, List<Integer> lst) {
        if (idx >= n) {
            res.add(new ArrayList<>(lst));
            return;
        }

        for (int i = 0; i < n; ++i) {
            if (vis[i]) {
                continue;
            }

            lst.add(nums[i]);
            vis[i] = true;
            dfs(idx+1, n, vis, nums, lst);
            lst.remove(lst.size() - 1);
            vis[i] = false;
        }
    }
}
```


## Sudoku Solver

https://leetcode.com/problems/sudoku-solver/

```
class Solution {
    // Time complexity: O((9!)*9)
    // Space complexity: O(1)
    public void solveSudoku(char[][] board) {
        dfs(0, 0, board);
    }

    private boolean dfs(int x, int y, char[][] board) {
        if (x >= 9) {
            return true;
        }
        int[] next = chooseNext(x, y);
        int u = next[0];
        int v = next[1];

        if (board[x][y] != '.') {
            return dfs(u, v, board);
        }

        for (int i = 1; i <= 9; ++i) {
            char c = (char)(i + '0');
            if (!isValid(c, x, y, board)) {
                continue;
            }
            board[x][y] = c;
            if (dfs(u, v, board)) {
                return true;
            }
            board[x][y] = '.';
        }
        return false;
    }

    private boolean isValid(char c, int x, int y, char[][] board) {
        // Check numbers in same row and same column
        for (int i = 0; i < 9; ++i) {
            if (board[x][i] == c) {
                return false;
            }
            if (board[i][y] == c) {
                return false;
            }
        }

        // Check numbers in same square
        // column = 8, start column = 6 = (8 / 3) * 3 
        int startX = (x/3) * 3;
        int startY = (y/3) * 3;
        for (int i = startX; i < startX + 3; ++i) {
            for (int j = startY; j < startY + 3; ++j) {
                if (board[i][j] == c) {
                    return false;
                }
            }
        }
        return true;
    }

    private int[] chooseNext(int x, int y) {
        if (y < 8) {
            return new int[]{x, y + 1};
        }
        return new int[]{x+1, 0};
    }
}
```

## N-Queens

https://leetcode.com/problems/n-queens/

```
class Solution {
    // Time complexity: O(N!)
    // Space complexity: O(N^2)
    List<List<String>> res  = new ArrayList<>();

    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] i : board) {
            Arrays.fill(i, '.');
        }
        dfs(0, n, board);
        return res;
    }

    private void dfs(int idx, int n, char[][] board) {
        if (idx >= n) {
            List<String> lst = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                lst.add(new String(board[i]));
            }
            res.add(lst);
            return;
        }

        for (int i = 0; i < n; ++i) {
            if (!isValid(i, idx, n, board)) {
                continue;
            }
            board[i][idx] = 'Q';
            dfs(idx+1, n, board);
            board[i][idx] = '.';
        }
    }

    private boolean isValid(int x, int y, int n, char[][] board) {
        // Check same row and same column
        for (int i = 0; i < n; ++i) {
            if (board[x][i] == 'Q' || board[i][y] == 'Q') {
                return false;
            }
        }

        // Check left diagonal
        int len = Math.min(x, y);
        int i = x - len;
        int j = y - len;
        while (i < n && j < n) {
            if (board[i][j] == 'Q') {
                return false;
            }
            i++;
            j++;
        }

        // Check right dianonal
        len = Math.min(x, (n-y-1));
        i = x - len;
        j = y + len;
        while (i < n && j >= 0) {
            if (board[i][j] == 'Q') {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
```
