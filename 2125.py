class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre = 0
        res = 0
        for s in bank:
            cnt = 0
            for c in s:
                if c == '1':
                    cnt += 1
            if cnt != 0:
                res += pre*cnt
                pre = cnt
        return res
