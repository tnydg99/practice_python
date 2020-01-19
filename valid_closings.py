def isValid(s: str) -> bool:
    mappings = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }
    char_list = ['x']
    for char in s:
        if char in mappings and char_list[-1] == mappings[char]:
            char_list.pop()
        else:
            char_list.append(char)
    return len(char_list) == 1

if __name__ == "__main__":
    print(isValid("((((((()))))))"))