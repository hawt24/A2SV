class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 or k==1:
            return 0
        parent=self.kthGrammar(n-1,ceil(k/2) )
        if parent==1 and k%2==1 or parent==0 and k%2==0:
            return 1
        return 0
     
  