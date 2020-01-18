from functools import reduce

def longestCommonPrefix(strs: list) -> str:
    strs.sort(key=lambda x:len(x))
    if len(strs) == 0 or len(strs[0]) == 0:
        return ""
    prefix_number = 0
    letter = strs[0][prefix_number]
    is_prefixed = list(map(lambda x: x[0] == letter, strs))
    if not reduce(lambda x,y: x and y, is_prefixed):
        return ""
    else:
        prefix = ''
        while reduce(lambda x,y: x and y, is_prefixed) and prefix_number < len(strs[0]):        
            prefix += letter
            prefix_number += 1
            if prefix_number < len(strs[0]):
                letter = strs[0][prefix_number]
                is_prefixed = list(map(lambda x: x[prefix_number] == letter, strs))
        return prefix  

if __name__ == "__main__":
    print(longestCommonPrefix(["abab","aba",""]))