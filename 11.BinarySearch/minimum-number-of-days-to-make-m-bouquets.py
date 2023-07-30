# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # x : days 
        # f(x) -> numberOfBouquets
        # smallest x  f(x) >= m
        # range of x = [0, max(bloomDay)]
        if m * k > len(bloomDay): 
            return -1

        low = 0
        high = max(bloomDay)
        res = high

        while low <= high:
            mid = low + (high - low) // 2

            cnt = self.numberOfBouquets(bloomDay, mid, k)

            if cnt >= m:
                res = min(res, mid)
                high = mid - 1

            else:
                low = mid + 1

        return res


    def numberOfBouquets(self, bloomDay: List[int], days: int, k: int):
        cnt = 0
        cnt_flowers = 0

        for x in bloomDay:
            if x <= days:
                cnt_flowers += 1
            else:
                cnt_flowers = 0
            if cnt_flowers == k:
                cnt += 1
                cnt_flowers = 0
        
        return cnt
