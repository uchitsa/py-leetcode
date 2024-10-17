def maximumSwap(num: int) -> int:
    digs = list(str(num))
    seelast = {int(d): i for i,d in enumerate(digs)}
    for i,d in enumerate(digs):
        for swapd in range(9,int(d),-1):
            if swapd in seelast and seelast[swapd]>i:
                digs[i],digs[seelast[swapd]] = digs[seelast[swapd]],digs[i]
                return int(''.join(digs))
    return num


if __name__ == '__main__':
    print(maximumSwap(2736))
    print(maximumSwap(9973))
