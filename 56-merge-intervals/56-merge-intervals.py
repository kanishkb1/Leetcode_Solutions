class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals)<2:
            return intervals
        
        START,END=0,1
        result=[]

        intervals.sort( key=lambda x: (x[START],x[END] ) )
        
        for interval in intervals:
            if not result or (result[-1][END] < interval[START]):
                result.append(interval)
                
            else:
                result[-1][END] = max(result[-1][END],interval[END])
                
        return result