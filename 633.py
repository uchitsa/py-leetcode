def judgeSquareSum(c: int) -> bool:
    i = 0
    while i*i<=c:
        b = sqrt(c - i*i)
        if int(b) == b:
            return True
        i += 1
    return False

if __name__ == '__main__':
    print(judgeSquareSum(0))
    print(judgeSquareSum(2))
    print(judgeSquareSum(4))
