import heapq
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.info = {}
        self.cuisimp = defaultdict(list)
        for foo, cuisi, rate in zip (foods, cuisines, ratings):
            self.info[foo] = (cuisi, rate)
            heapq.heappush(self.cuisimp[cuisi], (-rate, foo))


    def changeRating(self, food: str, newRating: int) -> None:
        cuisi, oldrate = self.info[food]
        self.info[food] = (cuisi, newRating)
        heapq.heappush(self.cuisimp[cuisi], (-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisimp[cuisine]
        while heap:
            negrate, foodname = heap[0]
            expectrate = - negrate
            realcusi, realrate = self.info[foodname]
            if expectrate == realrate:
                return foodname
            else:
                heapq.heappop(heap)
        return ""
    


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
