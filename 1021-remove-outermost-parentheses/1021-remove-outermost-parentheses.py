class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        stack=[]
        for i in range(len(s)):
            if(s[i]=="(" and c!=0):
                stack.append(s[i])
                c+=1
            elif(s[i]==")" and c!=1):
                stack.append(s[i])
                c-=1
            elif(s[i]=="(" and c==0):
                c+=1
            else:
                c-=1
        return "".join(stack)
       