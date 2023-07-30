# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]: # (left -> mid) increasing
                if nums[left] <= target and nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            else: # (mid -> right) increasing 
                if nums[mid] <= target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
