def numWaterBottles(numBottles: int, numExchange: int) -> int:
    drunk = numBottles
    emptys = numBottles
    while emptys>=numExchange:
        neos = emptys//numExchange
        remains = emptys%numExchange
        drunk += neos
        emptys = remains + neos
    return drunk


print(numWaterBottles(9,3))
print(numWaterBottles(15,4))
