def twoSum(nums: list, target: int) -> list:
    indexes = []
    indexes_nums = list(enumerate(nums))
    indexes_nums.sort(key=lambda x: x[1])
    
    for index_num in indexes_nums:
        index, num = index_num
        for match_index in range(index + 1, len(indexes_nums)):
            print(f'{indexes_nums[match_index][1]} + {num} == {target}')
            if indexes_nums[match_index][1] + num == target:
                indexes.append(index)
                indexes.append(indexes_nums[match_index][0])
                break
    return indexes
    

if __name__ == "__main__":
    print(twoSum([-3,4,3,90], 0))