class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n =len(s)
        #two pointers were used 
        #first pointer from L->R
        #last pointer from R->L
        
        first = 0
        last = n-1
        while last > first:
            s[first],s[last] = s[last],s[first]  
            first+=1
            last-=1
    
            
                    