class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        left=0
        word=list(word)
        right=word.index(ch)
        while left<right:
            word[left],word[right]=word[right],word[left]
            right-=1
            left+=1
        return "".join(word)