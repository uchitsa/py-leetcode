import collections
import bisect

class Packet:
    __slots__ = ('source','destination','timestamp')
    def __init__(self, source, destination, timestamp):
        self.source = source
        self.destination = destination
        self.timestamp = timestamp
    def __eq__(self,other):
        return (self.source == other.source and
                self.destination == other.destination and
                self.timestamp == other.timestamp)
    def __hash__(self):
        return hash((self.source, self.destination, self.timestamp))


class Router:

    def __init__(self, memoryLimit: int):
        self.memlim = memoryLimit
        self.pakque = collections.deque()
        self.unipak = set()
        self.desttime = collections.defaultdict(list)
        self.proccnt = collections.defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        newpak = Packet(source, destination, timestamp)
        if newpak in self.unipak:
            return False
        if len(self.pakque) == self.memlim:
            self._remove_oldest_packet()
        self.pakque.append(newpak)
        self.unipak.add(newpak)
        self.desttime[destination].append(timestamp)
        return True
    
    def _remove_oldest_packet(self):
        oldpak = self.pakque.popleft()
        self.unipak.remove(oldpak)
        dest = oldpak.destination
        self.proccnt[dest] += 1

    def forwardPacket(self) -> List[int]:
        if not self.pakque:
            return []
        pakfwd = self.pakque.popleft()
        self.unipak.remove(pakfwd)
        dest = pakfwd.destination
        self.proccnt[dest] += 1
        return [pakfwd.source, pakfwd.destination, pakfwd.timestamp]


    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.desttime:
            return 0
        timelist = self.desttime[destination]
        start = self.proccnt.get(destination, 0)
        left = bisect.bisect_left(timelist, startTime, start)
        right = bisect.bisect_right(timelist, endTime, start)
        return right-left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
