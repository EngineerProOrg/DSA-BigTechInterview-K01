# Tree - Live Coding Solutions

Speaker: Hiệp
## [1. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)

```java
class Solution {

    // last visited value
    long prev = Long.MIN_VALUE;

    // inorder traversal, the outcome should be increasing, i.e., next value must be greater than previous one
    private boolean dfs(TreeNode p) {
        if (p == null) return true;
        // recursively check left subtree: if it's not valid, the whole tree is invalid
        if (!dfs(p.left)) return false;
        // next value must be greater than the previous one
        if (p.val <= prev) return false;
        // update this node's value as the last one visited
        prev = p.val;
        // recursively check right subtree
        return dfs(p.right);
    }

    public boolean isValidBST(TreeNode root) {
        return dfs(root);
    }
}
```

```java
class Solution {

    // check if p's value is in the range [l, r]
    private boolean dfs(TreeNode p, long l, long r) {
        if (p == null) return true;
        // if p.val is out of range, the tree is invalid
        if (p.val < l || p.val > r) return false;
        // recursively check left subtree. The left node must be smaller than the current node
        if (!dfs(p.left, l, (long) p.val - 1)) return false;
        // recursively check right subtree. The right node must be greater than the current node
        if (!dfs(p.right, (long) p.val + 1, r)) return false;
        return true;
    }

    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
```

Complexity:

- Time: O(N), where N is total number of nodes.
- Space: O(h), where h is the depth of the tree.

## [2. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;

        // queue for BFS
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            // number of nodes on this level
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; ++i) {
                TreeNode p = q.poll();
                level.add(p.val);
                // push next level nodes to the queue
                if (p.left != null) q.add(p.left);
                if (p.right != null) q.add(p.right);
            }
            res.add(level);
        }
        return res;
    }
}
```

Complexity:

- Time: O(N), where N is total number of nodes.
- Space: O(N).

## [3. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

```java
class Solution {

    // count number of visited nodes
    int count = 0;

    // inorder traversal
    int dfs(TreeNode p, int k) {
        if (p == null) return -1;
        int tmp = dfs(p.left, k);
        // if the k-th nodes is found in the left subtree then return
        if (tmp != -1) return tmp;
        // increase the count when visiting p
        count++;
        // if this is the k-th node, return its value
        if (count == k) return p.val;
        // recursively find the k-th node in the right subtree
        return dfs(p.right, k);
    }

    public int kthSmallest(TreeNode root, int k) {
        return dfs(root, k);
    }
}
```

Complexity:

- Time: O(N), where N is total number of nodes.
- Space: O(h), where h is the depth of the tree.