class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        for num in nums:
            mp[num] = mp.get(num,0) + 1

        ans = 0

        for key in mp:
            if mp.get(key-1,0): # Not the start of sequence
                continue
            else:
                # Start of sequence
                val = key
                curr = 1
                while mp.get(val+1,0):
                    curr+=1
                    val+=1
            ans = max(ans,curr)

        return ans