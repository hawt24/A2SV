class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list)
        for idx, char in enumerate(s):
            dic[char].append(idx)

        count = 0

        for word in words:
            i = 0
            found = True
            for char in word:
                if char not in dic or not dic[char]:
                    found = False
                    break
                index = bisect_left(dic[char], i)
                if index == len(dic[char]):
                    found = False
                    break
                i = dic[char][index] + 1
            if found:
                count += 1

        return count
