from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for word in strs:
            freq = [0]*26
            for i in word:
                freq[ord(i) - ord('a')]+=1
            mp[tuple(freq)].append(word)

        ans = []
        for key in mp:
            ans.append(mp[key])

        if len(ans):
            return ans
        else:
            temp = [" "]
            ans.append(temp)
            return ans