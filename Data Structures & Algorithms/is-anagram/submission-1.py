class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterT = {}
        counterS = {}
        for c in s:
            if c in counterS:
                counterS[c] += 1
            else:
                counterS[c] = 1
        
        for c in t:
            if c in counterT:
                counterT[c] += 1
            else:
                counterT[c] = 1
        
        if counterT == counterS:
            return True
        return False
