class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
       
        n = len(intervals)
        ans = 1
    
        current = intervals[0]
        
        for i in range(n):
            
            if intervals[i][0] >= current[1]:
                print(intervals[i][0],current[1])
                ans+=1
                current = intervals[i]
        return n - ans