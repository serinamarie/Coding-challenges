# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine 
# if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # UPER
        # edge case: could be empty or 1 interval
        # input: array (lol)
        # output: bool
        # plan: 
        
        sorted_intervals = sorted(intervals)
        
        for i in range(len(sorted_intervals)-1):
            if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
                return False
        return True