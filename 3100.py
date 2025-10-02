def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    a = 1
    b = 2 * numExchange - 3
    c = -2 * numBottles
    dis = b*b - 4*a*c
    t = math.ceil((-b+math.sqrt(dis))/(2*a))
    return numBottles + t - 1

print(maxBottlesDrunk(13,6))
print(maxBottlesDrunk(10,3))
