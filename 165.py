import itertools
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]
        for one, two in itertools.zip_longest(v1,v2,fillvalue=0):
            if one > two:
                return 1
            if two > one:
                return -1
        return 0
