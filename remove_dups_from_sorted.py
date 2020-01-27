def removeDuplicates(nums):
    if len(nums):
        dup_num = nums[0]
        index = 1
        while index < len(nums):
            if dup_num == nums[index]:
                nums.pop(index)
                index -= 1
            else:
                dup_num = nums[index]
            index += 1
    return len(nums)

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
    print(nums)