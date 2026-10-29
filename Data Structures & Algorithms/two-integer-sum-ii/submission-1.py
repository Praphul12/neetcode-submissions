class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1
        
        ans = []
        while low < high:
            val = numbers[low] + numbers[high]
            if val < target:
                low+=1
            elif val > target:
                high-=1
            else:
                ans.append(low+1)
                ans.append(high+1)
                break

        return ans
            