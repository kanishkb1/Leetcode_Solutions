class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array_length =len(nums)
        i = 0
        j = array_length // 2
        
        ls = []
        
        for i in range(array_length//2):
            ls.append(nums[i])
            ls.append(nums[j])
            i+=1
            j+=1
        return ls            
         
        #Time complexity- O(N^2)
        #Space complexity- O()