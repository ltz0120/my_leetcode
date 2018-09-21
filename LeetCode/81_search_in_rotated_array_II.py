class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        start = 0
        end = len(nums) - 1
        s = []
        s.append([start, end])
        while s:
            start, end = s.pop(0)
            if start <= end:
                if start == end:
                    if nums[start] == target:
                        return True
                else:
                    mid = (start + end) / 2
                    print(mid)
                    if nums[mid] == target:
                        return True
                    if target == nums[0] or target == nums[-1]:
                        return True

                    elif target > nums[0]:
                        print("mid", mid)
                        if nums[mid] < nums[0]:
                            print("mid2", mid)
                            end = mid - 1
                            s.append([start, end])
                        elif nums[mid] == nums[0] and nums[0] == nums[-1]:
                            s.append([start, mid - 1])
                            s.append([mid + 1, end])
                        else:
                            if nums[mid] > target:
                                end = mid - 1
                            else:
                                start = mid + 1
                            s.append([start, end])
                    elif target < nums[-1]:
                        if nums[mid] > nums[-1]:
                            start = mid + 1
                            s.append([start, end])
                        elif nums[mid] == nums[0] and nums[0] == nums[-1]:
                            s.append([start, mid - 1])
                            s.append([mid + 1, end])
                        else:
                            if nums[mid] > target:
                                end = mid - 1
                            else:
                                start = mid + 1
                            s.append([start, end])

        return False