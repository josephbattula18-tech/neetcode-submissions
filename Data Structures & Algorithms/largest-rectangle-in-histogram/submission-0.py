class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_a=0
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                area = h * width
                max_a = max(max_a, area)
            stack.append(i)
        i = len(heights)

        while stack:
            h = heights[stack.pop()]

            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            area = h * width
            max_a = max(max_a, area)

        return max_a