def addBinary(a, b):
    return str(bin(int(a, base=2) + int(b, base=2))).replace('0b', '')

if __name__ == "__main__":
    print(addBinary('11', '1'))