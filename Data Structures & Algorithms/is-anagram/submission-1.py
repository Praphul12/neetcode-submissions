class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}

        for i in s:
            if i not in mp1:
                mp1[i] = 1
            else:
                mp1[i] +=1
        
        for i in t:
            if i not in mp2:
                mp2[i] = 1
            else:
                mp2[i] += 1
        

        for i in mp1:
            if i not in mp2:
                return False
            elif mp1[i] != mp2[i]:
                return False
        
        for i in mp2:
            if i not in mp1:
                return False
            elif mp1[i] != mp2[i]:
                return False
        
        return True
        