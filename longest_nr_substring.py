def lengthOfLongestSubstring(s):
    letter_hash = {} 
    letter_index = 0
    highest_count = 0
    if s.isspace():
        return 1
    while letter_index < len(s):
        letter = s[letter_index] 
        if letter in letter_hash.keys():
            letter_index = letter_hash.pop(letter)
            letter_hash.clear()            
        else:
            letter_hash[letter] = letter_index
        if len(letter_hash) > highest_count:
            highest_count = len(letter_hash)
        letter_index += 1
    return highest_count

if __name__ == "__main__":
    print(lengthOfLongestSubstring('bbbbbbbbbbb'))
