def strStr(haystack, needle):
    letter_index = 0
    needle_index = 0
    reset_index = 0
    start_index = 0
    reset_changed = False
    while needle_index != len(needle) and letter_index < len(haystack):
        if haystack[letter_index] == needle[0] and not reset_changed:
            reset_index = letter_index
            if needle_index == 0:
                start_index = letter_index
            if reset_index > start_index:
                reset_changed = True
        if needle[needle_index] == haystack[letter_index]:
            needle_index += 1  
        else:
            needle_index = 0
            if reset_index > start_index: 
                letter_index = reset_index - 1
                reset_changed = False
        letter_index += 1
    return letter_index - len(needle) if needle_index == len(needle) else -1
        
if __name__ == "__main__":
    print(strStr('aabaaabaaac', 'aabaaac'))