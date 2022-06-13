class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        n=len(nums)
    
    
        for i in range(n-2):
           
            pointer1=i+1
            pointer2=n-1
            
            while pointer1<pointer2:
                total = nums[i] + nums[pointer1] + nums[pointer2]
                
                if total==target:
                    return total
                
                if abs(total-target) <= diff:
                    diff = abs(total-target)
                    answer = total
                    
                if total<target:
                    pointer1+=1
                else:
                    pointer2-=1
                    
        return answer
    
 
    