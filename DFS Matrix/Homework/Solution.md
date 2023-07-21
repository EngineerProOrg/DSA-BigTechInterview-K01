## Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/

```
class Solution {
    // Time complexity: O(M*N) where M is number of rows and N is number of columns
    // Space complexity: O(M*N)
   
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};


    public int countBattleships(char[][] board) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] vis = new boolean[m][n];
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j] || board[i][j] == '.') {
                    continue;
                }
                res++;
                dfs(i,j,m,n,vis,board);
            }
        }
        return res;
    }


    private void dfs(int x, int y, int m, int n, boolean[][] vis, char[][] board) {
        vis[x][y] = true;
        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || vis[u][v] || board[u][v] == '.') {
                continue;
            }
            dfs(u,v,m,n,vis,board);
        }
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}
```

## Find All Groups of Farmland

https://leetcode.com/problems/find-all-groups-of-farmland/

```
class Solution {
    // Time complexity: O(M*N) where M is number of rows and N is number of columns
    // Space complexity: O(M*N)    
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};


    public int[][] findFarmland(int[][] land) {
        int m = land.length;
        int n = land[0].length;
        List<int[]> lst = new ArrayList<>();
        boolean[][] vis = new boolean[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j] || land[i][j] == 0) {
                    continue;
                }
                int[] bottomRight = dfs(i,j,m,n,vis,land);
                lst.add(new int[]{i,j,bottomRight[0],bottomRight[1]});
            }
        }  
        return lst.toArray(new int[0][]);
    }


    private int[] dfs(int x, int y, int m, int n, boolean[][] vis, int[][] land) {
        vis[x][y] = true;
        int[] bottomRight = new int[]{x,y};
        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || vis[u][v] || land[u][v] == 0) {
                continue;
            }
            int[] next = dfs(u,v,m,n,vis,land);
            bottomRight[0] = Math.max(bottomRight[0], next[0]);
            bottomRight[1] = Math.max(bottomRight[1], next[1]);
        }
        return bottomRight;
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}
```

## Maximum Number of Fish in a Grid

https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/

```
class Solution {
    // Time complexity: O(M*N) where M is number of rows and N is number of columns
    // Space complexity: O(M*N)        
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};


    public int findMaxFish(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] vis = new boolean[m][n];
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0 || vis[i][j]) {
                    continue;
                }
                int value = dfs(i,j,m,n,vis,grid);
                res = Math.max(res, value);
            }
        }
        return res;
    }


    private int dfs(int x, int y, int m, int n, boolean[][] vis, int[][] grid) {
        vis[x][y] = true;


        int val = grid[x][y];


        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || vis[u][v] || grid[u][v] == 0) {
                continue;
            }
            val += dfs(u,v,m,n,vis,grid);
        }
        return val;
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }


}
```

## Detect Cycles in 2D Grid

https://leetcode.com/problems/detect-cycles-in-2d-grid/description/

```
class Solution {
    // Time complexity: O(M*N) where M is number of rows and N is number of columns
    // Space complexity: O(M*N)    
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};
    int m, n;


    public boolean containsCycle(char[][] grid) {
        m = grid.length;
        n = grid[0].length;


        boolean[][] vis = new boolean[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j]) continue;
                if (dfs(-1,-1,i,j,vis,grid)) {
                    return true;
                }
            }
        }    
        return false;
    }


    private boolean dfs(int prevX, int prevY, int x, int y, boolean[][] vis, char[][] grid) {
        vis[x][y] = true;


        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || grid[u][v] != grid[x][y] || (prevX == u && prevY == v)) continue;
            if (vis[u][v]) {
                return true;
            }
            if (dfs(x,y,u,v,vis,grid)) {
                return true;
            }
        }
        return false;
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}
```

## Path With Minimum Effort

https://leetcode.com/problems/path-with-minimum-effort/description/

```
class Solution {
    // Time complexity: O(M*N*Log(H)), where H is max possible height. In this case, H is constant 1000000. So can consider time complexity as O(M*N)
    // Space complexity: O(M*N)
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};


    public int minimumEffortPath(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        int lo = 0;
        int hi = 1000000;
        int res = hi;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            boolean[][] vis = new boolean[m][n];
            if (dfs(0, 0, m, n, vis, heights, mid)) {
                res = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return res;
    }


    private boolean dfs(int x, int y, int m, int n, boolean[][] vis, int[][] heights, int maxDif) {
        if (x == m-1 && y == n-1) {
            return true;
        }
        vis[x][y] = true;
        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || vis[u][v]) {
                continue;
            }
            int dif = Math.abs(heights[x][y] - heights[u][v]);
            if (dif > maxDif) {
                continue;
            }
            if (dfs(u,v,m,n,vis,heights,maxDif)) {
                return true;
            }
        }
        return false;
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}

```
