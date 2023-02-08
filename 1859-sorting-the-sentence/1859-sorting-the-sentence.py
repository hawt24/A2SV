class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        dic={}
        for word in s:
            l_word=word[-1]
            dic[l_word]=word[:-1]
        dic=dict(sorted(dic.items()))
        return ' '.join(dic.values())

            
            