class Solution:
    def trap(self, height: List[int]) -> int:
        lt=[0]*len(height)
        lt[0]=height[0]
        n=len(height)
        total=0
        
        rt=[0]*n
        rt[n-1]=height[n-1]
        for i in range(1,n):
            lt[i]=max(lt[i-1],height[i])
        for i in range(n - 2, -1, -1):
            rt[i]=max(rt[i+1],height[i])
        for i in range(n):
            if min(lt[i],rt[i])-height[i]>0:
                total = total + min(lt[i],rt[i])-height[i]
        return total
            