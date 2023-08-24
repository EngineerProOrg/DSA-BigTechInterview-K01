## Target Sum
https://leetcode.com/problems/target-sum/

```
class Solution {
    // Time complexity: O(N*T) where N is lenght of the array and T is total sum. We go thru the dp array to fill the value. And we may go through N*T state once during DFS
    // Space complexity: O(N*T): storing the DP array for memorization
    int[][] dp;
    int n;
    int total;

    public int findTargetSumWays(int[] nums, int target) {
        int n = nums.length;
        total = 0;
        for (int i = 0; i < n; ++i) {
            total += nums[i];
        }        
        dp = new int[n][2*total + 1];
        for (int[] i : dp) {
            Arrays.fill(i, Integer.MIN_VALUE);
        }
        
        return dfs(0, n, nums, 0, target);
    }

    private int dfs(int idx, int n, int[] nums, int sum, int target) {
        if (idx >= n) {
            return target == sum ? 1 : 0;
        }
        if (dp[idx][sum + total] != Integer.MIN_VALUE) {
            return dp[idx][sum + total];
        }
        int count = 0;
        // Choose plus
        count += dfs(idx+1, n, nums, sum + nums[idx], target);
        // Choose minus
        count += dfs(idx+1, n, nums, sum - nums[idx], target);
        dp[idx][sum + total] = count;
        return count;
    }
}
```

## Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

```
class Solution {
    // Time complexity: O(K*(N + E)): Iterate K times. Each time we go through all the nodes. In each node, we go through all the edges of this node to compute the min time of this node for this iteration.
    // Space complexity: O(K*N)
    int INF = 1000000000;
    int res = INF;
    List<List<int[]>> cons = new ArrayList<>();
    int[][] dp;
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        for (int i = 0; i < n; ++i) {
            cons.add(new ArrayList<>());            
        }    
        for (int[] e : flights) {
            cons.get(e[0]).add(new int[]{e[1], e[2]});
        }
        dp = new int[n][k+1];
        for (int[] i : dp) {
            Arrays.fill(i, INF);
        }
        for (int i = 0; i < k; ++i) {
            for (int j = 0; j < n; ++j) {
                dfs(j, dst, i, i);
            }
            res = Math.min(res, dp[src][i]);
        }
        dfs(src, dst, k, k);
        res = Math.min(res, dp[src][k]);
        return res == INF ? -1 : res;
    }

    private int dfs(int cur, int dst, int remStop, int startStop) {       
        if (cur == dst) {
            return 0;
        }
        if (remStop < 0) {
            return INF;
        }
        if (remStop < startStop) {
            return dp[cur][remStop];
        }
        int val = INF;

        for (int[] u : cons.get(cur)) {
            int dis = u[1] + dfs(u[0], dst, remStop-1, startStop);
            val = Math.min(val, dis);
        }
        dp[cur][startStop] = val;
        return val;
    }
}
```

## House Robber III
https://leetcode.com/problems/house-robber-iii/

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Time complexity: O(N), for each house, we visit at most 2 times (one where we can rob, one where we cannot rob)
    // Space complexity: O(N): we store maximum value for each house for 2 conditions (can rob, cannot rob)
    Map<TreeNode, Map<Boolean, Integer>> map = new HashMap<>();

    public int rob(TreeNode root) {
        return dfs(root, true);
    }

    private int dfs(TreeNode node, boolean canRob) {
        if (node == null) {
            return 0;
        }
        if (map.containsKey(node) && map.get(node).containsKey(canRob)) {
            return map.get(node).get(canRob);
        }
        int val = 0;
        if (canRob) {
            int left = dfs(node.left, false);
            int right = dfs(node.right, false);
            val = node.val + left + right;
        }
        int maxValueIfNotRobThisHouse = dfs(node.left, true) + dfs(node.right, true);
        val = Math.max(val, maxValueIfNotRobThisHouse);
        if (!map.containsKey(node)) {
            map.put(node, new HashMap<>());
        }
        map.get(node).put(canRob, val);
        return val;

    }
}
```
