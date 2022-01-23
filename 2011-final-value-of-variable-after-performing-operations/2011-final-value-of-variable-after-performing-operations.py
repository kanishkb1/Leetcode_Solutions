class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num=0
        for i in operations:
            if i[1]=='+':
                num+=1
            else:
                num-=1
        return num