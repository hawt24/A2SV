class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words=s.split() 
        arr=[]
        for word in words:
            if word.isdigit():
                arr.append(int(word))
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                return False
        return True
       