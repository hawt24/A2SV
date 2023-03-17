class Solution:
    def smallestCharFreq(self, s):
        sc = s[0]
        cnt = 1
        for idx in range(1,len(s)):
            c = s[idx]

            if c < sc: 
                cnt = 1
                sc= c 
            elif c == sc:
                cnt += 1
        return cnt

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        W = sorted([self.smallestCharFreq(i) for i in words])
        ans = []
        for q in queries:
            target = self.smallestCharFreq(q)
            ans.append(len(W) - bisect_left(W, target+1))

        return ans