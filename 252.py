class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            cur = intervals[i]

            if cur[0] < prev[1]:
                return False
        return True
