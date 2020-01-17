def reverse(x: int) -> int:
    is_negative = True if x < 0 else False
    str_abs_x = str(abs(x))
    reversed_int = 0 if int(str_abs_x[::-1]) > 2**31 - 1 else int(str_abs_x[::-1]) 
    return reversed_int if not is_negative else reversed_int * -1

if __name__ == "__main__":
    while True:
        try:
            print(reverse(int(input('What number would you like to reverse: '))))
            break
        except ValueError:
            print('Please enter in a number!')
            continue