# Tree - Homework Solutions

Speaker: Hiệp

## [1. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if ((p.val <= root.val && q.val >= root.val) || (p.val >= root.val && q.val <= root.val)) {
            return root;
        }
        if (p.val < root.val) return lowestCommonAncestor(root.left, p, q);
        else return lowestCommonAncestor(root.right, p, q);
    }
}
```

Complexity:

- Time: O(h) where `h` is the height of the tree.
- Space: O(h).

## [2. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

```java
class Solution {

    Map<Integer, Integer> pos;
    int cur;

    TreeNode solve(int[] pre, int[] in, int l, int r) {
        if (l > r) return null;
        TreeNode res = new TreeNode(pre[cur]);
        int u = pos.get(pre[cur]);
        cur++;
        res.left = solve(pre, in, l, u - 1);
        res.right = solve(pre, in, u + 1, r);
        return res;
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int n = preorder.length;
        pos = new HashMap<>();
        for (int i = 0; i < n; ++i) pos.put(inorder[i], i);
        cur = 0;

        return solve(preorder, inorder, 0, n - 1);
    }
}
```

Complexity:

- Time: O(n)
- Space: O(n).

## [3. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

```java
class Solution {

    List<Integer> res;

    void dfs(TreeNode p, int h) {
        if (p == null) return;
        if (h == res.size()) res.add(p.val);
        dfs(p.right, h + 1);
        dfs(p.left, h + 1);
    }

    public List<Integer> rightSideView(TreeNode root) {
        res = new ArrayList<>();
        dfs(root, 0);
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(n).

## [4. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)

```java
class BSTIterator {

    Stack<TreeNode> st;

    public BSTIterator(TreeNode root) {
        st = new Stack<>();
        while (root != null) {
            st.add(root);
            root = root.left;
        }
    }
    
    public int next() {
        TreeNode cur = st.pop();
        int res = cur.val;
        cur = cur.right;
        while (cur != null) {
            st.add(cur);
            cur = cur.left;
        }
        return res;
    }
    
    public boolean hasNext() {
        return !st.isEmpty();
    }
}
```

Complexity:

- Time: O(n).
- Space: O(h).

## [5. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

```java
class Solution {

    int res;

    void dfs(TreeNode p, int cur) {
        cur = cur * 10 + p.val;
        if (p.left == null && p.right == null) {
            res += cur;
            return;
        }
        if (p.left != null) dfs(p.left, cur);
        if (p.right != null) dfs(p.right, cur);
    }

    public int sumNumbers(TreeNode root) {
        res = 0;
        dfs(root, 0);
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(h).

## [6. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/)

```java
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        var newNode = new TreeNode(val);
        if (root == null) return newNode;
        TreeNode p = root, parent = null;
        while (p != null) {
            parent = p;
            if (p.val < val) p = p.right;
            else p = p.left;
        }
        if (parent.val < val) parent.right = newNode;
        else parent.left = newNode;
        return root;
    }
}
```

Complexity:

- Time: O(h).
- Space: O(1).

## [7. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

```java
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
            return root;
        }
        if (key > root.val) {
            root.right = deleteNode(root.right, key);
            return root;
        }

        if (root.left == null) return root.right;
        TreeNode p = root.left, parent = root;
        while (p.right != null) {
            parent = p;
            p = p.right;
        }
        root.val = p.val;
        if (parent != root) parent.right = p.left;
        else root.left = p.left;
        return root;
    }
}
```

Complexity:

- Time: O(h).
- Space: O(h).