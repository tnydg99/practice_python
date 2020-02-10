def searchInsert(nums, target):
    if len(nums):
        if target in nums:
            return nums.index(target)
        else:
            for index in range(len(nums)):
                if nums[index] > target:
                    return index
            else: 
                return len(nums)
    else:
        return 0

if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 7))