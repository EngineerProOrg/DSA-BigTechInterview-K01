## Number of Islands

https://leetcode.com/problems/number-of-islands/

```
class Solution {
    // Time complexity: O(M*N) where M is number of rows and N is number of columns
    // Space complexity: O(M*N)


    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};
    boolean[][] vis;


    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        vis = new boolean[m][n];


        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j] || grid[i][j] == '0') continue;
                res++;
                dfs(i, j, m, n, grid);
            }
        }    
        return res;
    }


    private void dfs(int x, int y, int m, int n, char[][] grid) {
        vis[x][y] = true;
        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || vis[u][v] || grid[u][v] == '0') continue;
            dfs(u, v, m, n, grid);
        }
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}
```

## Max Area of Island

https://leetcode.com/problems/max-area-of-island/

```
class Solution {
    // Time complexity: O(M*N) where M is number of rows and N is number of columns
    // Space complexity: O(M*N)


    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};


    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] vis = new boolean[m][n];
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j] || grid[i][j] == 0) {
                    continue;
                }
                res = Math.max(res, dfs(i, j, m, n, vis, grid));
            }
        }
        return res;
    }


    private int dfs(int x, int y, int m, int n, boolean[][] vis, int[][] grid) {
        vis[x][y] = true;
        int area = 1;
        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || vis[u][v] || grid[u][v] == 0) {
                continue;
            }
            area += dfs(u, v, m, n, vis, grid);
        }
        return area;
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}
```

## Count Sub Islands
https://leetcode.com/problems/count-sub-islands/

```
class Solution {
    // Time complexity: O(M*N)
    // Space complexity: O(M*N)
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};


    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int m = grid1.length;
        int n = grid1[0].length;
        boolean[][] vis = new boolean[m][n];


        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j] || grid2[i][j] == 0) continue;
                if (dfs(i,j,m,n,vis,grid1,grid2)) {
                    res++;
                }
            }
        }
        return res;
    }


    private boolean dfs(int x, int y, int m, int n, boolean[][] vis, int[][] grid1, int[][] grid2) {
        vis[x][y] = true;
        boolean res = grid1[x][y] == 1;


        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v,m,n) || vis[u][v] || grid2[u][v] == 0) continue;
            res &= dfs(u,v,m,n,vis,grid1,grid2);
        }
        return res;
    }


    private boolean inside(int x, int y, int m, int n) {
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}
```

## Shortest Bridge
https://leetcode.com/problems/shortest-bridge/

```
class Solution {
    // Time complexity: O(N^2)
    // Space complexity: O(N^2)
    int[] dx = new int[]{-1,0,1,0};
    int[] dy = new int[]{0,1,0,-1};
    boolean[][] vis;
    int n;


    public int shortestBridge(int[][] grid) {
        n = grid.length;
        vis = new boolean[n][n];
        boolean found = false;
        for (int i = 0; i < n && !found; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) {
                    continue;
                }
                dfs(i,j,grid);
                found = true;
                break;
            }
        }
        return bfs(grid);
    }


    private int bfs(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (vis[i][j] && grid[i][j] == 1) {
                    for (int k = 0; k < 4; ++k) {
                        int u = i + dx[k];
                        int v = j + dy[k];
                        if (!inside(u,v) || vis[u][v]) {
                            continue;
                        }
                        vis[u][v] = true;
                        q.add(new int[]{u,v});
                    }
                }
            }
        }


        int res = 0;
        while (!q.isEmpty()) {
            res++;
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                int[] cur = q.poll();
                for (int k = 0; k < 4; ++k) {
                    int u = cur[0] + dx[k];
                    int v = cur[1] + dy[k];
                    if (!inside(u,v) || vis[u][v]) {
                        continue;
                    }
                    if (grid[u][v] == 1) {
                        return res;
                    }
                    vis[u][v] = true;
                    q.add(new int[]{u,v});
                }
            }
        }
        return -1;
    }


    private void dfs(int x, int y, int[][] grid) {
        vis[x][y] = true;


        for (int k = 0; k < 4; ++k) {
            int u = x + dx[k];
            int v = y + dy[k];
            if (!inside(u,v) || vis[u][v] || grid[u][v] == 0) {
                continue;
            }
            dfs(u,v,grid);
        }
    }


    private boolean inside(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}
```
