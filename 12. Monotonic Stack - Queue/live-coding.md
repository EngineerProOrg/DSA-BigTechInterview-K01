# Monotonic Stack & Queue - Live Coding Solutions

Speaker: Hiệp
## [1. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res[i] = 0 if not stack else stack[-1] - i
            stack.append(i)
        return res
```

Complexity:

- Time: O(N).
- Space: O(N).

## [2. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/description/)

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = nums + nums

        stack = []
        res = [-1]*n
        for i in range(2*n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if i < n:
                res[i] = -1 if not stack else arr[stack[-1]]
            stack.append(i)
        return res
```

Complexity:

- Time: O(N).
- Space: O(N).

## [3. Remove K Digits](https://leetcode.com/problems/remove-k-digits/description/)

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == n:
            return "0"
        l = n - k
        j = 0
        d = deque()
        res = ""
        for i in range(l):
            while j <= k + i:
                while d and d[-1] > num[j]:
                    d.pop()
                d.append(num[j])
                j += 1
            res += d.popleft()
        
        i = 0
        while i + 1 < len(res) and res[i] == '0':
            i += 1
        return res[i:]
```

Complexity:

- Time: O(N).
- Space: O(N).

## [4. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/)

```python
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minq = deque()
        maxq = deque()

        res = 0
        j = -1
        for i in range(n):
            while j + 1 < n:
                if minq and nums[j + 1] - nums[minq[0]] > limit:
                    break
                if maxq and nums[maxq[0]] - nums[j + 1] > limit:
                    break
                j += 1
                while minq and nums[minq[-1]] >= nums[j]:
                    minq.pop()
                while maxq and nums[maxq[-1]] <= nums[j]:
                    maxq.pop()
                minq.append(j)
                maxq.append(j)
            
            res = max(res, j - i + 1)

            if i == minq[0]:
                minq.popleft()
            if i == maxq[0]:
                maxq.popleft()
        return res
```

Complexity:

- Time: O(N).
- Space: O(N).