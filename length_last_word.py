def lengthOfLastWord(s):
    return len(s.strip().split(" ")[len(s.strip().split(" ")) - 1])

if __name__ == "__main__":
    print(lengthOfLastWord('a '))