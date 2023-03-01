class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                val=0
                while stack and stack[-1]!="(":
                    val+=stack.pop()
                stack.pop()
                if val==0:
                    stack.append(1)
                else:
                    stack.append(val*2)
        return sum(stack)
            
        
        
        
      