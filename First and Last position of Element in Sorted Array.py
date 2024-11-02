def searchRange(nums,target):
    def findLeft(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
    def findRight(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r
        
    left_index = findLeft(nums, target)
    right_index = findRight(nums, target)
        
    if left_index <= right_index and left_index < len(nums) and nums[left_index] == target:
        return [left_index, right_index]
    return [-1, -1]


nums=[5, 7, 7, 8, 8, 10]
target=8
print(searchRange(nums,target))
