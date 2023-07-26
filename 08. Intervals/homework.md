# Intervals - Homework Solutions

Speaker: Hiệp

## [1. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

```java
class Solution {
    public int findMinArrowShots(int[][] points) {
        int n = points.length;
        Arrays.sort(points, (p1, p2) -> Integer.compare(p1[1], p2[1]));

        int res = 1;
        int x = points[0][1];
        for (int[] p: points) {
            if (p[0] > x) {
                res++;
                x = p[1];
            }
        }
        return res;
    }
}
```

Complexity:

- Time: O(N * log N).
- Space: O(1).

## [2. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/description/)

```java
class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int n = firstList.length, m = secondList.length;
        List<int[]> res = new ArrayList<>();
        for (int i = 0, j = 0; i < n && j < m; ++i) {
            while (j < m && secondList[j][1] < firstList[i][0]) j++;
            while (j < m && secondList[j][0] <= firstList[i][1]) {
                int l = Math.max(firstList[i][0], secondList[j][0]);
                int r = Math.min(firstList[i][1], secondList[j][1]);
                res.add(new int[]{l, r});
                if (secondList[j][1] <= firstList[i][1]) {
                    j++;
                } else {
                    break;
                }
            }
        }
        return res.toArray(new int[0][]);
    }
}
```

Complexity:

- Time: O(N).
- Space: O(N).

## [3. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/description/)

```java
class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> {
            if (i1[0] != i2[0]) return i1[0] - i2[0];
            return i2[1] - i1[1];
        });
        int res = 0;
        int[] open = null;
        for (int[] interval: intervals) {
            if (open == null || interval[1] > open[1]) {
                res++;
                open = interval;
            }
        }
        return res;
    }
}
```

Complexity:

- Time: O(n * log n).
- Space: O(1).

## [4. Find Right Interval](https://leetcode.com/problems/find-right-interval/description/)

```java
class Solution {
    public int[] findRightInterval(int[][] intervals) {
        TreeSet<int[]> tree = new TreeSet<>((i1, i2) -> i1[0] - i2[0]);
        int n = intervals.length;
        for (int i = 0; i < n; ++i) {
            tree.add(new int[]{intervals[i][0], intervals[i][1], i});
        }

        int[] res =  new int[n];
        for (int i = 0; i < n; ++i) {
            var upper = tree.ceiling(new int[]{intervals[i][1], intervals[i][1]});
            if (upper == null) res[i] = -1;
            else res[i] = upper[2];
        }
        return res;
    }
}
```

Complexity:

- Time: O(N * log N).
- Space: O(N).

## [5. Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/)

```java
class Solution {
    public int minGroups(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> i1[0] - i2[0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((i1, i2) -> i1[1] - i2[1]);
        int res = 0;
        for (int[] i: intervals) {
            while (pq.size() > 0 && pq.peek()[1] < i[0]) pq.poll();
            pq.add(i);
            res = Math.max(res, pq.size());
        }
        return res;
    }
}
```

Complexity:

- Time: O(N * log N).
- Space: O(N).

## [6. Count Ways to Group Overlapping Ranges](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/description/)

```java
class Solution {

    private static final int mod = 1000000007;

    public int countWays(int[][] ranges) {
        Arrays.sort(ranges, (i1, i2) -> i1[0] - i2[0]);
        int n = ranges.length;
        int res = 1;
        int[] last = null;
        for (int[] i: ranges) {
            if (last == null || i[0] > last[1]) {
                res = (res + res) % mod;
                last = i;
            } else {
                last[1] = Math.max(last[1], i[1]);
            }
        }
        return res;
    }
}
```

Complexity:

- Time: O(n * log n).
- Space: O(1).

## [7. Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

```java
class SummaryRanges {

    private TreeSet<int[]> intervals;

    public SummaryRanges() {
        intervals = new TreeSet<>((i1, i2) -> i1[0] - i2[0]);
    }
    
    public void addNum(int value) {
        int[] interval = new int[]{value, value};
        var lower = intervals.floor(interval);
        if (lower != null && lower[1] >= value) return;
        
        int left = value, right = value;
        if (lower != null && lower[1] == value - 1) {
            left = lower[0];
            intervals.remove(lower);
        }
        var upper = intervals.ceiling(interval);
        if (upper != null && upper[0] == value + 1) {
            right = upper[1];
            intervals.remove(upper);
        }
        intervals.add(new int[]{left, right});
    }
    
    public int[][] getIntervals() {
        return intervals.toArray(new int[0][]);
    }
}
```

Complexity:

- Time: O(log n) per operation.
- Space: O(n).
