# Two Pointers - Live Coding Solutions

Speaker: Hiệp
## [1. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length, cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (cnt < 2 || nums[i] != nums[cnt - 2]) {
                nums[cnt++] = nums[i];
            }
        }
        return cnt;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [2. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length - 1;
        while (i < j) {
            if (numbers[i] + numbers[j] == target) return new int[]{i + 1, j + 1};
            if (numbers[i] + numbers[j] > target) j--;
            else i++;
        }
        return null;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [3. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            int area = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, area);
            if (height[left] < height[right]) left++;
            else right--;
        }
        return maxArea;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [4. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)

```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) return null;
        ListNode slow = head, fast = head;
        
        while (true) {
            if (fast.next == null || fast.next.next == null) {
                return null;
            }
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) break;
        }

        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).