def putMarbles(weights, k):
    n = len(weights)
    if k == 1 or k == n:
        return 0
    
    sums = []
    for i in range(n-1):
        sums.append(weights[i] + weights[i+1])

    sums.sort()

    minco = sum(sums[:k-1])
    maxco = sum(sums[-(k-1):])
    
    return maxco - minco


if __name__ == '__main__':
    weights = list(map(int, input().split()))
    k = int(input())
    print(putMarbles(weights, k))
