class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        last=strs[-1]
        first=strs[0]
        i=0
        while i<len(last) and i<len(first) and last[i]==first[i]:
            i+=1
        return first[:i]