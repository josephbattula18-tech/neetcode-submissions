class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(len(nums)):
            target=-(nums[i])
            left = i+1
            right = n-1
            while left<right :
                if nums[left] + nums[right] == target:
                    ans.append([-(target), nums[left], nums[right]])
                    left = left+1
                    right = right-1
                elif nums[left] + nums[right] > target:
                    right=right-1
                elif nums[left] + nums[right] < target:
                    left = left+1
        ans = [list(x) for x in set(tuple(x) for x in ans)]    
        return ans