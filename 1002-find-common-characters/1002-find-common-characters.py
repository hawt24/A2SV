class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count={}
        for letter in words[0]:
            if letter in count:
                count[letter]+=1
            else:
                count[letter]=1
        for wor in words[1:]:
            word_count={}
            for letter in wor:
                if letter in word_count:
                    word_count[letter] += 1
                else:
                    word_count[letter] = 1
            for key in count:
                if key in word_count:
                    count[key] = min(count[key], word_count[key])
                else:
                    count[key] = 0
                    
        ans = []
        for key, val in count.items():
            if val > 0:
                word_count =[key] * val
                ans.extend(word_count)
        return ans
                
                    
                    
            
            