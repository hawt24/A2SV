class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        ans="/"
        i=0
        while i<len(path):
            temp=""
            while i<len(path) and path[i]=="/":
                i+=1
            while i<len(path) and path[i]!="/":
                temp+=path[i]
                i+=1
            if temp=="..":
                if stack:
                    stack.pop()
            elif temp==".":
                continue
            elif len(temp)>0:
                stack.append(temp)
        st=[]
        while stack:
            st.append(stack[-1])
            stack.pop()

        while st:
            tem=st[-1]
            if (len(st) != 1):
                ans += (tem + "/")
            else:
                ans+= tem
            st.pop()
        return ans

     
        
            
          
            