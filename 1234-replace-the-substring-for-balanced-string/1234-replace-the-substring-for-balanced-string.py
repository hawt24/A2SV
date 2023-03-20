class Solution:
    def balancedString(self, s: str) -> int:
        n=len(s)
        x=n//4
        count=Counter(s)
        dic={}
        for ch in ("Q","W","E","R"):
            if count[ch]>x:
                dic[ch]=count[ch]-x
    
        i=j=0
        ans=float('inf')
        counter=len(dic)          
        if counter==0:
            return 0
                                
        while j<n:
            if s[j] in dic:
                dic[s[j]]-=1
                if dic[s[j]]==0:
                    counter-=1
            j+=1
            while counter==0:       
                if s[i] in dic:
                    if dic[s[i]]==0:
                        counter+=1
                    dic[s[i]]+=1
                i+=1
                ans=min(ans,j-i+1)
        return ans