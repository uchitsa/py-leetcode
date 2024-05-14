def mySqrt(x: int) -> int:
        lo = 0
        hi = x
        while lo<=hi:
            mi = (lo+hi)//2
            if mi*mi == x:
                return mi
            elif mi*mi>x:
                hi = mi - 1
            else:
                lo = mi + 1
        return hi

if __name__ == '__main__':
    print(mySqrt(4))
    print(mySqrt(8))
    