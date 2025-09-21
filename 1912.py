from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = {}
        self.availy = defaultdict(SortedList)
        self.rented = SortedList()
        
        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.availy[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        if movie not in self.availy:
            return []
        
        result = []
        for price, shop in self.availy[movie][:5]:
            result.append(shop)
        return result

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.availy[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.availy[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        res = []
        for price, shop, movie in self.rented[:5]:
            res.append([shop, movie])
        return res
