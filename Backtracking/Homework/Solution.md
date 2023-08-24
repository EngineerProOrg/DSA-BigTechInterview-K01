## Combinations
https://leetcode.com/problems/combinations/

```
class Solution {
    // Time complexity: O( n!/[(k-1)!( n-k)!]): there are O(nCk) solutions, i.e: number of ways to choose k elements from n elements, which is O( n!/[k!( n-k)!]). Then for each solution, we need O(k) operation to add the solution into the result list.
    // Space complexity: O(K)
    List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> combine(int n, int k) {
        dfs(1, n, k, new ArrayList<>());
        return res;
    }

    private void dfs(int cur, int n, int k, List<Integer> lst) {
        if (k == 0) {
            res.add(new ArrayList<>(lst));
            return;
        }
        for (int i = cur; i <= n-k+1; ++i) {
            lst.add(i);
            dfs(i+1, n, k-1, lst);
            lst.remove(lst.size()-1);
        }
    }
}
```

## Subsets
https://leetcode.com/problems/subsets

```
class Solution {
    // Time complexity: O(N*2^N): There are 2^N ways to choose a subset. For each subset, we need O(N) operation to copy into the result list
    // Space complexity: O(N)
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {        
        int n = nums.length;
        dfs(0,n,nums,new ArrayList<>());
        return res;
    }

    private void dfs(int idx, int n, int[] nums, List<Integer> lst) {
        if (idx >= n) {
            res.add(new ArrayList<>(lst));
            return;
        }
        lst.add(nums[idx]);
        dfs(idx+1,n,nums,lst);
        lst.remove(lst.size()-1);
        dfs(idx+1,n,nums,lst);
    }
}
```
## Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning

```
class Solution {
    // Time complexity: O(N*2^N)
    // - For each character, we have 2 choices: choose it for the current palindrome or start a new palindrom.
    // -> worst case, there are 2^N possible solutions. For each solutions, we take O(N) operation to add to the result list -> O(N*2^N)
    // We also have O(N^2) operations to store the palindrome array.
    // -> O(N*2^N) + O(N^2) = O(N*2^N)
    // Space complexity: O(N^2): we store the DP array which takes N^2. We also have the recursive stack frame which takes O(N). O(N^2) + O(N) = O(N^2)
    int n;
    List<List<String>> res = new ArrayList<>();
    boolean[][] dp;

    public List<List<String>> partition(String s) {
        char[] arr = s.toCharArray();
        n = arr.length;
        dp = new boolean[n][n];
        for (int i = 0; i < n; ++i) {
            dp[i][i] = true;
            for (int j = i-1; j >= 0; --j) {
                if (arr[j] == arr[i]) {
                    if (i - j == 1) {
                        dp[j][i] = true;
                    } else {
                        dp[j][i] = dp[j+1][i-1];
                    }
                }
            }
        }
        dfs(0, arr, new ArrayList<>());
        return res;
    }

    private void dfs(int idx, char[] arr, List<String> lst) {
        if (idx >= n) {
            res.add(new ArrayList<>(lst));
            return;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = idx; i < n; ++i) {
            sb.append(arr[i]);
            if (!dp[idx][i]) {
                continue;
            }
            lst.add(sb.toString());
            dfs(i+1,arr,lst);
            lst.remove(lst.size()-1);
        }
    }
}
```

## All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target

```
class Solution {
    // Time complexity: O(N*2^N):
    //  - We always choose start and end node. For each (N-2) intermedidate node: it has a chance to be in a valid path or not (2 chances) -> 2^(N-2) possible paths. So upper bound is O(2^N)
    //  - For each valid path, we need O(N) to copy the path to the result.
    // Space compleixty: O(N)
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n = graph.length;
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(0, n, graph, path);
        return res;
    }

    private void dfs(int node, int n, int[][] graph, List<Integer> path) {
        if (node == n-1) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int u : graph[node]) {
            path.add(u);
            dfs(u, n, graph, path);
            path.remove(path.size()-1);
        }
    }
}
```



