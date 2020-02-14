def climbStairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        n_1 = 2
        n_2 = 1
        for _ in range(3,n+1):
            total = n_1 + n_2
            n_2 = n_1
            n_1 = total
        return total

if __name__ == "__main__":
    print(climbStairs(6))