class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count=defaultdict(int)
        for i in cpdomains:
            num,i=i.split()
            num=int(num)
            space=i.split(".")
            
            while len(space)>0:
                name=".".join(space)
                space=space[1:]
                count[name]+=num
        
        ans=[]
        for key,val in count.items():
            ans.append(str(val)+" "+key)
        return ans
                
            
    