# Monotonic Stack & Queue - Homework Solutions

Speaker: Hiệp

## [1. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/description/)

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        cnt = Counter(s)

        stack = []
        used = {chr(c + 97): False for c in range(26)}
        for c in s:
            cnt[c] -= 1
            if used[c]:
                continue
            while stack and cnt[stack[-1]] > 0 and stack[-1] > c:
                used[stack.pop()] = False
            stack.append(c)
            used[c] = True
        return ''.join(stack)
```

Complexity:

- Time: O(N).
- Space: O(1).

## [2. Online Stock Span](https://leetcode.com/problems/online-stock-span/description/)

```python
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.cnt = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        res = self.cnt + 1 if not self.stack else self.cnt - self.stack[-1][0]
        self.stack.append((self.cnt, price))
        self.cnt += 1
        return res
```

Complexity:

- Time: O(N).
- Space: O(N).

## [3. Jump Game VI](https://leetcode.com/problems/jump-game-vi/description/)

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0]*n
        f[0] = nums[0]
        d = deque()
        d.append(0)
        for i in range(1, n):
            while d and d[0] < i - k:
                d.popleft()
            f[i] = f[d[0]] + nums[i]
            while d and f[d[-1]] <= f[i]:
                d.pop()
            d.append(i)
        return f[n - 1]
```

Complexity:

- Time: O(n).
- Space: O(n).

## [4. 132 Pattern](https://leetcode.com/problems/132-pattern/description/)

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        minTo = [0]*n
        minTo[0] = nums[0]
        for i in range(1, n):
            minTo[i] = min(minTo[i - 1], nums[i])
        
        stack = [0]
        for k in range(1, n):
            while stack and nums[stack[-1]] <= nums[k]:
                stack.pop()
            if stack:
                j = stack[-1]
                if j > 0 and minTo[j - 1] < nums[k]:
                    return True
            stack.append(k)
        return False
```

Complexity:

- Time: O(N).
- Space: O(N).

## [5. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/description/)

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        right = [n]*n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = n if not stack else stack[-1]
            stack.append(i)
        
        stack = []
        res = 0
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left = -1 if not stack else stack[-1]
            res += arr[i] * (i - left) * (right[i] - i)
            stack.append(i)
        return res % 1000000007
```

Complexity:

- Time: O(N).
- Space: O(N).
