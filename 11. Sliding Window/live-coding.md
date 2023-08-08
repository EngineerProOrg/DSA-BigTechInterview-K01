# Sliding Window - Live Coding Solutions

Speaker: Hiệp
## [1. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/)

```java
class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int sum = 0;
        for (int i = 0; i < k - 1; ++i) sum += arr[i];

        int res = 0, n = arr.length;
        for (int i = 0; i + k - 1 < n; ++i) {
            sum += arr[i + k - 1];
            if (sum >= threshold * k) res++;
            sum -= arr[i];
        }
        return res;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [2. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();

        Set<Character> seen = new HashSet<>();
        int res = 0;
        for (int i = 0, j = -1; i < n; ++i) {
            while (j + 1 < n && !seen.contains(s.charAt(j + 1))) {
                j++;
                seen.add(s.charAt(j));
            }
            res = Math.max(res, j - i + 1);

            seen.remove(s.charAt(i));
        }
        return res;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [3. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

```java
class Solution {
    public int characterReplacement(String s, int k) {
        int n = s.length();
        int[] cnt = new int[26];
        int cntmax = 0, res = 0;
        for (int i = 0, j = -1; i < n; ++i) {
            while (j + 1 < n) {
                cnt[s.charAt(j + 1) - 'A']++;
                if (cnt[s.charAt(j + 1) - 'A'] > cntmax) cntmax = cnt[s.charAt(j + 1) - 'A'];

                if (j - i + 2 - cntmax > k) {
                    cnt[s.charAt(j + 1) - 'A']--;
                    break;
                }
                j++;
            }

            if (j - i + 1 > res) res = j - i + 1;

            cnt[s.charAt(i) - 'A']--;
        }
        return res;
    }
}
```

Complexity:

- Time: O(N).
- Space: O(1).

## [4. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        if (n > m) return false;

        int[] cnt = new int[26];
        int[] cnt2 = new int[26];
        int diff = 0;
        for (char c: s1.toCharArray()) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] == 1) diff++;
        }

        for (int i = 0; i < m; ++i) {
            int c = s2.charAt(i) - 'a';
            cnt2[c]++;
            if (cnt2[c] == cnt[c]) diff--;
            else if (cnt2[c] == cnt[c] + 1) diff++;

            if (diff == 0) return true;

            if (i - n + 1 >= 0) {
                c = s2.charAt(i - n + 1) - 'a';
                cnt2[c]--;
                if (cnt2[c] == cnt[c]) diff--;
                else if (cnt2[c] == cnt[c] - 1) diff++;
            }
        }
        return false;
    }
}
```

Complexity:

- Time: O(n + m).
- Space: O(1).