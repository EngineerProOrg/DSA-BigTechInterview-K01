## Unique Paths
https://leetcode.com/problems/unique-paths/

```
class Solution {
    // Time complexity: O(M*N)
    // Space complexity: O(M*N)
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for (int[] i : dp) {
            Arrays.fill(i, -1);
        }
        dp[m-1][n-1] = 1;
        return dfs(0, 0, m, n, dp);
    }

    private int dfs(int x, int y, int m, int n, int[][] dp) {
        if (dp[x][y] != -1) {
            return dp[x][y];
        }
        int val = 0;
        if (x < m-1) {
            val += dfs(x+1, y, m, n, dp);
        }

        if (y < n-1) {
            val += dfs(x, y+1, m, n, dp);
        }
        dp[x][y] = val;
        return val;
    }
}
```

## Out of Boundary Paths
https://leetcode.com/problems/out-of-boundary-paths/

```
class Solution {
    // Time complexity: O(M*N*K)
    // Space complexity: O(M*N*K)
    long mod = (long)1e9 + 7;

    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        long[][][] dp = new long[m][n][maxMove+1];
        for (long[][] i : dp) {
            for (long[] j : i) {
                Arrays.fill(j, -1);
            }
        }
        return (int)dfs(startRow, startColumn, m, n, dp, maxMove);
    }

    private long dfs(int x, int y, int m, int n, long[][][] dp, int maxMove) {
        if (maxMove == 0) {
            return 0L;
        }
        if (dp[x][y][maxMove] != -1) {
            return dp[x][y][maxMove];
        }
        long val = 0;
        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n)) {
                val++;
                continue;
            }
            val += dfs(u,v,m,n,dp,maxMove-1);
            val %= mod;
        }
        dp[x][y][maxMove] = val;
        return val;
    }

    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m & y >= 0 && y < n;
    }
}
```

## Word Break
https://leetcode.com/problems/word-break/

```
class Solution {
    // Time complexity: O(N^2 + M*K): N is length of S,  M length of wordDict, K is avg length of the string in word dict
    // Space complexity: O(N + M*K)
    private class Trie {
      Trie[] children = new Trie[26];
      boolean isWord;
    }

    Trie head = new Trie();
    int[] dp;

    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        for (String word : wordDict) {
          Trie cur = head;
          for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (cur.children[idx] == null) {
              cur.children[idx] = new Trie();
            }
            cur = cur.children[idx];
          }
          cur.isWord = true;
        }
        dp = new int[n];
        Arrays.fill(dp, -1);

        return dfs(0, s.toCharArray());
    }

    private boolean dfs(int idx, char[] arr) {
      if (idx >= arr.length) {
        return true;
      }
      if (dp[idx] != -1) {
        return dp[idx] == 1;
      }

      Trie cur = head;
      for (int i = idx; i < arr.length; ++i) {
        int c = arr[i] - 'a';
        if (cur.children[c] == null) {
          break;
        }
        cur = cur.children[c];
        if (cur.isWord) {
          if (dfs(i+1, arr)) {
            dp[idx] = 1;
            return true;
          }
        }
      }
      dp[idx] = 0;
      return false;
    }
}
```

## Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

```
class Solution {
    // Time complexity: O(M*N)
    // Space complexity: O(M*N)
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};

    int m, n;

    public int longestIncreasingPath(int[][] matrix) {
        m = matrix.length;
        n = matrix[0].length;

        int[][] dp = new int[m][n];
        for (int[] i : dp) {
            Arrays.fill(i, -1);
        }

        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dp[i][j] == -1) {
                    res = Math.max(res, dfs(i, j, matrix, dp));
                }
            }
        }

        return res;
    }

    private int dfs(int x, int y, int[][] matrix, int[][] dp) {
        if (dp[x][y] != -1) {
            return dp[x][y];
        }

        int val = 1;
        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u, v) || matrix[u][v] <= matrix[x][y]) {
                continue;
            }
            val = Math.max(val, 1 + dfs(u, v, matrix, dp));
        }
        dp[x][y] = val;
        return val;
    }

    private boolean inside(int x, int y) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}
```
