class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        while i<len(chars):
            cnt=1
            temp=chars[i]
            i+=1
            while i<len(chars) and temp==chars[i]:
                chars.pop(i)
                cnt+=1
            # if cnt>1:
            #     str(cnt)
            # else:
            #     ""
            if cnt>1:
                for k in str(cnt):
                    chars.insert(i,k)
                    i+=1
        return len(chars)
            
