class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals)<2:
            return intervals
        
        #Constants for start and end of time intervals
        START,END=0,1
        result=[]

        #makke all intervals sorted on start and end time intervals in ascending order
        intervals.sort( key=lambda x: (x[START],x[END] ) )
        
    
        for interval in intervals:
            #no overlapping 
            if not result or (result[-1][END] < interval[START]):
                result.append(interval)
            #merge with previous interval    
            else:
                result[-1][END] = max(result[-1][END],interval[END])
                
        return result
    
    #Time complexity- O(n logn)
    #Space complexity- O(N)