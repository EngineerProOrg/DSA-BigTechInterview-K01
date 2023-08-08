# Sliding Window - Homework Solutions

Speaker: Hiệp

## [1. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/)

```java
class Solution {
    public int maxFrequency(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);

        int res = 0;
        long sum = 0;
        for (int i = 0, j = -1; i < n; ++i) {
            while (j + 1 < n && (long) (j - i + 1) * nums[j + 1] - sum <= k) {
                j++;
                sum += nums[j];
            }
            res = Math.max(res, j - i + 1);
            sum -= nums[i];
        }
        return res;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [2. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/description/)

```java
class Solution {
    public int totalFruit(int[] fruits) {
        int n = fruits.length;
        Map<Integer, Integer> cnt = new HashMap<>();
        int res = 0;
        for (int i = 0, j = -1; i < n; ++i) {
            while (j + 1 < n && (cnt.containsKey(fruits[j + 1]) || cnt.size() < 2)) {
                j++;
                cnt.put(fruits[j], cnt.getOrDefault(fruits[j], 0) + 1);
            }
            res = Math.max(res, j - i + 1);
            cnt.put(fruits[i], cnt.get(fruits[i]) - 1);
            cnt.remove(fruits[i], 0);
        }
        return res;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [3. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

```java
class Solution {

    private boolean isVowel(char c) {
        return c == 'u' || c == 'e' || c == 'o' || c == 'a' || c == 'i';
    }

    public int maxVowels(String s, int k) {
        int n = s.length();
        int cur = 0;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (isVowel(s.charAt(i))) cur++;
            if (cur > res) res = cur;
            if (i - k + 1 >= 0 && isVowel(s.charAt(i - k + 1))) cur--;
        }
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(n).

## [4. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int res = n + 1;
        int sum = 0;
        for (int i = 0, j = -1; i < n; ++i) {
            while (j < n && sum < target) {
                j++;
                if (j < n) sum += nums[j];
            }
            if (sum >= target) res = Math.min(res, j - i + 1);
            sum -= nums[i];
        }
        return res <= n ? res : 0;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).
