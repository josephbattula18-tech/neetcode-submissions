class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        best = 0

        while left < right:

            ar = (right - left)*(min(heights[left],heights[right])) 
            if best < ar:
                best = ar
            

            if heights[left]<heights[right]:
                left = left + 1
                
                
            else:
                right = right-1

        return best