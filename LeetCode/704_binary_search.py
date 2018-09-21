class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            if start == end:
                if nums[start] != target:
                    return -1
                else:
                    return start
            else:
                # print(start, end)
                mid = (start + end) / 2
                # print(mid)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
