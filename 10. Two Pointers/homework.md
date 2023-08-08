# Two Pointers - Homework Solutions

Speaker: Hiệp

## [1. 3Sum](https://leetcode.com/problems/3sum/description/)

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        Set<List<Integer>> res = new HashSet<>();
        for (int i = 0; i + 2 < n; ++i) {
            for (int j = i + 1, k = n - 1; j < k; ) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    res.add(List.of(nums[i], nums[j], nums[k]));
                    j++;
                } else if (nums[i] + nums[j] + nums[k] > 0) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        return new ArrayList<>(res);
    }
}
```

Complexity:

- Time: O(N^2).
- Space: O(N^2).

## [2. Reorder List](https://leetcode.com/problems/reorder-list/description/)

```java
class Solution {

    ListNode findMid(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    ListNode reverse(ListNode head) {
        ListNode prev = null, p = head;
        while (p != null) { 
            ListNode next = p.next;
            p.next = prev;
            prev = p;
            p = next;
        }
        return prev;
    }

    void merge(ListNode head, ListNode head2) {
        ListNode p = head, q = head2;
        while (p != null) {
            ListNode pnext = p.next;
            p.next = q;
            
            if (q != null) {
                ListNode qnext = q.next;
                q.next = pnext;
                q = qnext;
            }
            p = pnext;
        }
    }

    public void reorderList(ListNode head) {
        ListNode mid = findMid(head);
        
        ListNode secondHalf = mid.next;
        mid.next = null;

        ListNode p = reverse(secondHalf);
        merge(head, p);
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [3. Partition Labels](https://leetcode.com/problems/partition-labels/description/)

```java
class Solution {
    public List<Integer> partitionLabels(String s) {
        int n = s.length();
        int[] last = new int[26];
        for (int i = 0; i < n; ++i) last[s.charAt(i) - 'a'] = i;

        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            int j = i, k = last[s.charAt(i) - 'a'];
            while (j < k) {
                j++;
                k = Math.max(k, last[s.charAt(j) - 'a']);
            }
            res.add(j - i + 1);
            i = j;
        }
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(n).

## [4. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/description/)

```java
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1, res = 0;
        while (i <= j) {
            res++;
            if (people[i] + people[j] <= limit) {
                i++;
                j--;
            } else {
                j--;
            }
        }
        return res;
    }
}
```

Complexity:

- Time: O(N * log N).
- Space: O(1).

## [5. Minimum Number of Swaps to Make the String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/)

```java
class Solution {
    public int minSwaps(String s) {
        char[] arr = s.toCharArray();
        int d = 0, n = arr.length, res = 0;
        for (int i = 0, j = n - 1; i < j; ++i) {
            if (arr[i] == '[') d++;
            else d--;
            if (d < 0) {
                while (arr[j] == ']') j--;
                var tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                d += 2;
                res++;
            }
        }
        return res;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(N).

## [6. The k Strongest Values in an Array](https://leetcode.com/problems/the-k-strongest-values-in-an-array/)

```java
class Solution {
    public int[] getStrongest(int[] arr, int k) {
        Arrays.sort(arr);
        int n = arr.length;
        int i = 0, j = n - 1, m = arr[(n - 1) / 2];
        int[] res = new int[k];
        for (int u = 0; u < k; ++u) {
            if (m - arr[i] > arr[j] - m) res[u] = arr[i++];
            else res[u] = arr[j--];
        }
        return res;
    }
}
```

Complexity:

- Time: O(n * log n).
- Space: O(k).
