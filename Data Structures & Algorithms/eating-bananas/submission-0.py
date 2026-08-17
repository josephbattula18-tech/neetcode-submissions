class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while(left<=right):
            mid = (left+right)//2
            hrs=0
            for pile in piles:
                hrs=((pile+mid-1)//mid)+hrs
            if hrs<=h:
                right=mid-1
            else:
                left=mid+1
        return left
        