class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1]*len(nums)

        L = [1]*len(nums)
        R = [1]*len(nums)

        temp = 1
        for i in range(len(nums)-1,-1,-1):
            R[i] = temp* nums[i]
            temp *= nums[i]

        temp = 1

        for i in range(len(nums)):
            L[i] = temp * nums[i]
            temp *= nums[i]
        

        for i in range(len(ans)):
            val_L = L[i-1] if i>0 else 1
            val_R = R[i+1] if i < len(ans) -1 else 1

            ans[i] = val_L * val_R

        return ans