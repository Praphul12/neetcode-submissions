import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}

        for num in nums:
            mp[num] = mp.get(num,0) + 1

        heap = []

        for key in mp:
            heapq.heappush(heap,(-mp[key],key))

        ans = []
        while k:
            freq,val = heap[0]
            ans.append(val)
            heapq.heappop(heap)
            k-=1
        
        return ans
