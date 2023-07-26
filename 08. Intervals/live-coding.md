# Intervals - Live Coding Solutions

Speaker: Hiệp
## [1. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

```java
class Solution {

    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> i1[0] - i2[0]);

        int n = intervals.length;
        List<int[]> result = new ArrayList<>();
        int[] last = null;
        for (int[] interval: intervals) {
            if (last != null && last[1] >= interval[0]) {
                last[1] = Math.max(last[1], interval[1]);
            } else {
                result.add(interval);
                last = interval;
            }
        }
        return result.toArray(new int[0][]);
    }
}
```

Complexity:

- Time: O(N * log N).
- Space: O(N).

## [2. Insert Interval](https://leetcode.com/problems/insert-interval/description/)

```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;
        int i = 0;
        List<int[]> res = new ArrayList<>();
        while (i < n && intervals[i][1] < newInterval[0]) {
            res.add(intervals[i]);
            i++;
        }
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.add(newInterval);
        while (i < n) {
            res.add(intervals[i++]);
        }
        return res.toArray(new int[0][]);
    }
}
```

Complexity:

- Time: O(N).
- Space: O(N).

## [3. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/)

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> i1[0] - i2[0]);
        int n = intervals.length;
        int[] current = null;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (current == null || current[1] <= intervals[i][0]) {
                current = intervals[i];
            } else {
                res++;
                if (intervals[i][1] < current[1]) {
                    current = intervals[i];
                }
            }
        }
        return res;
    }
}
```

Complexity:

- Time: O(N * log N).
- Space: O(1).
