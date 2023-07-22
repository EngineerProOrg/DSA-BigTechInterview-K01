# Heap - Homework Solutions

Speaker: Hiệp

## [1. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x: nums) cnt.put(x, cnt.getOrDefault(x, 0) + 1);

        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> cnt.get(x) - cnt.get(y));
        for (int x: cnt.keySet()) {
            pq.add(x);
            if (pq.size() > k) pq.poll();
        }
        int[] res = new int[k];
        for (int i = 0; i < k; ++i) res[i] = pq.poll();
        return res;
    }
}
```

Complexity:

- Time: O(n * log k).
- Space: O(n).

## [2. Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set/)

```java
class SmallestInfiniteSet {

    Map<Integer, Boolean> removed;
    PriorityQueue<Integer> pq;
    int count;

    public SmallestInfiniteSet() {
        removed = new HashMap<>();
        pq = new PriorityQueue<>();
        count = 1;
    }
    
    public int popSmallest() {
        int res = pq.isEmpty() ? count++ : pq.poll();
        removed.put(res, true);
        return res;
    }
    
    public void addBack(int num) {
        if (removed.getOrDefault(num, false)) {
            removed.put(num, false);
            pq.add(num);
        }
    }
}
```

Complexity:

- Time: O(log n) per operation.
- Space: O(n).

## [3. Remove Stones to Minimize the Total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/)

```java
class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int res = 0;
        for (int x: piles) {
            pq.add(-x);
            res += x;
        }
        for (int i = 0; i < k; ++i) {
            int x = -pq.poll();
            res -= x / 2;
            pq.add(-((x + 1) / 2));
        }
        return res;
    }
}
```

Complexity:

- Time: O(n * log n).
- Space: O(n).

## [4. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/description/)

```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((p1, p2) -> p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1]);
        for (int[] p: points) {
            pq.add(p);
            if (pq.size() > k) pq.poll();
        }
        int[][] res = new int[k][];
        for (int i = 0; i < k; ++i) res[i] = pq.poll();
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(h).

## [5. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/)

```java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((cell1, cell2) -> matrix[cell1[0]][cell1[1]] - matrix[cell2[0]][cell2[1]]);
        int n = matrix.length;
        for (int i = 0; i < n && i < k; ++i) pq.add(new int[]{i, 0});

        for (int i = 0; i < k - 1; ++i) {
            int[] cell = pq.poll();
            if (cell[1] + 1 < n) pq.add(new int[]{cell[0], cell[1] + 1});
        }
        int[] res = pq.peek();
        return matrix[res[0]][res[1]];
    }
}
```

Complexity:

- Time: O(k * log k).
- Space: O(k).

## [6. Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/description/)

```java
class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        long[][] arr = new long[n][];
        for (int i = 0; i < n; ++i) arr[i] = new long[]{nums1[i], nums2[i]};
        Arrays.sort(arr, (p1, p2) -> Long.compare(p2[1], p1[1]));

        PriorityQueue<Long> pq = new PriorityQueue<>();
        long sum = 0;
        for (int i = 0; i < k - 1; ++i) {
            pq.add(arr[i][0]);
            sum += arr[i][0];
        }

        long res = 0;
        for (int i = k - 1; i < n; ++i) {
            res = Math.max(res, arr[i][1] * (arr[i][0] + sum));
            pq.add(arr[i][0]);
            sum += arr[i][0];
            sum -= pq.poll();
        }
        return res;
    }
}
```

Complexity:

- Time: O(n * log n).
- Space: O(n).
