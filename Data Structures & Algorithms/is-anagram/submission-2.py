class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False

        
        for i in range(len(s)):
            if s[i] not in d1.keys():
                d1[s[i]] = 1
            else: 
                d1[s[i]] += 1

        for j in range(len(t)):
            
            if t[j] not in d2.keys():
                d2[t[j]] = 1
            else:
                d2[t[j]] += 1

        if d1 == d2:
            return True
        return False

            

        
        