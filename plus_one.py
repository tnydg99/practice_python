def plusOne(digits):
    if len(digits):
        index = len(digits) - 1
        digits[index] += 1
        while digits[index] == 10:
            digits[index] = 0
            if index == 0:
                digits.insert(0, 1)
            else:
                index -= 1
                digits[index] += 1
    return digits

if __name__ == "__main__":
    print(plusOne([9,9,9,9]))