def removeElement(nums, val):
    if len(nums):
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
            else:
                index += 1
    return len(nums)

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    removeElement(nums, 2)
    print(nums)