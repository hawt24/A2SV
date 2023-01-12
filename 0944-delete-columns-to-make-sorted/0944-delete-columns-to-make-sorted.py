class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        list1=[]
        delt=0
        for word in strs:
            list1.append(list(word))
        for i in range(len(list1[0])):
            for j in range(len(list1)-1):
                if list1[j][i]>list1[j+1][i]:
                    delt+=1
                    break
        return delt
                    
                    
                       
                       
            
            