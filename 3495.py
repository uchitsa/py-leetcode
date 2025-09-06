import bisect

def minOperations(queries: List[List[int]]) -> int:
    steps = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456]
    prefixs = [0, 3, 27, 171, 939, 4779, 23211, 109227, 502443, 2271915, 10136235, 44739243, 195734187, 850045611, 3668617899]

    def get_subtotal(n):
        idx = bisect.bisect_right(steps, n)
        return prefixs[idx-1] + idx * (n - steps[idx-1])
    
    return sum((get_subtotal(r+1) - get_subtotal(l) + 1) // 2 for l, r in queries)

print(minOperations([1,2],[2,4]))
print(minOperations([2,6]))
