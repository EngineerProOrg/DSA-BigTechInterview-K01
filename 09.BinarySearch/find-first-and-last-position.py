# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # start = end = 4 
        #  2 2 3 5 6 7
        # if a[mid] == target:
            # start = mid 
            # right = mid - 1

        # if a[mid] == target:
            # end = mid 
            # low = mid + 1

        ind = self.findSmallestIndex(nums, target) # 2
        if ind == len(nums) or nums[ind] != target: # not found  
            return [-1, -1]
        return [ind , self.findSmallestIndex(nums, target + 1) - 1]
        
    def findSmallestIndex(self, arr, target):
        # find smallest index >= target
        ind = len(arr)
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] >= target:
                ind = min(ind, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ind
